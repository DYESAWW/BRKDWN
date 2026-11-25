from textual.binding import Binding
from textual.widgets import Static
from textual.containers import Vertical
from textual.app import ComposeResult
from textual.screen import Screen

class AboutScreen(Screen):

	BINDINGS = [
		Binding("escape", "app.pop_screen", "BACK"),
		Binding("q", "app.quit", "QUIT")
	]
	def compose(self) -> ComposeResult:
		yield Vertical(
			Static("ABOUT SCREEN")
		)