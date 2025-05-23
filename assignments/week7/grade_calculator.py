import csv
import random

file = "Technical Basics I_2025 - Sheet1.csv"

try:
    with open(file, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        students = list(reader)
        #print(f"Loaded {len(students)} students from {file}")
except FileNotFoundError:
    print(f"File {file} not found.")

weeks = [f"Week {i}" for i in range(1, 14) if i != 6]

for student in students:
    for week in weeks:
        if student.get(week) in (None, "", " "):
            student[week] = str(random.randint(1, 3))
