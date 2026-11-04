import db

def export_db_to_csv(filename):
	connection = db.get_connection()
	rows = connection.fetchall()
	with open(filename, "w", encoding="utf-8") as file:
		file.write("Type,Date,Description,Amount,Currency,Balance")
		for row in rows:
			file.write(f"")
