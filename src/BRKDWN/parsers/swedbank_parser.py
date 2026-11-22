
import csv

def csv_to_dict_swedbank(input_csv):
    VALIDATION_DICT = {
        "estonian": ["Kliendi konto", "Reatüüp", "Kuupäev", "Saaja/Maksja",
                     "Selgitus", "Summa", "Valuuta", "Deebet/Kreedit",
                     "Arhiveerimistunnus", "Tehingu tüüp", "Viitenumber",
                     "Dokumendi number"]
    }

    data = {
        "date": [],
        "description": [],
        "amount": [],
        "currency": []
    }

    with open(input_csv, encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        first_row = next(reader, None)

        if first_row is not None and first_row == VALIDATION_DICT["estonian"]:
            for row in reader:
                if row[1] == "20":
                    date = row[2].split(".")
                    data["date"].append(date[2] + date[1] + date[0])
                    data["description"].append(row[4])

                    amount = float(row[5].replace(",", "."))

                    if row[7] == "K":
                        amount = -amount

                    data["amount"].append(amount)
                    data["currency"].append(row[6])
        else:
            return -1

    return data
