import csv

def csv_to_dict_swedbank(input_csv) -> dict | int:
	VALIDATION_DICT = {
		"estonian": [
			"Kliendi konto", "Reatüüp", "Kuupäev", "Saaja/Maksja", "Selgitus", "Summa", "Valuuta", "Deebet/Kreedit", "Arhiveerimistunnus", "Tehingu tüüp", "Viitenumber", "Dokumendi number"
		],
								
		"english": [
			"Client account", "Row type", "Date", "Beneficiary/Payer", "Details", "Amount", "Currency", "Debit/Credit", "Transfer reference", "Transaction type", "Reference number", "Document number"
		],

		"russian": [
			"Счëт клиентa", "Строковый тип", "Дата", "Получатель/Плательщик", "Пояснение", "Сумма", "Currency", "Дебит/Кредит", "Архивный признак", "Тип сделки", "Номер ссылки", "Номер документа"
		]
	}

	data = {
		"IBAN": [],
		"date": [],
		"description": [],
		"amount": [],
		"currency": []
	}

	with open(input_csv, encoding="utf-8") as csvfile:
		
		reader = csv.reader(csvfile, delimiter=";")
		first_row = next(reader, None)

		if first_row:
			while first_row and first_row[-1] == "":
				first_row.pop() # Remove empty columns in the end

		if first_row is not None and first_row in VALIDATION_DICT.values(): # compare headers to confirm file validity
			for row in reader:
				if row[1] == "20": # 20 row type means transaction (anything else is irrelevant)
					data["IBAN"].append(row[0])
					date = row[2].split(".")
					data["date"].append(date[2] + date[1] + date[0])
					data["description"].append(row[4])
					data["currency"].append(row[6])

					amount = float(row[5].replace(",", "."))

					if row[7] == "K": # debit/credit
						amount = -amount

					data["amount"].append(amount)
		else:
			return -1

	return data

