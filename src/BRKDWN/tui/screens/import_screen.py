from textual.app import ComposeResult
from textual.screen import Screen
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


class ImportScreen(Screen):
	def compose(self) -> ComposeResult:
		yield Vertical(
			Vertical(
				Static(LOGO, id="logo", markup=False),
				Horizontal(
					Button("IMPORT", classes="button"),
				),
				classes="center",
			),
			Button("ABOUT", id="about"),  # add about page
			id="layout",
		)