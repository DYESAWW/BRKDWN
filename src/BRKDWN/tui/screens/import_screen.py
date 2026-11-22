from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical, Horizontal
from BRKDWN.tui.screens.file_selector import FileSelector

LOGO = r"""
╔══════════════════════════════════════════════════════╗
║ ██████╗ ██████╗ ██╗  ██╗██████╗ ██╗    ██╗███╗   ██╗ ║
║ ██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██║    ██║████╗  ██║ ║
║ ██████╔╝██████╔╝█████╔╝ ██║  ██║██║ █╗ ██║██╔██╗ ██║ ║
║ ██╔══██╗██╔══██╗██╔═██╗ ██║  ██║██║███╗██║██║╚██╗██║ ║
║ ██████╔╝██║  ██║██║  ██╗██████╔╝╚███╔███╔╝██║ ╚████║ ║
║ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝ ║
╚══════════════════════════════════════════════════════╝
"""


class ImportScreen(Screen):
	def compose(self) -> ComposeResult:
		yield Vertical(
			Vertical(
				Static(LOGO, id="logo", markup=False),
				Horizontal(
					Button("IMPORT", classes="button", id="import"),
				),
				classes="center",
			),
			Button("ABOUT", id="about-button", classes="button"),  # add about page
			id="layout",
		)

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "import":
			self.app.push_screen(FileSelector())