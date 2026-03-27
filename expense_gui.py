import tkinter as tk
import json
import matplotlib.pyplot as plt

expenses = {}

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = {}

def add_expense():
    amount = entry_amount.get()
    category = entry_category.get()

    if not amount.isdigit():
        result_label.config(text="Enter valid amount!")
        return

    if category == "":
        result_label.config(text="Enter category!")
        return

    amount = int(amount)
    expenses[category] = expenses.get(category, 0) + amount
    save_expenses()

    result_label.config(text="Expense Added!")
    entry_amount.delete(0, tk.END)
    entry_category.delete(0, tk.END)
def show_pie_chart():
    if not expenses:
        result_label.config(text="No data to show!")
        return

    categories = list(expenses.keys())
    amounts = list(expenses.values())

    plt.figure()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

def view_expenses():
    text = ""
    total = 0

    for category, amount in expenses.items():
        text += f"{category}: {amount}\n"
        total += amount

    text += f"\nTotal: {total}"
    result_label.config(text=text)

def delete_expense():
    category = entry_category.get()

    if category in expenses:
        del expenses[category]
        save_expenses()
        result_label.config(text=f"{category} deleted!")
    else:
        result_label.config(text="Category not found!")

load_expenses()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")
root.configure(bg="#f5f5f5")

tk.Label(root, text="Expense Tracker", font=("Arial", 18)).pack(pady=10)

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Category").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=5)
tk.Button(root, text="Delete Expense", command=delete_expense).pack(pady=5)
tk.Button(root, text="Show Pie Chart", command=show_pie_chart).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()