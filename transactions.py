from account import Account

class TransactionManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, initial_balance=0.0):
        if account_id in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[account_id] = Account(account_id, initial_balance)

    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_id]
