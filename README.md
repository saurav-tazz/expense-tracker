# Expense Calculator

A command-line expense tracker written in Python. Add expenses, view them, see totals, and keep your data between runs in a JSON file.

## Features

- Add an expense with an amount (in rupees), a category and an optional description
- View all expenses as a numbered list
- See the total spent
- See totals grouped by category
- Data is saved to `expenses.json` after every successful add and loaded on start
- Input validation with clear error messages (nothing crashes on bad input)

## Requirements

- Python 3.8 or newer
- No third-party packages

## Run it

```
git clone https://github.com/saurav-tazz/<repo-name>.git
cd <repo-name>
python expenses.py
```

## Menu

```
1. Add expense
2. View expenses
3. Total spent
4. Total by category
5. Quit
```

Example session:

```
Enter option (1-5): 1
Enter amount in rupees: 12.50
Enter category: Food
Enter description (optional): lunch
Expense added.

Enter option (1-5): 2
1. Rs.12.50 | food | lunch
```

## How it works

### Money is stored as integer paisa

Floats can't store most decimals exactly (`0.1 + 0.2` gives `0.30000000000000004`), so sums of money would drift. Every amount is converted to whole paisa when it is added, and converted back to rupees only when it is displayed.

```
Rs 12.50  ->  stored as 1250  ->  shown as Rs.12.50
```

`format_rupees` is the only function that divides by 100.

### Data format

Expenses are stored in `expenses.json` as a list of dictionaries:

```json
[
  {
    "amount": 1250,
    "category": "food",
    "description": "lunch"
  }
]
```

Categories are stripped and lowercased, so `"Food"` and `"food "` count as the same category.

### Validation

`add_expense` rejects:

- amounts that aren't numbers (including `True`/`False`)
- `inf` and `nan`
- amounts that are zero or negative, or that round to zero paisa (like `0.004`)
- categories that aren't strings or are empty after stripping
- descriptions that aren't strings

Each rejection raises a `ValueError` with a clear message, and nothing is added to the list.

### Files and errors

- If `expenses.json` doesn't exist, the program starts with an empty list.
- If the file is damaged, or doesn't contain a list, the program prints an error and stops **without overwriting the file**.
- If saving fails, the expense is removed from memory so the list and the file stay in sync.

## Project structure

```
expense_calculator/
├── expenses.py        # all functions and the menu
├── test_expenses.py   # manual test script
├── expenses.json      # created on first add (not in git)
├── .gitignore
└── README.md
```

### Functions

| Function | What it does |
|---|---|
| `add_expense(expenses, amount, category, description)` | Validates input and appends an expense. Prints nothing. |
| `total_by_category(expenses)` | Returns `{category: total in paisa}`. |
| `total_spent(expenses)` | Returns the sum of all amounts in paisa. |
| `format_rupees(paisa)` | Returns a string like `Rs.12.50`. |
| `view_expenses(expenses)` | Prints the numbered list. |
| `get_int(prompt, low, high)` | Reads a whole number in a range, or raises `ValueError`. |
| `load_expenses(filename)` | Reads the JSON file. Missing file gives `[]`. |
| `save_expenses(expenses, filename)` | Writes the list to the JSON file. |
| `main(filename)` | Runs the menu loop. |

## Testing

`test_expenses.py` imports the functions and calls them with good and bad input. Run it from the project folder:

```
python test_expenses.py
```

## What I learned

- Why money should be stored as integers
- Grouping with a dictionary and `.get(key, 0)`
- Validating input in one place and catching errors where they can be shown to the user
- Reading and writing JSON, and handling missing and damaged files
- Keeping functions that return separate from functions that print

## Possible improvements

- Delete or edit an expense
- Filter by date or category
- Add a date to each expense
- Check every item when loading the file
- Turn it into a FastAPI backend with a database