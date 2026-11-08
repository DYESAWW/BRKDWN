import csv

def csv_to_dict_lhv(input_csv):
	VALIDATION_DICT = {
		"english": [
			"Customer account no", "Document no", "Date", "Sender/receiver account", "Sender/receiver name", "Debit/Credit (D/C)", "Amount","Reference number","Archiving code", "Description", "Currency", "Personal code or register code", "Sender/receiver bank BIC", "Ultimate debtor name", "Transaction reference", "Account servicer reference"
			],
		"estonian": [
			"Kliendi konto", "Dokumendi number", "Kuupäev", "Saaja/maksja konto", "Saaja/maksja nimi", "Deebet/Kreedit (D/C)", "Summa", "Viitenumber", "Arhiveerimistunnus", "Selgitus", "Valuuta", "Isikukood või registrikood", "Saaja/maksja panga BIC", "Makse algataja nimi", "Kande viide", "Konto teenusepakkuja viide"
			],
		"russian": [
			"Счёт клиента", "Номер документа", "Дата", "Счёт плательщика/получателя", "Имя плательщика/получателя", "Дебет/Кредит (D/C)", "Сумма", "Номер ссылки", "Признак архивирования", "Пояснение", "Валюта", "Личный код или регистрационный код", "BIC банка получателя/плательщика", "Имя инициатора платежа", "Ссылка проводки", "Ссылка поставщика счета"
		]
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
		if first_row is None or first_row not in VALIDATION_DICT.values():
			return -1
		for row in reader:
			data["date"].append(row[2].replace("-", "")) # write into only date without time and remove "-" symbol
			data["description"].append(row[9])
			data["amount"].append(float(row[6]))
			data["currency"].append(row[10])
	return data
