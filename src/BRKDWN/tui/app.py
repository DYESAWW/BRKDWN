from textual.app import App

from BRKDWN.db import IsEmptyDB
from BRKDWN.tui.screens.import_screen import ImportScreen


class BrkdwnApp(App):
	CSS_PATH = "app.tcss"

	def on_mount(self) -> None:
		if IsEmptyDB():
			self.push_screen(ImportScreen())
		# else:
		# Here goes transactions screen