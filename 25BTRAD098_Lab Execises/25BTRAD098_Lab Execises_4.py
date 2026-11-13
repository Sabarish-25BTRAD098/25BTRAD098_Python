# LAB EXERCISE 11: LOG FILE READER PROGRAM
def read_and_summarize_log(filename):
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                upper_line = line.upper()

                for keyword in counts:
                    counts[keyword] += upper_line.count(keyword)

        print("\nLOG SUMMARY")
        print("-------------------------")

        for keyword, count in counts.items():
            print(f"{keyword}: {count}")

        if all(count == 0 for count in counts.values()):
            print("No ERROR, WARNING or INFO entries found.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print("Error: Permission denied while reading the file.")

    except OSError as error:
        print("Unable to read the file:", error)


def main():
    filename = input("Enter log file name (example: app.log): ").strip()

    if not filename:
        print("File name cannot be empty.")
        return

    read_and_summarize_log(filename)


if __name__ == "__main__":
    main()

# LAB EXERCISE 12: STUDENT DATA MANAGER USING FILES
# Records are stored permanently in students.csv.
import csv
import os

FILENAME = "students.csv"
FIELDS = ["roll_no", "name", "course", "email"]


def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_students():
    ensure_file()

    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_students(students):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    students = load_students()

    roll_no = input("Enter roll number: ").strip()

    if not roll_no:
        print("Roll number cannot be empty.")
        return

    if any(s["roll_no"] == roll_no for s in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    email = input("Enter email: ").strip()

    if not name or not course:
        print("Name and course are required.")
        return

    students.append({
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "email": email
    })

    save_students(students)
    print("Student record saved successfully.")


def display_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n{:<12} {:<20} {:<15} {}".format(
        "ROLL NO", "NAME", "COURSE", "EMAIL"))

    print("-" * 70)

    for s in students:
        print("{:<12} {:<20} {:<15} {}".format(
            s["roll_no"], s["name"], s["course"], s["email"]))


def search_student():
    roll_no = input("Enter roll number to search: ").strip()

    for s in load_students():
        if s["roll_no"] == roll_no:
            print("Record found:", s)
            return

    print("Student not found.")


def update_student():
    students = load_students()

    roll_no = input("Enter roll number to update: ").strip()

    for s in students:
        if s["roll_no"] == roll_no:
            name = input("Enter new name (press Enter to keep current): ").strip()
            course = input("Enter new course (press Enter to keep current): ").strip()
            email = input("Enter new email (press Enter to keep current): ").strip()

            if name:
                s["name"] = name

            if course:
                s["course"] = course

            if email:
                s["email"] = email

            save_students(students)
            print("Student record updated successfully.")
            return

    print("Student not found.")


def delete_student():
    students = load_students()

    roll_no = input("Enter roll number to delete: ").strip()

    updated = [s for s in students if s["roll_no"] != roll_no]

    if len(updated) == len(students):
        print("Student not found.")
    else:
        save_students(updated)
        print("Student record deleted successfully.")


def main():
    ensure_file()

    while True:
        print("\n===== STUDENT DATA MANAGER =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting Student Data Manager.")
            break
        else:
            print("Invalid choice. Enter 1 to 6.")


if __name__ == "__main__":
    main()

# LAB EXERCISE 13: CSV-BASED PAYROLL MANAGEMENT SYSTEM
import csv

INPUT_FILE = "employees.csv"
OUTPUT_FILE = "payroll_summary.csv"

# Payroll assumptions:
# Gross salary = Basic + HRA + Allowance
# PF deduction = 12% of Basic salary
# Tax deduction = 5% of Gross salary
# Net salary = Gross salary - PF - Tax


def process_payroll():
    total_gross = 0.0
    total_deductions = 0.0
    total_net = 0.0
    employee_count = 0

    try:
        with open(INPUT_FILE, "r", newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)

            required = {"emp_id", "name", "basic", "hra", "allowance"}

            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                print("CSV file is missing required columns:", required)
                return

            with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
                fields = [
                    "emp_id", "name", "gross", "pf", "tax",
                    "total_deductions", "net_salary"
                ]

                writer = csv.DictWriter(outfile, fieldnames=fields)
                writer.writeheader()

                for row in reader:
                    try:
                        basic = float(row["basic"])
                        hra = float(row["hra"])
                        allowance = float(row["allowance"])

                        if min(basic, hra, allowance) < 0:
                            print("Skipping", row["emp_id"],
                                  "- salary values cannot be negative.")
                            continue

                        gross = basic + hra + allowance
                        pf = basic * 0.12
                        tax = gross * 0.05
                        deductions = pf + tax
                        net = gross - deductions

                        writer.writerow({
                            "emp_id": row["emp_id"],
                            "name": row["name"],
                            "gross": f"{gross:.2f}",
                            "pf": f"{pf:.2f}",
                            "tax": f"{tax:.2f}",
                            "total_deductions": f"{deductions:.2f}",
                            "net_salary": f"{net:.2f}"
                        })

                        total_gross += gross
                        total_deductions += deductions
                        total_net += net
                        employee_count += 1

                    except (ValueError, TypeError):
                        print("Skipping invalid salary record for employee:",
                              row.get("emp_id", "Unknown"))

        if employee_count == 0:
            print("No valid employee records were processed.")
            return

        print("\nPAYROLL SUMMARY")
        print("-----------------------------------------------")
        print("Employees processed:", employee_count)
        print(f"Total gross salary: Rs. {total_gross:.2f}")
        print(f"Total deductions: Rs. {total_deductions:.2f}")
        print(f"Total net salary: Rs. {total_net:.2f}")
        print("Detailed report saved to", OUTPUT_FILE)

    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} was not found.")

    except PermissionError:
        print("Error: Permission denied while accessing payroll files.")

    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    process_payroll()