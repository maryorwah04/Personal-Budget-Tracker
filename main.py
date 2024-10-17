expenses = {}
income_bal = 0.0
 
def exit_program():
    print("Exiting the program... Goodbye!")
  
def expense_func():
    category = input("Enter the expense category (e.g groceries or rent): ")
    amount = input(f"Enter the amount for {category}: ")
    try:
        amount = float(amount)
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        print(f"Expense of {amount:.1f} added to {category}")
    except ValueError as e:
        print("Invalid input", e)


def income_func():
    global income_bal
    try:
        income_amt = float(input("Enter the amount of income: "))
        income_bal += income_amt
        print(f"Income of {income_amt:.1f} added successfully!")
        print(f"New income balance is {income_bal:.1f}")
    except ValueError as e:
        print("Invalid input", e)

def summary():
    total_expenses = sum(expenses.values())
    overspent = total_expenses - income_bal
    print("---- Budget Summary ----")
    print(f"Total income: {income_bal:.1f}")
    print(f"Total expenses: {total_expenses:.1f}")
    print("--- expense categories ---")
    for category, amount in expenses.items():
        print(f"{category}: {amount:.1f}")
    if total_expenses > income_bal:
        print(f"You've overspent by {overspent:.1f}")


while True:
    print("----- Personal Budget Tracker -----")
    print("1. Add income")
    print("2. Add expense")
    print("3. View summary")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > 4:
        print("Invalid input! Please enter a valid number between 1 and 4.")
        continue 

    if int(choice) == 4:
        exit_program()
        break
    elif int(choice) == 2:
        expense_func()
    elif int(choice) == 1:
        income_func()
    elif int(choice) == 3:
        summary()
