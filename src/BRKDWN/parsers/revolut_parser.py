import csv

def csv_to_dict_revolut(input_csv):
	data = {
		"type": [],
		"date": [],
		"description": [],
		"amount": [],
		"currency": [],
		"balance": []
	}
	with open(input_csv) as csvfile:
		reader = csv.DictReader(csvfile, delimiter=",") # set delimiter specific to each bank statement
		for row in reader:
			print(row)
			data["type"].append(row["Type"])
			data["date"].append(row["Started Date"][:10].replace("-", "")) # write into only date without time and remove "-" symbol
			data["description"].append(row["Description"])
			data["amount"].append(float(row["Amount"]))
			data["currency"].append(row["Currency"])
			data["balance"].append(float(row["Balance"]))
	return data
