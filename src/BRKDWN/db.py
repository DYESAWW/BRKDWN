import sqlite3
from contextlib import closing

def get_connection():
	connection = sqlite3.connect("database.db")
	connection.row_factory = sqlite3.Row
	return connection


def init_db():
	# with closing() ensures that connection is closed #
	# with ensures that sqlite calls commit or rollback #
	with closing(get_connection()) as connection:
		with connection:
			connection.execute(
				"""
				CREATE TABLE IF NOT EXISTS transactions (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					date TEXT NOT NULL,
					description TEXT,
					amount REAL NOT NULL,
					currency TEXT NOT NULL
				)
				"""
			)


def insert_from_parser_to_db(data):
	with closing(get_connection()) as connection:
		with connection:
			for i in range(len(data["type"])):
				connection.execute(
					"""
					INSERT INTO transactions
					(type, date, description, amount, currency)
					VALUES (?, ?, ?, ?)
					""",
					(
						data["date"][i],
						data["description"][i],
						data["amount"][i],
						data["currency"][i],
					),
				)


def sum_incomes():
	with closing(get_connection()) as connection:
		result = connection.execute(
			"""
			SELECT SUM(amount) AS total
			FROM transactions
			WHERE amount > 0
			"""
		).fetchone()

	return result["total"] or 0

def sum_costs():
	with closing(get_connection()) as connection:
		result = connection.execute(
			"""
			SELECT SUM(amount) AS total
			FROM transactions
			WHERE amount < 0
			"""
		).fetchone()

	return result["total"] or 0