import csv

def csv_to_dict_revolut(input_csv) -> dict | int:
	VALIDATION_DICT = {
		"english": [
			'Type', 'Product', 'Started Date', 'Completed Date', 'Description', 'Amount', 'Fee', 'Currency', 'State', 'Balance'
		],

		"russian": [
			'Тип', 'Продукт', 'Дата начала', 'Дата выполнения', 'Описание', 'Сумма', 'Комиссия', 'Валюта', 'State', 'Остаток средств'
		]
	}
	
	IBAN = "Revolut (IBAN unknown)"

	data = {
		"IBAN": [],
		"date": [],
		"description": [],
		"amount": [],
		"currency": []
	}
	with open(input_csv, encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile, delimiter=",") # set delimiter specific to each bank statement
		first_row = next(reader, None) # skip first row
		if first_row is not None and first_row in VALIDATION_DICT.values(): # compare headers to confirm file validity
			for row in reader:
				data["IBAN"].append(IBAN)
				data["date"].append(row[2][:10].replace("-", "")) # write into only date without time and remove "-" symbol
				data["description"].append(row[4])
				data["currency"].append(row[7])
				data["amount"].append(float(row[5]))
		else:
			return -1 # gotta check this to ensure that parse was successful
	return data
