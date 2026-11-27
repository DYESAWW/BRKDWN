import sqlite3
from contextlib import closing
from pathlib import Path
from datetime import datetime

DB_PATH = Path("database.db")

def get_connection():
	"""Create cursor for database."""
	connection = sqlite3.connect(DB_PATH)
	connection.row_factory = sqlite3.Row
	return connection

def init_db():
	"""Initialize database, create table and declare entries"""
	# with closing() ensures that connection is closed #
	# with ensures that sqlite calls commit or rollback #
	with closing(get_connection()) as connection:
		with connection:
			connection.execute(
				"""
				CREATE TABLE IF NOT EXISTS transactions (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					IBAN TEXT NOT NULL,
					date TEXT NOT NULL,
					description TEXT,
					currency TEXT NOT NULL,
					amount REAL NOT NULL
				)
				"""
			)

def insert_from_parser_to_db(data):
	"""Insert dictionary provided by one of the parsers and insert transactions' data to database."""
	with closing(get_connection()) as connection:
		with connection:
			for i in range(len(data["IBAN"])):
				connection.execute(# the order down below is important
					"""
					INSERT INTO transactions
					(IBAN, date, description, currency, amount)
					VALUES (?, ?, ?, ?, ?)
					""",
					(
						data["IBAN"][i],
						data["date"][i],
						data["description"][i],
						data["currency"][i],
						data["amount"][i]
					),
				)

def sum_incomes() -> float:
	"""Sum incomes for further balance calculation"""
	with closing(get_connection()) as connection:
		result = connection.execute(# everything is calculated in sqlite request
			"""
			SELECT SUM(amount) AS total
			FROM transactions
			WHERE amount > 0
			"""
		).fetchone()
	# return 0 in case database is empty
	return result["total"] or 0 # result["total"] may be None in case db is empty

def sum_costs() -> float:
	"""Sum costs for further balance calculation"""
	with closing(get_connection()) as connection:
		result = connection.execute(
			"""
			SELECT SUM(amount) AS total
			FROM transactions
			WHERE amount < 0
			"""
		).fetchone()
	
	return result["total"] or 0 # result["total"] may be None in case db is empty

def IsEmptyDB() -> bool:
	"""Check if database is empty."""
	with closing(get_connection()) as connection:
		result = connection.execute(
			"SELECT EXISTS(SELECT 1 FROM transactions)"
		).fetchone()
	return not result[0]

def fetch_from_db_to_table() -> list:
	"""Prepare list sorted according to date and containing every element of database for table."""
	with closing(get_connection()) as connection:
		output_rows = [("IBAN", "DATE", "DESCRIPTION", "CURRENCY", "AMOUNT")] # Preapare columns for textual table
		rows = connection.execute("SELECT * FROM transactions").fetchall()
		sorted_rows = sorted(rows, key=lambda x: x[2], reverse=True) # sort according to date by default

		for row in sorted_rows:
			# format date
			date = datetime.strptime(row[2], "%Y%m%d").date()
			formatted_date = date.strftime("%d %b %Y")
			
			# insert tuples
			output_rows.append((
				row[1],
				formatted_date,
				row[3],
				row[4],
				row[5]
			))
		
	return output_rows