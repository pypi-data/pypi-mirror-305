import json
import logging
import os

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from ai_sec.reporting.callbacks import register_callbacks
from ai_sec.reporting.components import \
    create_footer  # Import shared components
from ai_sec.reporting.components import create_header, create_sidebar
from ai_sec.reporting.data_loader import load_report

logger = logging.getLogger(__name__)


class DashDashboard:
    def __init__(self, report_path, base_directory, host='127.0.0.1', port=8050):
        """
        Initialize the Dash dashboard with given report and configurations.
        
        :param report_path: Path to the linting report JSON file
        :param base_directory: Base directory for the project
        :param host: Host address for the Dash server
        :param port: Port number for the Dash server
        """
        self.app = dash.Dash(
            __name__,
            external_stylesheets=[dbc.themes.SPACELAB],  # Use Bootstrap for theming
            suppress_callback_exceptions=True
        )
        self.base_directory = base_directory
        self.report_path = report_path
        self.linter_data = self.load_linter_data(report_path)  # Load and process report data
        self.host = host  # Customize host
        self.port = port  # Customize port
        self.show_warning = not bool(os.getenv("OPENAI_API_KEY"))
        # Build the app layout with header, sidebar, and footer
        self.app.layout = self.create_app_layout()

        # Register callbacks
        self.register_callbacks()

    def load_linter_data(self, report_path):
        """
        Load the linter data from the given report file.
        :param report_path: Path to the report JSON file
        :return: Parsed linter data as list or dict
        """
        try:
            linter_data = load_report(report_path)
            if not linter_data:
                logger.warning("No linting issues found in the report.")
            else:
                logger.info(f"Linter data loaded from {report_path}.")
            return linter_data
        except FileNotFoundError:
            logger.error(f"Report file not found at {report_path}. Exiting dashboard.")
            return None
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from report file: {report_path}")
            return None

    def should_run(self):
        """
        Check if the dashboard should run by verifying if there are linting issues to display.
        
        :return: True if there are linting issues, False otherwise
        """
        if isinstance(self.linter_data, list):
            return len(self.linter_data) > 0  # Return True if list contains linting issues
        if isinstance(self.linter_data, dict):
            return self.linter_data and any(self.linter_data.get("linters", {}).values())  # Check for linting issues
        return False  # Default case: no issues

    def create_modal(self):
        """
        Create a modal to display detailed information about selected linter issues.
        """
        return dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Linter Issue Details")),
                dbc.ModalBody(html.Div(id="modal-body")),  # This will hold the issue details
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-modal-btn", className="ms-auto", n_clicks=0)
                ),
            ],
            id="modal",
            is_open=False,
        )

    def create_summary_cards(self):
        """
        Create summary cards to display passed, failed, and skipped checks.
        """
        summary = {}
        if isinstance(self.linter_data, dict):
            summary = self.linter_data.get("summary", {})

        passed = summary.get('passed', 0)
        failed = summary.get('failed', 0)
        skipped = summary.get('skipped', 0)
        passed_percentage, failed_percentage = self.calculate_percentage({
            'passed': passed,
            'failed': failed,
            'skipped': skipped
        })

        summary_cards = dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("Passed Checks", className="card-title"),
                    html.P(f"{passed} ({passed_percentage:.2f}%)"),
                ])
            ], color="success", inverse=True), width=4),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("Failed Checks", className="card-title"),
                    html.P(f"{failed} ({failed_percentage:.2f}%)"),
                ])
            ], color="danger", inverse=True), width=4),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("Skipped Checks", className="card-title"),
                    html.P(f"{skipped}"),
                ])
            ], color="warning", inverse=True), width=4),
        ])
        return summary_cards

    def calculate_percentage(self, summary):
        """
        Calculate the percentage of passed and failed checks.
        """
        total_checks = summary.get('passed', 0) + summary.get('failed', 0) + summary.get('skipped', 0)
        passed_percentage = (summary.get('passed', 0) / total_checks) * 100 if total_checks else 0
        failed_percentage = (summary.get('failed', 0) / total_checks) * 100 if total_checks else 0
        return passed_percentage, failed_percentage

    def create_app_layout(self):
        """
            Create the full layout of the app, including header, sidebar, content area, modal, and footer.
        """
        warning_message = None
        if self.show_warning:
            warning_message = dbc.Alert(
                "AI insights are disabled. Set the OPENAI_API_TOKEN environment variable to enable AI context for severity and context insights.",
                color="warning",
                style={"margin": "20px 0", "textAlign": "center"}
            )
        return dbc.Container([
            dcc.Location(id="url"),  # Tracks the URL for dynamic content loading
            create_header(),  # Use shared header
            dbc.Row([
                dbc.Col(
                    html.Div(create_sidebar(self.linter_data, "/"), id="sidebar-wrapper", style={"height": "100vh", "overflow-y": "auto"}),
                    width=2
                ),  # Sidebar with scroll
                dbc.Col(
                    html.Div([
                        warning_message,  # Insert warning here
                        html.Div(id="page-content", style={"overflow-y": "auto", "height": "calc(100vh - 120px)"})
                    ]),
                    width=10,
                )  # Main content with controlled scroll
            ]),
            create_footer(),  # Use shared footer
            self.create_modal(),  # Modal for issue details
        ], fluid=True)

    def register_callbacks(self):
        """
        Register the necessary callbacks for handling modals and other interactions.
        """
        register_callbacks(self.app, self.linter_data)

    def run(self):
        """
        Run the Dash dashboard server if linting issues are found.
        """
        if not self.should_run():
            logger.info("No issues to display. Exiting dashboard.")
            return

        issue_count = len(self.linter_data) if isinstance(self.linter_data, list) else len(self.linter_data['linters'])
        logger.info(f"Starting dashboard with {issue_count} linter issues.")

        # Run the Dash server
        self.app.run_server(debug=True, host=self.host, port=self.port)