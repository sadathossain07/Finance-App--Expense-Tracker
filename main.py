# Expense Tracker Project

expenses_list = []  # each expense is stored as a dictionary


# ---------- Helper functions ----------

def get_number(message, number_type=float):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return number_type(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu():
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")


# ---------- Feature functions ----------

def add_expense():
    date = input("On what date was the expense incurred? ")
    category = input("What kind of expense? (Food, Travel, Makeup, Books): ")
    description = input("Provide more details: ")
    amount = get_number("Enter the amount: ")

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }

    expenses_list.append(expense)
    print("\nDONE Sir. Expense is added successfully.")


def view_expenses():
    if len(expenses_list) == 0:
        print("No expenses added. Please add some expenses first.")
        return

    print("\n===== Your Expenses =====")
    for number, expense in enumerate(expenses_list, start=1):
        print(
            f"Expense Number {number} -> "
            f"{expense['date']}, {expense['category']}, "
            f"{expense['description']}, {expense['amount']:.2f}"
        )


def view_total():
    total = sum(expense["amount"] for expense in expenses_list)
    print(f"\nTOTAL EXPENSE = {total:.2f}")


# ---------- Main program ----------

def main():
    print("Welcome to Expense Tracker:")

    while True:
        show_menu()
        choice = get_number("Please enter your choice: ", int)

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            view_total()
        elif choice == 4:
            print("Thank you for using Expense Tracker. Have a nice day!")
            break
        else:
            print("INVALID CHOICE. TRY AGAIN.")


main()