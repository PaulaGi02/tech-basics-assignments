import csv
import random
from collections import defaultdict
from sys import argv

# Define weeks (excluding week 6)
weeks = [f"week{i}" for i in range(1, 14) if i != 6]
students = []

# Read CSV file
def read_csv(filename):
    global students
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            students = list(reader)
            print(f"✅ Loaded {len(students)} students from '{filename}'")
    except FileNotFoundError:
        print("🚨 File not found! Please check the filename.")
        exit()

# Populate scores for weeks 1–13 (skip week 6)
def populate_scores():
    for student in students:
        for week in weeks:
            val = student.get(week, "").strip()
            if val == "":
                student[week] = str(random.randint(1, 3))

# Calculate Total and Average Points
def calculate_all():
    for student in students:
        scores = []
        for week in weeks:
            try:
                val = int(student.get(week, "").strip())
                scores.append(val)
            except (ValueError, TypeError):
                continue

        top_10 = sorted(scores, reverse=True)[:10]
        total = sum(top_10)
        avg = sum(scores) / len(scores) if scores else 0

        student["Total Points"] = str(total)
        student["Average Points"] = f"{avg:.2f}"

# Write updated data to new CSV
def write_csv(output_file):
    fieldnames = list(students[0].keys())
    with open(output_file, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

# Bonus: Print nicely formatted analysis
def print_analysis():
    stream_scores = defaultdict(list)
    weekly_scores = defaultdict(list)

    for student in students:
        stream = student.get("Stream", "").strip().upper()
        try:
            avg = float(student["Average Points"])
            if stream:
                stream_scores[stream].append(avg)
        except ValueError:
            continue

        for week in weeks:
            try:
                score = int(student.get(week, "").strip())
                weekly_scores[week].append(score)
            except (ValueError, TypeError):
                continue

    print("\n📊 Grade Summary")
    print("=" * 35)

    for stream in sorted(stream_scores):
        scores = stream_scores[stream]
        avg = sum(scores) / len(scores) if scores else 0
        print(f"📘 Stream {stream} - Avg Points: {avg:.2f}")

    print("\n📅 Weekly Averages:")
    print("-" * 35)
    for week in weeks:
        scores = weekly_scores[week]
        avg = sum(scores) / len(scores) if scores else 0
        print(f"{week:<8}: {avg:.2f}")

# Main execution
if __name__ == "__main__":
    if len(argv) < 2:
        print("🚨 Please provide the input CSV file as an argument.")
        exit()

    filename = argv[1]
    print(f"📂 Opening file: {filename}")

    read_csv(filename)
    populate_scores()
    calculate_all()

    user_name = "paula"
    output_file = filename.replace(".csv", f"_calculated_by_{user_name}.csv")
    write_csv(output_file)
    print(f"\n✅ New file saved as: {output_file}")

    print_analysis()
