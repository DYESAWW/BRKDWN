from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical, Horizontal


class ImportScreen(Screen):
	def compose(self) -> ComposeResult:
		yield Vertical(
		)