import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data=[]
        for row in reader:
            data.append({'longitude':row[0], 'latitude':row[1], 'housing_median_age':row[2], 'total_rooms':row[3], 'total_bedrooms':row[4], 'population':row[5], 'households':row[6], 'median_income':row[7], 'median_house_value':row[8]})

    with open (OUTPUT_FILENAME, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")