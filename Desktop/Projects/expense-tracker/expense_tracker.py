import argparse
import json
import os
from datetime import datetime
import sys

EXPENSE_FILES= "expenses.json"

# load existing expenses or start empty

def load_expenses():
    if os.path.exists(EXPENSE_FILES):
        with open(EXPENSE_FILES, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # file exists but is empty or broken
    return []


def save_expenses(expenses):
    with open(EXPENSE_FILES, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(description, amount):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    new_expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

def show_expenses():
    expenses = load_expenses()
    if not expenses:
        print("no expenses found")
        return
    

    print("\nSaved Expenses:")
    for exp in expenses:
        print(f"ID: {exp['id']} | Description: {exp['description']} | Cost: {exp['amount']}")

def clear_expenses():
    save_expenses([])
    # overwrite old file with new empty file

    print("all expenses have been removed")

def remove_expense(expense_id):
    expenses = load_expenses()
    new_expenses = [exp for exp in expenses if exp['id'] != expense_id]

    if len(expenses) == len(new_expenses):
        print(f"no expense with ID: {expense_id} found")
    else:
        save_expenses(new_expenses)
        print(f"Item ID {expense_id} removed successfully")


def main():
    '''
    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True, help="Description of expense:")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")

    # show command
    subparsers.add_parser("show")

    # clear command
    subparsers.add_parser("clear")

    # remove command
    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("--id", type=int, required=True, help="id of the expense")

    # Reads command line input and stores it in args
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "show":
        show_expenses()
    elif args.command == "clear":
        clear_expenses()
    elif args.command == "remove":
        remove_expense(args.id)
    else:
        print("Unknown command")


if __name__ == "__main__":

    main()
    '''

    if len(sys.argv) < 2:
        print("please add a command")
        sys.exit()

    command = sys.argv[1]

    if command == "add":
        description = sys.argv[2]
        amount = float(sys.argv[3])
        add_expense(description, amount)
    elif command == "clear":
        clear_expenses()
    elif command == "remove":
        id = int(sys.argv[2])
        remove_expense(id)
    elif command == "show":
        show_expenses()
    else:
        print("unknown command")
    
if __name__ == "__main__":

    main()