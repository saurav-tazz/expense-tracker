import json
import math

FILENAME = "expenses.json"


def add_expense(expenses, amount, category, description=""):
    """Add one expense. Amount is in rupees, stored as integer paisa."""
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise ValueError("Expected a number.")
    if not math.isfinite(amount):
        raise ValueError("Amount must be a finite number.")

    paisa = round(amount * 100)
    if paisa <= 0:
        raise ValueError("Amount cannot be negative or zero")

    if not isinstance(category, str):
        raise ValueError("Category must be a valid string")

    category = category.strip().lower()
    if category == "":
        raise ValueError("Category cannot be empty")

    if not isinstance(description, str):
        raise ValueError("Description must be a valid string")
    description = description.strip()

    expenses.append({"amount": paisa, "category": category, "description": description})


def total_by_category(expenses):
    """Return {category: total in paisa}."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        totals[category] = totals.get(category, 0) + amount
    return totals


def format_rupees(paisa):
    if not isinstance(paisa, int) or isinstance(paisa, bool):
        raise ValueError("Expected an integer.")
    return f"Rs.{paisa / 100:.2f}"


def total_spent(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {format_rupees(expense['amount'])} | {expense['category']} | {expense['description']}")


def get_int(prompt, low, high):
    try:
        number = int(input(f"{prompt} ({low}-{high}): "))
    except ValueError:
        raise ValueError("Please enter a whole number.")
    if not low <= number <= high:
        raise ValueError(f"Select between {low} and {high}")
    return number


def load_expenses(filename=FILENAME):
    """Return the list from the file. Missing file -> []. Damaged file -> ValueError."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        return []
    if not isinstance(expenses, list):
        raise ValueError("File must contain a list of expenses.")
    return expenses


def save_expenses(expenses, filename=FILENAME):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)


def main(filename):
    try:
        expenses = load_expenses(filename)
    except ValueError:
        print(f"Error: {filename} is damaged and could not be read.\nFix the file or delete it, then run the program again.")
        return

    print("Expense Calculator")
    while True:
        print("\nMenu\n1. Add expense\n2. View expenses\n3. Total spent\n4. Total by category\n5. Quit")
        try:
            option = get_int("Enter option", 1, 5)
        except ValueError as e:
            print(e)
            continue

        if option == 1:
            try:
                amount = float(input("Enter amount in rupees: "))
            except ValueError:
                print("Amount must be a number.")
                continue
            category = input("Enter category: ")
            description = input("Enter description (optional): ")

            try:
                add_expense(expenses, amount, category, description)
            except ValueError as e:
                print(e)
                continue

            try:
                save_expenses(expenses, filename)
            except OSError as e:
                expenses.pop()
                print(f"Could not save, expense not added: {e}")
                continue

            print("Expense added.")
        elif option == 2:
            view_expenses(expenses)
        elif option == 3:
            print(format_rupees(total_spent(expenses)))
        elif option == 4:
            if not expenses:
                print("No expenses yet.")
            else:
                totals = total_by_category(expenses)
                for category, paisa in totals.items():
                    print(f"{category} | {format_rupees(paisa)}")
        elif option == 5:
            print("Thank you for using the Expense Calculator.")
            return


if __name__ == "__main__":
    main(FILENAME)