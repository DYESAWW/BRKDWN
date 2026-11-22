from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Static, Button, DirectoryTree
from textual.binding import Binding

class FileSelector(ModalScreen[bool]):
	def compose(self) -> ComposeResult:
		yield Vertical(
			Vertical(
				DirectoryTree("~/"),
				Button("confirm", classes="dialog-buttons")
			),
			classes="dialog"
		)