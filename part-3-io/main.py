import csv

with open("input.csv", "r") as file:
    data = csv.DictReader(file, delimiter=",")
    for row in data:
        print({
            "id": row.get("id"),
            "name": row.get("name"),
            "email": row.get("email")
        })
