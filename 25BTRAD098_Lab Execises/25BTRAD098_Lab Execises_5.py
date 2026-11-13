# LAB EXERCISE 14: BANK ACCOUNT SYSTEM USING OOP
class BankAccount:

    def __init__(self, account_holder, account_number, opening_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = 0.0  # Encapsulated private attribute

        if opening_balance >= 0:
            self.__balance = float(opening_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit. Amount must be greater than zero.")
        else:
            self.__balance += amount
            print(f"Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal. Amount must be greater than zero.")
        elif amount > self.__balance:
            print("Transaction failed. Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Available balance: Rs. {self.__balance:.2f}")

    def display_account(self):
        print("\nACCOUNT DETAILS")
        print("------------------------------")
        print("Account holder:", self.account_holder)
        print("Account number:", self.account_number)
        self.check_balance()


def main():
    print("===== BANK ACCOUNT SYSTEM =====")

    holder = input("Enter account holder name: ").strip()
    number = input("Enter account number: ").strip()

    try:
        opening = float(input("Enter opening balance: Rs. "))

        if opening < 0:
            print("Opening balance cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid opening balance.")
        return

    account = BankAccount(holder, number, opening)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance enquiry")
        print("4. Display account")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice in ("1", "2"):
            try:
                amount = float(input("Enter amount: Rs. "))

                if choice == "1":
                    account.deposit(amount)
                else:
                    account.withdraw(amount)

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.display_account()

        elif choice == "5":
            print("Thank you for using the Bank Account System.")
            break

        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    main()

    
# LAB EXERCISE 15: LIBRARY MANAGEMENT SYSTEM USING OOP
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print(f"{self.book_id:<10} {self.title:<25} "
              f"{self.author:<20} {status}")


class ReferenceBook(Book):
    # Inheritance: ReferenceBook reuses Book attributes and methods.

    def __init__(self, book_id, title, author, section):
        super().__init__(book_id, title, author)
        self.section = section

    def display(self):
        super().display()
        print(" Reference section:", self.section)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if any(existing.book_id == book.book_id for existing in self.books):
            print("A book with this ID already exists.")
        else:
            self.books.append(book)
            print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\nBOOK LIST")
        print("-" * 75)
        print(f"{'ID':<10} {'TITLE':<25} {'AUTHOR':<20} STATUS")
        print("-" * 75)

        for book in self.books:
            book.display()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return

        print("Book ID not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully.")
                else:
                    print("This book was not issued.")
                return

        print("Book ID not found.")


def main():
    library = Library()

    # Initial sample books
    library.add_book(Book("B101", "Python Basics", "A. Kumar"))
    library.add_book(Book("B102", "Data Structures", "R. Sharma"))
    library.add_book(ReferenceBook("R201", "Python Handbook",
                                   "M. Das", "Reference"))

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Display books")
        print("2. Issue book")
        print("3. Return book")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            library.display_books()

        elif choice == "2":
            book_id = input("Enter book ID to issue: ").strip()
            library.issue_book(book_id)

        elif choice == "3":
            book_id = input("Enter book ID to return: ").strip()
            library.return_book(book_id)

        elif choice == "4":
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Select 1 to 4.")


if __name__ == "__main__":
    main()
    
    
import random

def roll_dice(number_of_dice):
    results = []

    for _ in range(number_of_dice):
        results.append(random.randint(1, 6))

    return results


def main():
    print("===== DICE SIMULATOR =====")

    try:
        number_of_dice = int(input("How many dice do you want to roll? "))

        if number_of_dice <= 0:
            print("Enter a number greater than zero.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    frequency = {face: 0 for face in range(1, 7)}

    while True:
        choice = input("\nPress R to roll or Q to quit: ").strip().upper()

        if choice == "R":
            results = roll_dice(number_of_dice)

            print("Dice outcomes:", results)

            for face in results:
                frequency[face] += 1

            print("Total of this roll:", sum(results))

        elif choice == "Q":
            break

        else:
            print("Invalid choice. Press R or Q.")

    total_rolls = sum(frequency.values())

    print("\nFREQUENCY SUMMARY")
    print("-------------------------")

    for face, count in frequency.items():
        print(f"Face {face}: {count}")

    print("Total dice outcomes:", total_rolls)

    if total_rolls > 0:
        print("\nObserved percentages:")

        for face, count in frequency.items():
            percentage = (count / total_rolls) * 100
            print(f"Face {face}: {percentage:.2f}%")

    print("\nThank you for using Dice Simulator.")


if __name__ == "__main__":
    main()