import sqlite3

def get_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
	with get_connection() as connection:
		# Create table
		connection.execute(
			"""
				CREATE TABLE IF NOT EXISTS transactions (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						type TEXT NOT NULL,
						date TEXT NOT NULL,
						description TEXT,
						amount REAL NOT NULL,
						currency TEXT NOT NULL,
						balance REAL NOT NULL
				)
			"""
		)

def insert_from_parser_to_db(data):
	connection = get_connection()
	for i in range(len(data["type"])):
		connection.execute("""
		INSERT INTO transactions
		(type, date, description, amount, currency, balance)
		VALUES (?, ?, ?, ?, ?, ?)
	""", (data["type"][i], data["date"][i], data["description"][i], data["amount"][i], data["currency"][i], data["balance"][i]))
		connection.commit()