import csv
from contextlib import closing
from . import db

def export_db_to_csv(filename):
	with closing(db.get_connection()) as connection:
		rows = connection.execute(
			"""
			SELECT type, date, description, amount, currency
			FROM transactions
			"""
		).fetchall()

	with open(filename, "w", encoding="utf-8", newline="") as file:
		writer = csv.writer(file)

		writer.writerow(
			["Type", "Date", "Description", "Amount", "Currency"]
		)

		for row in rows:
			writer.writerow(
				[
					row["type"],
					row["date"],
					row["description"],
					row["amount"],
					row["currency"],
				]
			)