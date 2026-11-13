# ------------------------------------------------
# PROJECT: SALES DATA ANALYZER
# UNIT 3 - PROBLEM SOLVING COMPONENT
# LANGUAGE: PYTHON
# ------------------------------------------------

# List to store product details
products = []


# Function to add a new product
def add_product():
    print("\n--- ADD PRODUCT ---")

    name = input("Enter product name: ").strip()

    if not name:
        print("Product name cannot be empty!")
        return

    # Check whether product already exists
    for product in products:
        if product["name"].lower() == name.lower():
            print("Product already exists! Use Update Product.")
            return

    try:
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter price per unit: "))

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative!")
            return

        product = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        products.append(product)

        print("Product added successfully!")

    except ValueError:
        print("Invalid input! Enter valid numeric values.")


# Function to update product details
def update_product():
    print("\n--- UPDATE PRODUCT ---")

    name = input("Enter product name: ").strip()

    for product in products:

        if product["name"].lower() == name.lower():

            try:
                quantity = int(input("Enter new quantity sold: "))
                price = float(input("Enter new price per unit: "))

                if quantity < 0 or price < 0:
                    print("Values cannot be negative!")
                    return

                product["quantity"] = quantity
                product["price"] = price

                print("Product updated successfully!")
                return

            except ValueError:
                print("Invalid input!")

                return

    print("Product not found!")


# Function to display all products
def display_products():
    print("\n========== SALES RECORDS ==========")

    if not products:
        print("No product records available!")
        return

    print("-" * 65)

    print("{:<15} {:<12} {:<12} {:<15}".format(
        "Product",
        "Quantity",
        "Price",
        "Revenue"
    ))

    print("-" * 65)

    for product in products:

        revenue = product["quantity"] * product["price"]

        print("{:<15} {:<12} {:<12.2f} {:<15.2f}".format(
            product["name"],
            product["quantity"],
            product["price"],
            revenue
        ))

    print("-" * 65)


# Function to calculate total sales revenue
def calculate_total_sales():

    total = 0

    for product in products:

        revenue = product["quantity"] * product["price"]

        total += revenue

    print("\n========== TOTAL SALES ==========")

    print("Total Sales Revenue: Rs.", round(total, 2))


# Function to identify highest-selling product
def highest_selling_product():

    if not products:
        print("No product records available!")
        return

    highest = max(products, key=lambda p: p["quantity"])

    print("\n====== HIGHEST SELLING PRODUCT ======")

    print("Product Name:", highest["name"])

    print("Quantity Sold:", highest["quantity"])

    print("Revenue: Rs.", highest["quantity"] * highest["price"])


# Function to display product-wise performance
def product_performance():

    if not products:
        print("No product records available!")
        return

    print("\n======= PRODUCT PERFORMANCE =======")

    for product in products:

        revenue = product["quantity"] * product["price"]

        print("\nProduct:", product["name"])

        print("Quantity Sold:", product["quantity"])

        print("Price Per Unit: Rs.", product["price"])

        print("Total Revenue: Rs.", round(revenue, 2))

        print("-" * 35)


# Main menu
def main():

    while True:

        print("\n")
        print("====================================")
        print("       SALES DATA ANALYZER")
        print("====================================")

        print("1. Add Product")
        print("2. Update Product")
        print("3. Display Sales Records")
        print("4. Calculate Total Sales")
        print("5. Highest Selling Product")
        print("6. Product Performance")
        print("7. Exit")

        print("====================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":

            add_product()

        elif choice == "2":

            update_product()

        elif choice == "3":

            display_products()

        elif choice == "4":

            calculate_total_sales()

        elif choice == "5":

            highest_selling_product()

        elif choice == "6":

            product_performance()

        elif choice == "7":

            print("\nThank you for using Sales Data Analyzer!")

            print("Program terminated successfully.")

            break

        else:

            print("Invalid choice! Please select between 1 and 7.")


# Program execution
if __name__ == "__main__":

    main()
