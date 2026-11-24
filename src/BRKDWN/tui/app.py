from textual.app import App
from textual.binding import Binding
from textual.theme import Theme

from BRKDWN.db import IsEmptyDB
from BRKDWN.tui.screens.import_screen import ImportScreen
from BRKDWN.tui.screens.transactions import Transactions

BRKDWN_THEME = Theme( # declare theme
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
	] # these bindings are global (excepting pushed screen like file_selector.py)

	def on_mount(self) -> None:
		self.register_theme(BRKDWN_THEME) # set theme
		self.theme = "BRKDWN"
		if IsEmptyDB(): # offer to import bank statement in case no database presented
			self.push_screen(ImportScreen())
		else:
			self.push_screen(Transactions())