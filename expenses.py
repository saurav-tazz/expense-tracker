import math

def add_expense(expenses, amount, category, description = ""):
    """code to add expense"""
    if not isinstance(amount, (int, float)) or isinstance(amount, bool) :
        raise ValueError("Expected a number.\n")
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
    
    if not isinstance(description, str) or description is None:
            raise ValueError("Description must be a valid string")
    description = description.strip()

    expenses.append({"amount": paisa, "category": category, "description": description})

def total_by_category(expenses):
    """code to calculate total by category"""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        totals[category] = totals.get(category, 0) + amount

    return totals

def format_rupees(paisa):
    if not isinstance(paisa, int) or isinstance(paisa, bool):
        raise ValueError("Expected an integer.")
    return f"Rs.{paisa/100:.2f}"

def total_spent(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, expense in enumerate(expenses, start = 1):
        print(f"{i}. {format_rupees(expense['amount'])} | {expense['category']} | {expense['description']}")

def get_int(prompt, low, high):
    try:
        number = int(input(f"{prompt} ({low}-{high}): "))
    except ValueError:
        raise ValueError("Please enter a whole number.")
    if not low <= number <= high:
        raise ValueError(f"Select between {low} and {high}")
    return number

def main():
    expenses = []
    print("Expense Calculcator")
    while True:
        print("\nMenu\n1. Add expense\n2. View expense\n3. Total spent\n4. Total by category\n5. Quit")
        try:
            option = get_int("Enter Option", 1, 5)
        except ValueError as e:
            print(e)
            continue

        if option == 1:
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Amount must be a number")
                continue
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            try:
                add_expense(expenses, amount, category, description)
                print("Expense added")
            except ValueError as e:
                print(e)
        elif option == 2:
            view_expenses(expenses)
        elif option == 3:
            print(format_rupees(total_spent(expenses)))
        elif option == 4:
            if not expenses:
                print("No expenses yet")
            else:
                totals = total_by_category(expenses)
                for category, amount in totals.items():
                    print(f"{category} | {format_rupees(amount)}")
        elif option == 5:
            print("Thank You for using.")
            return
if __name__ == "__main__":
    main()
        
        
