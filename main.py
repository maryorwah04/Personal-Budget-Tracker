print("----- Personal Budget Tracker -----")
print("1. Add income")
print("2. Add expense")
print("3. View summary")
print("4. Exit")

choice = int(input("Enter your choice(1-4): "))

def exit():
    print("Exiting the program... Goodbye!")

if choice == 4:
    exit()
else:
    print("Continue")