from BRKDWN.parsers.lhv_parser import csv_to_dict_lhv

def test_csv_to_dict_lhv():
	result = csv_to_dict_lhv("tests/samples/anon-statement-lhv-short.csv")

	assert result == {
		"date": ["20260904", "20260905"],
		"description": ["Test 1", "Test 2"],
		"amount": [150.0, -150.0],
		"currency": ["EUR", "EUR"]
	}