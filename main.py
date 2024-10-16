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
        print(f"Expense of {amount} added to {category}")
    except ValueError as e:
        print("Invalid input", e)


def income_func():
    global income_bal
    try:
        income_amt = float(input("Enter the amount of income: "))
        income_bal += income_amt
        print(f"Income of {income_amt} added successfully!")
        print(f"New income balance is {income_bal}")
    except ValueError as e:
        print("Invalid input", e)


while True:
    print("----- Personal Budget Tracker -----")
    print("1. Add income")
    print("2. Add expense")
    print("3. View summary")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")
    if len(choice) == 0:
        raise Exception("input cannot be empty")

    if int(choice) == 4:
        exit_program()
        break
    elif int(choice) == 2:
        expense_func()
    elif int(choice) == 1:
        income_func()
    elif int(choice) == 3:
        summary()
    else:
        print("Invalid choice, select a valid option")
