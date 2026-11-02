import csv

with open("data/F1Drivers_Dataset.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        driver = str('row[0]')
        if student_id > 395:
            print(f"{student_id}: {row[1]} {row[2]}")