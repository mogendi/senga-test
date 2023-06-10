from search import search


def run_tests():
    testInsts = [
        ("test_data/transaction_data_1.csv", 1, ["K20008"]),
        ("test_data/transaction_data_2.csv", 3, ["K20987", "K20008", "K20233"]),
        (
            "test_data/transaction_data_3.csv",
            5,
            ["K20002", "K20005", "K20377", "K20987", "K22584"],
        ),
    ]

    for inst in testInsts:
        res = search(inst[0], inst[1])
        try:
            assert inst[2] == res
            print(f"\n{inst[0]} ✓\n")
        except AssertionError as e:
            print(f"\n{inst[0]} X\n")
            raise e
