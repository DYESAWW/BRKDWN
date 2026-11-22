import time
from pathlib import Path

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, DirectoryTree


class FileSelector(ModalScreen[Path | None]):    # returns a path, or None on cancel
	DOUBLE_CLICK_SECONDS = 0.4

	BINDINGS = [
		Binding("escape", "cancel", "Cancel"),
		Binding("enter", "confirm", "Import", priority=True),
		Binding("q", "app.quit", "Quit"),
	]

	def __init__(self) -> None:
		super().__init__()
		self._last_click_path: Path | None = None
		self._last_click_time = 0.0

	def compose(self) -> ComposeResult:
		yield Vertical(
			Vertical(
				DirectoryTree(Path.home(), id="tree"),
				Button("confirm", classes="dialog-buttons", id="confirm")
			),
			classes="dialog"
		)

	def on_mount(self) -> None:
		self.query_one("#tree", DirectoryTree).show_root = False
		self.notify("Choose your statement from Swedbank, LHV or Revolut")

	def get_highlighted_path(self) -> Path | None:
		"""Path of the entry under the tree cursor, or None if nothing or a folder is highlighted."""
		node = self.query_one("#tree", DirectoryTree).cursor_node
		if node is None or node.data is None:
			return None
		path = node.data.path
		return path if path.is_file() else None

	def confirm_selection(self) -> None:
		path = self.get_highlighted_path()
		if path is None:
			self.notify("Highlight a file first", severity="warning")
			return
		self.dismiss(path)

	# Confirm button
	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "confirm":
			self.confirm_selection()

	# Double click on a file
	def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
		now = time.monotonic()
		is_double = (
			event.path == self._last_click_path
			and now - self._last_click_time <= self.DOUBLE_CLICK_SECONDS
		)
		self._last_click_path = event.path
		self._last_click_time = now
		if is_double:
			self.confirm_selection()

	def action_cancel(self) -> None:
		self.app.clear_notifications()
		self.dismiss(None)