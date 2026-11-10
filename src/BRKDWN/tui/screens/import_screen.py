from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Vertical, Horizontal

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

class ImportScreen(App):
	CSS_PATH = "../app.tcss"
	def compose(self) -> ComposeResult:
		yield Vertical(
			Vertical(
				Static(LOGO, id="logo", markup=False),
				Horizontal(
					Button("IMPORT", classes="button"),
				),
				classes="center"
			),
			Button("ABOUT", id="about"), # add about page
			id="layout"
		)


def run_import_screen():
	ImportScreen().run()