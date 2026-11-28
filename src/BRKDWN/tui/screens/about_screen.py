from textual.binding import Binding
from textual.widgets import Static, Footer
from textual.containers import Vertical, VerticalScroll
from textual.app import ComposeResult
from textual.screen import Screen


class AboutScreen(Screen):

    BINDINGS = [
        Binding("escape", "app.pop_screen", "BACK"),
        Binding("q", "app.quit", "QUIT")
    ]

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Static("BRKDWN", id="about-title"),

            Vertical(
                Static("ABOUT THE PROJECT", classes="about-heading"),
                Static("BRKDWN helps users manage their income and expenses in one place."),
                classes="about-box"
            ),

            Vertical(
                Static("HOW IT WORKS", classes="about-heading"),
                Static("1. Import bank statements as CSV files."),
                Static("2. Combine statements from different banks."),
                Static("3. View your income and expenses."),
                Static("4. Export combined statements as a CSV file."),
                classes="about-box"
            ),

            Vertical(
                Static("SUPPORTED BANKS", classes="about-heading"),
                Static("Swedbank | LHV | Revolut"),
                classes="about-box"
            ),

            Vertical(
                Static("DEVELOPMENT ENVIRONMENT", classes="about-heading"),
                Static("Programming language: Python"),
                Static("User interface: Textual"),
                Static("Styling: TCSS"),
                Static("Database: SQLite3"),
                Static("Testing: pytest"),
                classes="about-box"
            ),

            Vertical(
                Static("DEVELOPERS", classes="about-heading"),
                Static("Konstantin Razdolski"),
                Static("Ain August Talts"),
                classes="about-box"
            ),

            id="about-content"
        )

        yield Footer()