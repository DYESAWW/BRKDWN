from pathlib import Path
from BRKDWN.parsers.lhv_parser import csv_to_dict_lhv
from BRKDWN.parsers.swedbank_parser import csv_to_dict_swedbank
from BRKDWN.parsers.revolut_parser import csv_to_dict_revolut
from BRKDWN.db import insert_from_parser_to_db

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Button
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
			Button("ABOUT", id="about-button", classes="button"),  # add about page
			id="layout",
		)

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "import":
			self.app.clear_notifications()
			self.app.push_screen(FileSelector(), self.on_file_chosen)

	def on_file_chosen(self, path: Path | None) -> None:
		"""Get path and use parser to import to db"""
		PARSERS = (csv_to_dict_lhv, csv_to_dict_swedbank, csv_to_dict_revolut)

		if path is None:
			return
		if path.suffix.lower() != ".csv":
			self.notify("Please select a .csv file to import", severity="warning")
			return
		
		self.notify(f"Importing {path.name}")

		for parse in PARSERS:
			data = parse(path)
			if data != -1:
				insert_from_parser_to_db(data)
				self.app.clear_notifications()
				self.notify(f"Imported {path.name}")
				self.app.switch_screen(Transactions())
				return

		self.notify("Please select a valid statement from Swedbank, LHV or Revolut", severity="warning")
