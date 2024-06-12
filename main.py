from menu import display_menu, handle_choice
from transactions import TransactionManager

def main():
    transaction_manager = TransactionManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if not handle_choice(choice, transaction_manager):
            break

if __name__ == "__main__":
    main()
