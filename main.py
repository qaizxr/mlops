import csv


def load_students(path="student.csv"):
    """Read the student records from the CSV file."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    students = load_students()
    print(f"Loaded {len(students)} students")
    for student in students:
        print(f"{student['name']} (age {student['age']}, {student['major']})")


if __name__ == "__main__":
    main()
