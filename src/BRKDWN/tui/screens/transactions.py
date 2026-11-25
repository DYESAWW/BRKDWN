from textual.binding import Binding
from BRKDWN.db import fetch_from_db_to_table
from rich.text import Text

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, DataTable, Sparkline, Footer
from textual.containers import Vertical, Horizontal

class Transactions(Screen):
	def compose(self) -> ComposeResult:
		data = fetch_from_db_to_table()
		data.pop(0)
		amounts = []
		for i in range(len(data)):
			amounts.append(data[i][4])

		yield Vertical(
			DataTable(zebra_stripes=True),
			Sparkline(amounts),
		)
		yield Footer(classes="prevent_footer_overlap", show_command_palette=False)
		

	def on_mount(self) -> None:
		ROWS = fetch_from_db_to_table()
		table = self.query_one(DataTable)
		for column in ROWS[0]:
			styled_columns: list[Text] = [
				Text(str(column), style="#e5c890", justify="left")
			]
			table.add_columns(*styled_columns)
		for row in ROWS[1:]:
			# add styles to text in table
			styled_row = []
			for cell in row:
				if isinstance(cell, float) and cell > 0:
					styled_row.append(Text(str(cell), style="#a6da95", justify="center"))
				elif isinstance(cell, float) and cell < 0:
					styled_row.append(Text(str(cell), style="#e64553", justify="center"))
				elif isinstance(cell, float) and cell == 0.0:
					styled_row.append(Text(str(cell), justify="center"))
				else:
					styled_row.append(Text(str(cell), justify="left"))
			table.add_row(*styled_row)
		
		def on_screen_resume(self) -> None:
			# reload on after coming back
			self.reload_data()