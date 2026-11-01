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
		reader = csv.reader(csvfile, delimiter=",") # set delimiter specific to each bank statement
		first_row = next(reader, None) # skip first row
		if first_row is not None and first_row == ['Type', 'Product', 'Started Date', 'Completed Date', 'Description', 'Amount', 'Fee', 'Currency', 'State', 'Balance']:
			for row in reader:
				data["type"].append(row[0])
				data["date"].append(row[2][:10].replace("-", "")) # write into only date without time and remove "-" symbol
				data["description"].append(row[4])
				data["amount"].append(float(row[5]))
				data["currency"].append(row[7])
				data["balance"].append(float(row[9]))
		else:
			return -1 # gotta check this to ensure that parse was successful
	return data
