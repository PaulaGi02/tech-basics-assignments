import csv

file = "Technical Basics I_2025 - Sheet1.csv"

try:
    with open(file, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        students = list(reader)
        print(f"Loaded {len(students)} students from {file}")
except FileNotFoundError:
    print(f"File {file} not found.")

