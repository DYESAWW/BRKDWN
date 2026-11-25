from textual.binding import Binding
from pathlib import Path
from BRKDWN.parsers.lhv_parser import csv_to_dict_lhv
from BRKDWN.parsers.swedbank_parser import csv_to_dict_swedbank
from BRKDWN.parsers.revolut_parser import csv_to_dict_revolut
from BRKDWN.db import insert_from_parser_to_db

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Button, Footer
from textual.containers import Vertical, Horizontal
from BRKDWN.tui.screens.file_selector import FileSelector
from BRKDWN.tui.screens.transactions import Transactions


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
					Button("IMPORT", classes="button", id="import"),
				),
				classes="center",
			),
			id="layout",
		)
		yield Footer(show_command_palette=False)

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "import":
			#self.app.clear_notifications()
			self.app.push_screen(FileSelector(), self.on_file_chosen) # push file selector on top

	def on_file_chosen(self, path: Path | None) -> None:
		"""Get path and use parser to import to db"""
		PARSERS = (csv_to_dict_lhv, csv_to_dict_swedbank, csv_to_dict_revolut) # declare parsers

		if path is None:
			return
		if path.suffix.lower() != ".csv": # check if file extension is csv
			self.notify("Please select a .csv file to import", severity="warning")
			return
		
		self.notify(f"Importing {path.name}")

		for parse in PARSERS: 
			data = parse(path)
			if data != -1: # one of the parsers will return data instead of -1
				insert_from_parser_to_db(data)
				#self.clear_notifications()
				self.notify(f"Imported {path.name}")
				 
				self.app.switch_screen(Transactions())
				return
		# every parser failed on this point (probably unsupported bank)
		self.notify("Please select a valid statement from Swedbank, LHV or Revolut", severity="warning")
