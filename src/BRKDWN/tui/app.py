from textual.app import App, ComposeResult
from textual.widgets import Footer, Static
from textual.binding import Binding
from textual.theme import Theme

from BRKDWN.db import IsEmptyDB
from BRKDWN.tui.screens.import_screen import ImportScreen
from BRKDWN.tui.screens.transactions import Transactions
from BRKDWN.tui.screens.about_screen import AboutScreen

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
		Binding("q", "app.quit", "QUIT"),
		Binding("a", "push_about_screen", "ABOUT"),
		Binding("i", "import_switch", "IMPORT"),
		Binding("t", "transactions_switch", "TRANSACTIONS")
	] # these bindings are global (excepting pushed screen like file_selector.py)

	def on_mount(self) -> None:
		self.register_theme(BRKDWN_THEME) # set theme
		self.theme = "BRKDWN"
		if IsEmptyDB(): # offer to import bank statement in case no database presented
			self.push_screen(ImportScreen())
		else:
			self.push_screen(Transactions())

	def push_screen(self, screen, callback=None, wait_for_dismiss=False):
		# override pushing function to clear notifications on screen pushing
		self.clear_notifications()
		return super().push_screen(screen, callback, wait_for_dismiss=wait_for_dismiss)

	def pop_screen(self):
		# override popping function to clear notifications on screen popping
		self.clear_notifications()
		return super().pop_screen()

	def action_push_about_screen(self) -> None:
		self.app.push_screen(AboutScreen())
	
	def action_import_switch(self) -> None:
		if not isinstance(self.app.screen, ImportScreen):
			self.app.push_screen(ImportScreen())
	
	def action_transactions_switch(self):
		if not isinstance(self.app.screen, Transactions):
			self.app.push_screen(Transactions())
			