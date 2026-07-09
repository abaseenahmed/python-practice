#================================== Expense Tracker App ========================================

#---------- Header Formatter -----------
def print_header(title):
    """Helper function to print formatted headers"""
    print("\n" + "="*50)
    print(title.center(50))
    print("="*50)

expenses = []

#----------- 1. ADD EXPENSE -------------
def add_expense():
    print_header("1. ADD EXPENSE")
    
    # Validate category
    while True:
        category = input("Enter Category: ").strip()
        if not category:
            print("❌ Please enter a valid category.")
            continue
        if not all(c.isalpha() or c in " .'-" for c in category):
            print("❌ Category should contain only letters, spaces, dots, and hyphens!")
            continue
        break
    
    # Validate amount
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Invalid amount! Please enter a valid number.")
    
    # Validate description
    while True:
        description = input("Enter Description: ").strip()
        if not description:
            print("❌ Please enter a valid description.")
            continue
        break
    
    # Create and add expense
    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print(f"✅ Expense added successfully! Amount: ${amount:.2f}")

#------------ VIEW EXPENSES -------------
def view_expense():
    print_header("2. VIEW EXPENSES")
    if not expenses:
        print("❌ No expenses found.")
        return
    
    expense_count = 0
    for expense in expenses:
        expense_count += 1
        print("-"*30)
        print(f"Expense #{expense_count}")
        print("-"*30)
        print(f"Category    : {expense['category']}")
        print(f"Amount      : ${expense['amount']:.2f}")
        print(f"Description : {expense['description']}")
        print()
    
    print("-"*30)
    print(f"Total Records: {expense_count}")
    print("-"*30)

#------------ TOTAL EXPENSE -------------
def total_expense():
    print_header("3. TOTAL EXPENSE")
    if not expenses:
        print("❌ No expenses found.")
        return
    
    total = 0
    for expense in expenses:
        total += expense["amount"]
    
    print("-"*30)
    print(f"Total Expenses: ${total:.2f}")
    print("-"*30)

#------------ SEARCH EXPENSE -------------
def search_expense():
    print_header("4. SEARCH EXPENSE")
    
    if not expenses:
        print("❌ No expenses found to search.")
        return
    
    # Get search category
    while True:
        search_category = input("Enter Category to Search: ").strip()
        if not search_category:
            print("❌ Please enter a valid search category.")
            continue
        break
    
    # Search for matching expenses
    found_expenses = []
    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            found_expenses.append(expense)
    
    # Display results
    if not found_expenses:
        print(f"❌ No expenses found with category: '{search_category}'")
        return
    
    print(f"\n✅ Found {len(found_expenses)} expense(s) with category: '{search_category}'")
    print("-"*30)
    
    search_count = 0
    total_amount = 0
    for expense in found_expenses:
        search_count += 1
        total_amount += expense["amount"]
        print(f"Expense #{search_count}")
        print("-"*30)
        print(f"Category    : {expense['category']}")
        print(f"Amount      : ${expense['amount']:.2f}")
        print(f"Description : {expense['description']}")
        print()
    
    print("-"*30)
    print(f"Total Records: {search_count}")
    print(f"Total Amount : ${total_amount:.2f}")
    print("-"*30)

#----------- DISPLAY MENU ---------------
def display_menu():
    """Display main menu"""
    print_header("EXPENSE TRACKER SYSTEM")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Search Expense")
    print("5. Exit")
    print("="*50)

#------------- MAIN RUN PROGRAM ----------
def run():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("Enter Choice (1-5): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            search_expense()
        elif choice == '5':
            print_header("Thank you for using the Expense Tracker!")
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5")
        
        input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    run()