from textual.app import App
from textual.binding import Binding
from textual.theme import Theme

from BRKDWN.db import IsEmptyDB
from BRKDWN.tui.screens.import_screen import ImportScreen

BRKDWN_THEME = Theme(
	name="BRKDWN",
	primary="#e5c890",
	accent="#e64553",
	foreground="#cad3f5",
	background="#1e2030",
	surface="#1e2030",
	panel="#24273a",
	dark=True,
)

class BrkdwnApp(App):
	CSS_PATH = "app.tcss"
	BINDINGS = [
		Binding("q", "app.quit", "Quit"),
		Binding("escape", "app.pop_screen", "Back")
	]

	def on_mount(self) -> None:
		self.register_theme(BRKDWN_THEME)
		self.theme = "BRKDWN"
		if IsEmptyDB():
			self.push_screen(ImportScreen())
		# else:
		# Here goes transactions screen