import csv

def csv_to_dict_revolut(input_csv):
	VALIDATION_DICT = {
		"english": ['Type', 'Product', 'Started Date', 'Completed Date', 'Description', 'Amount', 'Fee', 'Currency', 'State', 'Balance'],
		"russian": ['Тип', 'Продукт', 'Дата начала', 'Дата выполнения', 'Описание', 'Сумма', 'Комиссия', 'Валюта', 'State', 'Остаток средств']
	}
	
	data = {
		"date": [],
		"description": [],
		"amount": [],
		"currency": []
	}
	with open(input_csv) as csvfile:
		reader = csv.reader(csvfile, delimiter=",") # set delimiter specific to each bank statement
		first_row = next(reader, None) # skip first row
		if first_row is not None and first_row == VALIDATION_DICT["english"] or first_row == VALIDATION_DICT["russian"]:
			for row in reader:
				data["date"].append(row[2][:10].replace("-", "")) # write into only date without time and remove "-" symbol
				data["description"].append(row[4])
				data["amount"].append(float(row[5]))
				data["currency"].append(row[7])
		else:
			return -1 # gotta check this to ensure that parse was successful
	return data
