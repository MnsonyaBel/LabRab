# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_file:
        csv_reader = csv.DictReader(input_file)
        data = list(csv_reader)

    with open(OUTPUT_FILENAME, 'w') as output_file:
        json.dump(data, output_file, indent=4)

if '__name__' == '__main__':
    task()

    with open(OUTPUT_FILENAME, 'r') as output_f:
        for line in output_f:
            print(line, end="")