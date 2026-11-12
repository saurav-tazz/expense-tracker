from expenses import add_expense, total_by_category, format_rupees, total_spent, view_expenses


expenses = [
    {"amount": 100000, "category": "food", "description": "Saturday Dinner"},
    {"amount": 12500, "category": "college", "description": "printing"},
    {"amount": 4000, "category": "travel", "description": ""},
    ]


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

# empty list
# empty list
empty = []
view_expenses(empty)
print(total_spent(empty))
print(format_rupees(total_spent(empty)))

# three expenses
sample = [
    {"amount": 1000, "category": "food", "description": "khana"},
    {"amount": 1500, "category": "sports", "description": "futsal boots"},
    {"amount": 1000, "category": "clothes", "description": "tshirt + pants"},
]
view_expenses(sample)
print(total_spent(sample))
print(format_rupees(total_spent(sample)))

# bad input to format_rupees
for bad in (True, "abc", 12.5, [1, 2]):
    try:
        format_rupees(bad)
    except ValueError as e:
        print(f"{bad!r}: {e}")

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