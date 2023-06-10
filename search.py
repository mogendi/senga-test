import csv
from datetime import date
from typing import List, TypedDict

"""
    Helper for type hints
"""
class CustomerMetaData(TypedDict):
    ld: date
    count: int
    largest: int


"""
    O(nlogn + n)
    nlogn -> The data is pre-sorted
    n -> The counting traversal to determine frequencies
"""
def search(fp: str, n: int) -> List[str]:
    consecutiveOccurenceCounts = {}

    with open(fp) as src:
        srcData = csv.reader(src)
        next(srcData, None)
        csvData = sorted(srcData, key=lambda x: x[2])
        for data in csvData:
            formatedDate = date.fromisoformat(data[2][:-9])
            if data[0] not in consecutiveOccurenceCounts:
                consecutiveOccurenceCounts[data[0]] = {
                    "ld": formatedDate,
                    "count": 1,
                    "largest": 1,
                }
                continue

            inst: CustomerMetaData = consecutiveOccurenceCounts[data[0]]
            daysBtwnPayments = (formatedDate - inst["ld"]).days
            if daysBtwnPayments == 1:
                inst["count"] += 1
            if inst["count"] > inst["largest"]:
                inst["largest"] = inst["count"]
            if daysBtwnPayments > 1:
                inst["count"] = 1
            inst["ld"] = formatedDate

    items = consecutiveOccurenceCounts.items()
    queue = sorted(
        items,
        key=lambda x: (x[1]["largest"], (int("".join(str(ord(c)) for c in x[0])) * -1)),
        reverse=True,
    )

    return [item[0] for item in queue[:n]]
