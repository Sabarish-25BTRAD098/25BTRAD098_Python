#Lab Exercise 8: Contact Book Using Lists and Dictionaries
contacts = []

# Each contact is stored as a dictionary inside this list.

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    for contact in contacts:
        if contact["phone"] == phone:
            print("A contact with this phone number already exists.")
            return

    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully.")


def search_contact():
    keyword = input("Enter name or phone to search: ").strip().lower()

    for contact in contacts:
        if (keyword in contact["name"].lower()
                or keyword in contact["phone"].lower()):
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("Contact not found.")


def update_contact():
    phone = input("Enter the phone number of the contact to update: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            new_name = input("Enter new name: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email: ").strip()

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact():
    phone = input("Enter phone number of contact to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")


def display_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n{:<18} {:<16} {}".format("NAME", "PHONE", "EMAIL"))
    print("-" * 58)

    for contact in contacts:
        print("{:<18} {:<16} {}".format(
            contact["name"], contact["phone"], contact["email"]
        ))


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Display contacts")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()

# LAB EXERCISE 9: STUDENT GRADING SYSTEM
students = {}

# Key: student name, Value: marks

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        students[name] = marks
        print("Student record saved successfully.")

    except ValueError:
        print("Please enter marks as a number.")


def display_results():
    if not students:
        print("No student records available.")
        return

    print("\n{:<20} {:<12} {}".format("STUDENT", "MARKS", "GRADE"))
    print("-" * 42)

    for name, marks in students.items():
        grade = calculate_grade(marks)
        print("{:<20} {:<12.1f} {}".format(name, marks, grade))


def show_class_summary():
    if not students:
        print("No student records available.")
        return

    average = sum(students.values()) / len(students)
    passed = sum(1 for mark in students.values() if mark >= 50)
    failed = len(students) - passed

    print("\nClass average:", round(average, 2))
    print("Students passed:", passed)
    print("Students failed:", failed)


def main():
    while True:
        print("\n===== STUDENT GRADING SYSTEM =====")
        print("1. Add or update student marks")
        print("2. Display student results")
        print("3. Display class summary")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_results()
        elif choice == "3":
            show_class_summary()
        elif choice == "4":
            print("Exiting Student Grading System.")
            break
        else:
            print("Invalid choice. Please enter 1 to 4.")


if __name__ == "__main__":
    main()

# LAB EXERCISE 10: FREQUENCY COUNTER USING DICTIONARIES
def count_word_frequency():
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Please enter a sentence.")
        return

    # Convert to lowercase and remove common punctuation.
    cleaned = sentence.lower()

    for symbol in ".,!?;:\"()[]{}":
        cleaned = cleaned.replace(symbol, "")

    words = cleaned.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\nWORD FREQUENCY")
    print("-" * 28)

    for word, count in sorted(frequency.items()):
        print("{:<18} {}".format(word, count))

    most_common = max(frequency, key=frequency.get)

    print("\nMost frequent word:", most_common)
    print("Occurrences:", frequency[most_common])


def count_list_frequency():
    raw_items = input("Enter list items separated by commas: ").strip()

    if not raw_items:
        print("Please enter at least one item.")
        return

    items = [item.strip() for item in raw_items.split(",") if item.strip()]
    frequency = {}

    for item in items:
        frequency[item] = frequency.get(item, 0) + 1

    print("\nELEMENT FREQUENCY")
    print("-" * 28)

    for item, count in sorted(frequency.items()):
        print("{:<18} {}".format(item, count))


def main():
    while True:
        print("\n===== FREQUENCY COUNTER =====")
        print("1. Count words in a sentence")
        print("2. Count occurrences in a list")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            count_word_frequency()
        elif choice == "2":
            count_list_frequency()
        elif choice == "3":
            print("Exiting Frequency Counter.")
            break
        else:
            print("Invalid choice. Please enter 1 to 3.")


if __name__ == "__main__":
    main()