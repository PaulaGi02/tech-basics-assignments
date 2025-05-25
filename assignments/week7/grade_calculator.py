from sys import argv
import csv
import random

filename = "Technical Basics I_2025 - Sheet1.csv"
students = []
weeks = [f"week{i}" for week in range(1, 14) if i != 6]
# Step 1
def read_csv(filename):
    global students
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            students = list(reader)
            print(f"✅ Loaded {len(students)} students from '{filename}'")
    except FileNotFoundError:
        print ("File not found")
        exit()

# Step 2
def populate_scores():
    for student in students:
        for week in weeks:
            if week not in student:
                student[week] = ""  # Add missing week columns
            if week in weeks[5:]:
                if student.get(week) in (None, "", " "):
                    student[week] = str(random.randint(1, 3))

# Step 3
def calculate_all():
   for
    pass

def calculate_total(score):
    for student in students:
        scores = []
        for week in weeks:
            try:
                score = int(student.get(week, 0))
                scores.append(score)
            except (ValueError, TypeError):
                continue

    top_scores = sorted(scores, reverse=True) [:10]
    student["Total Points"] = str(sum(top_scores))


def calculate_average(scores):
    average =  0
    return average

# After the update let's save the data as a new csv file

def write_csv(filename):
    pass

# Bonus

def print_analysis():
    # print average scores for stream A, B and every week
    pass

if __name__ == "__main__":
    script, filename = argv

    print("Open file:", filename)

    read_csv(filename)

    populate_scores()
    calculate_all()

    user_name = "[your_name]"

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)
    print("New file written:", newname)

    print_analysis()

# Run the file with `python grade_calculator.py sheet.csv`