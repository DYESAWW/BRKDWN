import csv

def csv_to_dict_swedbank(input_csv):
    # Loon sõnastiku, kuhu salvestame tehingute andmed
    data = {
        "type": [],
        "date": [],
        "description": [],
        "amount": [],
        "currency": [],
        "balance": []
    }

    # Avame Swedbanki CSV-faili
    with open(input_csv, encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        first_row = next(reader, None)

        # Kontrollime, kas tegemist on õige CSV-failiga
        if first_row is not None and "Kuupäev" in first_row:
            for row in reader:
                amount = float(row[3].replace(",", "."))

                # Eristame sissetulekud ja väljaminekud
                data["type"].append("income" if amount > 0 else "expense")
                data["date"].append(row[0].replace(".", ""))
                data["description"].append(row[2])
                data["amount"].append(amount)
                data["currency"].append(row[4])
                data["balance"].append(float(row[5].replace(",", ".")))

        else:
            return -1

    # Tagastame töödeldud andmed
    return data