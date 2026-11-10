def add_expense(expenses, amount, category, description = ""):
    """code to add expense"""
    if not isinstance(amount, (int, float)) or isinstance(amount, bool) :
        raise ValueError("Expected a number.\n")
    
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
    if paisa == "":
        raise ValueError("Paisa cannot be empty")
    elif not isinstance(paisa, int) or isinstance(paisa, bool):
        raise ValueError("Expected an integer.")
    elif paisa <=0:
        raise ValueError("Paisa cannot be negative or 0")

    rupees = f"Rs.{paisa/100:.2f}"
    return rupees

def total_spent(expenses):
    amount = 0
    if not expenses:
        return amount
    for expense in expenses:
        amount += expense["amount"]*100
    return amount

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
    else:
        for i, expense in enumerate(expenses, start = 1):
            print(f"{i}. Rs.{format_rupees(expense["amount"])} | {expense["category"]} | {expense["description"]}")



expenses = []

try:
    add_expense(expenses, 1000, "Food", "Saturday Dinner")
except ValueError as e:
    print(e)

try:
    add_expense(expenses, 0.015, "misc")
except ValueError as e:
    print(e)

# bad amount
try:
    add_expense(expenses, 0, "Miscellanous", "Football boots")
except ValueError as e:
    print(e)

try:
    add_expense(expenses, -5, "Miscellanous", "Football boots")
except ValueError as e:
    print(e)

try:
    add_expense(expenses, "abc", "Miscellanous", "Football boots")
except ValueError as e:
    print(e)

try:
    add_expense(expenses, True, "Miscellanous", "Football boots")
except ValueError as e:
    print(e)

try:
    add_expense(expenses, 0.004, "Miscellanous", "Football boots")
except ValueError as e:
    print(e)

# bad category
try:
    add_expense(expenses, 1000, "    ", "Football boots")
except ValueError as e:
    print(e)

try:
    add_expense(expenses, 1000, 5, "Football boots")
except ValueError as e:
    print(e)

# bad description
try:
    add_expense(expenses, 1000, "Miscellanous", None)
except ValueError as e:
    print(e)

print(len(expenses))

for expense in expenses:
    print(f'Rs.{expense["amount"]/100:.2f} : {expense["category"]} : {expense["description"]}')

for category, paisa in total_by_category(expenses).items():
    print(f"{category} : Rs.{paisa/100:.2f}")

print("*"*20)
try:
    paisa = True
    print(format_rupees(paisa))
except ValueError as e:
    print(e)