import csv

if __name__ == "__main__":
    with open("input.csv", "r") as file:
        data = csv.DictReader(file, delimiter=",")
        for row in data:
            print(row)
            