from db import create_tables, add_transaction, get_transactions, set_budget, get_budget

def main():
    create_tables()
    
    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Set Budget")
        print("4. View Budget")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            description = input("Description: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            add_transaction(description, amount, date)
            print("Transaction added.")
        
        elif choice == '2':
            transactions = get_transactions()
            for t in transactions:
                print(f"ID: {t[0]}, Description: {t[1]}, Amount: {t[2]}, Date: {t[3]}")
        
        elif choice == '3':
            total = float(input("Total Budget: "))
            spent = float(input("Spent Amount: "))
            set_budget(total, spent)
            print("Budget set.")
        
        elif choice == '4':
            budget = get_budget()
            if budget:
                print(f"Total Budget: {budget[1]}, Spent: {budget[2]}")
            else:
                print("No budget set.")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
