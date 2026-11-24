from pathlib import Path

from textual import events
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.message import Message
from textual.screen import ModalScreen
from textual.widgets import Button, DirectoryTree


class PickerTree(DirectoryTree):
	BINDINGS = [Binding("enter", "pick", "Import")]    # replace tree widget Enter binding

	# redeclare picking path to implement every input way (doubleclick, enter)
	class PathPicked(Message):
		def __init__(self, path: Path) -> None:
			super().__init__()
			self.path = path

	def action_pick(self) -> None:
		node = self.cursor_node
		if node is None or node.data is None:
			return
		if node.data.path.is_dir():
			node.toggle()
		else:
			self.post_message(self.PathPicked(node.data.path))


class FileSelector(ModalScreen[Path | None]):
	# this one should mirror global bindings as well
	BINDINGS = [ 
		Binding("escape", "cancel", "Cancel"),
		Binding("q", "app.quit", "Quit"),
	] 

	def compose(self) -> ComposeResult:
		yield Vertical(
			Vertical(
				PickerTree(Path.home(), id="tree"),
				Button("confirm", classes="dialog-buttons", id="confirm")
			),
			classes="dialog"
		)

	def on_mount(self) -> None:
		self.query_one("#tree", PickerTree).show_root = False
		self.notify("Choose your statement from Swedbank, LHV or Revolut")

	def get_highlighted_path(self) -> Path | None:
		"""Path of the entry under the tree cursor, or None if nothing or a folder is highlighted."""
		node = self.query_one("#tree", PickerTree).cursor_node
		if node is None or node.data is None:
			return None
		path = node.data.path
		return path if path.is_file() else None

	def confirm_selection(self) -> None:
		path = self.get_highlighted_path()
		if path is None:
			self.notify("Highlight a file first", severity="warning")
			return
		self.app.clear_notifications()
		self.dismiss(path)

	# enter on a file (press once)
	def on_picker_tree_path_picked(self, event: PickerTree.PathPicked) -> None:
		self.app.clear_notifications()
		self.dismiss(event.path)

	# confirm button
	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "confirm":
			self.confirm_selection()

	# double click (for mouse click)
	def on_click(self, event: events.Click) -> None:
		if event.chain != 2:
			return
		tree = self.query_one("#tree", PickerTree)
		if event.widget is None or tree not in event.widget.ancestors_with_self:
			return
		if self.get_highlighted_path() is not None:
			self.confirm_selection()

	def action_cancel(self) -> None:
		self.app.clear_notifications() # this ensures that notifications aren't stacked
		self.dismiss(None)