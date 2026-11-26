from textual.binding import Binding
from textual.widgets import Static, Footer
from textual.containers import Vertical, Horizontal
from textual.app import ComposeResult
from textual.screen import Screen


class AboutScreen(Screen):

    BINDINGS = [
        Binding("escape", "app.pop_screen", "BACK"),
        Binding("q", "app.quit", "QUIT")
    ]

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static("B R K D W N", id="about-title"),

            Vertical(
                Static("ABOUT THE PROJECT", classes="about-heading"),
                Static("BRKDWN helps users manage their income "
                       "and expenses in one place."),
                classes="about-box"
            ),

            Horizontal(
                Vertical(
                    Static("HOW IT WORKS", classes="about-heading"),
                    Static("1. Import bank statements."),
                    Static("2. Combine statements."),
                    Static("3. Analyse transactions."),
                    Static("4. Export as CSV."),
                    classes="about-box"
                ),

                Vertical(
                    Static("DEVELOPMENT ENVIRONMENT",
                           classes="about-heading"),
                    Static("Python - Programming language"),
                    Static("Textual - User interface"),
                    Static("TCSS - Styling"),
                    Static("SQLite3 - Database"),
                    Static("pytest - Testing"),
                    classes="about-box"
                ),
                classes="about-row"
            ),

            Horizontal(
                Vertical(
                    Static("SUPPORTED BANKS", classes="about-heading"),
                    Static("Swedbank | LHV | Revolut"),
                    classes="about-box"
                ),

                Vertical(
                    Static("DEVELOPERS", classes="about-heading"),
                    Static("Konstantin Razdolski"),
                    Static("Ain August Talts"),
                    classes="about-box"
                ),
                classes="about-row"
            ),

            id="about-content"
        )

        yield Footer()