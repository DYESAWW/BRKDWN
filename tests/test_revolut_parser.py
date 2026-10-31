from BRKDWN.parsers.revolut_parser import csv_to_dict_revolut

def test_csv_to_dict_revolut():
	result = csv_to_dict_revolut("tests/samples/anon-statement-revolut-short.csv")

	assert result == {
		"type": ["Card Payment", "Deposit"],
		"date": ["20220601", "20220604"],
		"description": ["Item-b1eee5fa", "Item-5aca29d2"],
		"amount": [-4.37, 2.1],
		"currency": ["EUR", "EUR"],
		"balance": [137.12, 139.22]
	}