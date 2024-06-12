from transactions import TransactionManager

def display_menu():
    print("\nBanking System Menu:")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

def handle_choice(choice, transaction_manager):
    if choice == "1":
        account_id = input("Enter account ID: ")
        try:
            initial_balance = float(input("Enter initial balance: "))
            transaction_manager.create_account(account_id, initial_balance)
            print("Account created successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        account_id = input("Enter account ID: ")
        try:
            amount = float(input("Enter deposit amount: "))
            account = transaction_manager.get_account(account_id)
            account.deposit(amount)
            print("Deposit successful.")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "3":
        account_id = input("Enter account ID: ")
        try:
            amount = float(input("Enter withdrawal amount: "))
            account = transaction_manager.get_account(account_id)
            account.withdraw(amount)
            print("Withdrawal successful.")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "4":
        account_id = input("Enter account ID: ")
        try:
            account = transaction_manager.get_account(account_id)
            print(f"Account Balance: {account.get_balance()}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "5":
        print("Exiting the system.")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True
