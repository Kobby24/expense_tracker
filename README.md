
# Expense Tracker

A simple command-line application for managing and tracking your daily expenses. It allows users to add, list, summarize, delete, and update expense records. All records are stored in a CSV file for easy management.

## Features
- Add a new expense with a description and amount.
- View a list of all expenses.
- Summarize total expenses for a specific month or overall.
- Delete an expense by its ID.
- Update existing expense records.

## Requirements
- Python 3.x
- `argparse` (built-in)
- `csv` (built-in)
- `datetime` (built-in)
- `calendar` (built-in)

## How to Use

### 1. Add an Expense
To add a new expense, provide a description and an amount:
```bash
python expense_tracker.py add --description "Lunch" --amount 15.50
```
This will add a new expense to the `data.csv` file with the current date.

### 2. List All Expenses
To view all recorded expenses:
```bash
python expense_tracker.py list
```
This will display a table with the following columns:
- `ID`: Unique identifier for each record.
- `Date`: The date of the expense.
- `Description`: A short description of the expense.
- `Amount`: The expense amount in USD.

### 3. Summarize Expenses
To see the total expenses:
```bash
python expense_tracker.py summary
```

To summarize expenses for a specific month:
```bash
python expense_tracker.py summary --month 8
```
This will display the total expenses for the specified month (e.g., August).

### 4. Delete an Expense
To delete an expense by its ID:
```bash
python expense_tracker.py delete --id 2
```
This removes the record with ID 2 from the `data.csv` file.

### 5. Update an Expense
(To be implemented.)

## Example Output
### Adding an Expense:
```bash
python expense_tracker.py add --description "Groceries" --amount 45.75
Added Groceries for 45.75
```

### Listing Expenses:
```bash
python expense_tracker.py list
ID    Date         Description   Amount
1     2024-12-01   Lunch         $15.50
2     2024-12-02   Groceries     $45.75
```

### Summarizing Expenses:
```bash
python expense_tracker.py summary
Total expenses: $61.25
```

### Deleting an Expense:
```bash
python expense_tracker.py delete --id 1
Expense with ID 1 has been deleted.
```

## File Structure
- **`expense_tracker.py`**: The main script for managing expenses.
- **`data.csv`**: The file where all expense records are stored.

## Notes
- If the `data.csv` file doesn't exist, it will be created automatically when you add the first record.
- Only positive expense amounts are allowed.

## Future Enhancements
- Implement the `update` functionality to modify existing records.
- Add support for categorizing expenses.
- Provide better error handling for invalid inputs.

## Author 
Kobby24

## Project Link
https://roadmap.sh/projects/expense-tracker
