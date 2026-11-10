from BRKDWN.tui.screens.import_screen import run_import_screen
from BRKDWN.db import init_db, IsEmptyDB
from pathlib import Path

def main():
	init_db()
	if IsEmptyDB:
		run_import_screen()
#	else:
# Here goes transactions screen

if __name__ == "__name__":
	main()