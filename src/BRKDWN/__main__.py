from BRKDWN.db import init_db
from BRKDWN.tui.app import BrkdwnApp


def main():
	init_db()
	BrkdwnApp().run() # textual app TUI

if __name__ == "__main__":
	main()