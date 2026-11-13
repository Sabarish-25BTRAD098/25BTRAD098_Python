import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class BillGeneratorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("SuperMarket Bill Generator")
        self.root.geometry("450x550")

        # Shopping Cart list
        self.cart = []

        self.setup_ui()

    def setup_ui(self):
        # --- Input Section ---
        input_frame = tk.Frame(self.root, pady=10)
        input_frame.pack()

        tk.Label(input_frame, text="Item Name:",
                 font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)

        self.name_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(input_frame, text="Price ($):",
                 font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)

        self.price_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.price_var).grid(row=1, column=1)

        tk.Label(input_frame, text="Quantity:",
                 font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5)

        self.qty_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.qty_var).grid(row=2, column=1)

        # Add Item Button
        tk.Button(
            input_frame,
            text="Add to Cart",
            bg="#4CAF50",
            fg="white",
            command=self.add_item
        ).grid(row=3, column=0, columnspan=2, pady=10, sticky="we")

        # --- Receipt Display Section ---
        self.receipt_text = tk.Text(
            self.root,
            height=18,
            width=50,
            font=("Courier", 10)
        )

        self.receipt_text.pack(padx=10, pady=5)
        self.receipt_text.insert(tk.END, "Cart is empty. Add items above.\n")

        # --- Action Buttons ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Generate Final Bill",
            bg="#2196F3",
            fg="white",
            command=self.generate_bill,
            width=18
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="Clear All",
            bg="#f44336",
            fg="white",
            command=self.clear_all,
            width=18
        ).grid(row=0, column=1, padx=5)

    def add_item(self):
        name = self.name_var.get().strip()

        try:
            # Validate inputs
            if not name:
                raise ValueError("Name cannot be empty")

            price = float(self.price_var.get())
            qty = int(self.qty_var.get())

            if price < 0 or qty <= 0:
                raise ValueError("Invalid price or quantity")

            # Calculate item total and add to cart
            total_price = price * qty

            self.cart.append({
                "name": name,
                "price": price,
                "qty": qty,
                "total": total_price
            })

            # Show brief confirmation in the text box
            if len(self.cart) == 1:
                self.receipt_text.delete(1.0, tk.END)

            self.receipt_text.insert(
                tk.END,
                f"+ Added: {name} (x{qty})\n"
            )

            # Clear input fields for the next item
            self.name_var.set("")
            self.price_var.set("")
            self.qty_var.set("")

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter a valid Name, numeric Price, and whole Quantity."
            )

    def generate_bill(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "No items to bill!")
            return

        self.receipt_text.delete(1.0, tk.END)

        # Print Header
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.receipt_text.insert(tk.END, f"{'='*45}\n")
        self.receipt_text.insert(tk.END, f"{'SUPERMARKET RECEIPT':^45}\n")
        self.receipt_text.insert(tk.END, f"{date_str:^45}\n")
        self.receipt_text.insert(tk.END, f"{'='*45}\n")

        self.receipt_text.insert(
            tk.END,
            f"{'ITEM':<20}{'QTY':<6}{'PRICE':<9}{'TOTAL':<10}\n"
        )

        self.receipt_text.insert(tk.END, f"{'-'*45}\n")

        # Print Items
        subtotal = 0

        for item in self.cart:
            self.receipt_text.insert(
                tk.END,
                f"{item['name'][:18]:<20}"
                f"{item['qty']:<6}"
                f"${item['price']:<8.2f}"
                f"${item['total']:<9.2f}\n"
            )

            subtotal += item['total']

        # Print Totals
        tax = subtotal * 0.07
        grand_total = subtotal + tax

        self.receipt_text.insert(tk.END, f"{'-'*45}\n")
        self.receipt_text.insert(
            tk.END,
            f"{'Subtotal:':<35}${subtotal:.2f}\n"
        )

        self.receipt_text.insert(
            tk.END,
            f"{'Tax (7%):':<35}${tax:.2f}\n"
        )

        self.receipt_text.insert(tk.END, f"{'='*45}\n")

        self.receipt_text.insert(
            tk.END,
            f"{'GRAND TOTAL:':<35}${grand_total:.2f}\n"
        )

        self.receipt_text.insert(tk.END, f"{'='*45}\n")

    def clear_all(self):
        self.cart.clear()

        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(
            tk.END,
            "Cart is empty. Add items above.\n"
        )

        self.name_var.set("")
        self.price_var.set("")
        self.qty_var.set("")


if __name__ == "__main__":

    # Create the main window and pass it to our app
    root = tk.Tk()

    app = BillGeneratorApp(root)

    # Start the GUI event loop
    root.mainloop()