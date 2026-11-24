import csv
from contextlib import closing
from . import db

def export_db_to_csv(filename):
	"""Fetch all database entries to csv file and write down to a file specified."""
	# fetch from db
	with closing(db.get_connection()) as connection:
		rows = connection.execute(
			"""
			SELECT IBAN, date, description, currency, amount
			FROM transactions
			"""
		).fetchall()

	# write into file
	with open(filename, "w", encoding="utf-8", newline="") as file:
		writer = csv.writer(file)

		writer.writerow( # create header (columns)
			["IBAN", "Date", "Description", "Currency", "Amount"]
		)

		for row in rows:
			writer.writerow( # write the rows in
				[
					row["IBAN"],
					row["date"],
					row["description"],
					row["currency"],
					row["amount"]
				]
			)