from BRKDWN.parsers.swedbank_parser import csv_to_dict_swedbank
def test_csv_to_dict_swedbank():
    result = csv_to_dict_swedbank("tests/samples/anon-statement-swedbank")

    assert result == {
        "type": ["Card Payment", "Card Payment", "Card Payment", "Card Payment"],
        "date": ["20260910","20260910", "20260930" "20260930"],
        "description": ["Test 2", "Test 3", "Käive", "Käive"],
        "amount": [-100, -17.40, -566.00, 536.00],
        "currency": ["EUR", "EUR", "EUR", "EUR"],
        "balance": [None,None, None, None ]
     }