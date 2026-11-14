from BRKDWN.parsers.swedbank_parser import csv_to_dict_swedbank
def test_csv_to_dict_swedbank():
    result = csv_to_dict_swedbank("tests/samples/anon-statement-swedbank copy.csv")

    assert result == {
        "date": ["20260910","20260910"],
        "description": ["Test 2", "Test 3"],
        "amount": [-100, 17.40],
        "currency": ["EUR", "EUR"],
    }