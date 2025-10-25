class BankAccount:
    """A class to represent a bank account."""

    def __init__(self, account_number: str, account_holder: str, balance: float, account_type: str):
        """Initializes a new BankAccount object."""
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__account_type = account_type

    def get_account_number(self) -> str:
        """Returns the account number."""
        return self.__account_number

    def get_account_holder(self) -> str:
        """Returns the account holder."""
        return self.__account_holder

    def get_balance(self) -> float:
        """Returns the account balance."""
        return self.__balance

    def get_account_type(self) -> str:
        """Returns the account type."""
        return self.__account_type

    def deposit(self, amount: float):
        """Deposits a given amount to the account."""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        """Withdraws a given amount from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount.")

    def __str__(self) -> str:
        """Returns a string representation of the BankAccount object."""
        return f"Account Holder: {self.__account_holder}, Account Type: {self.__account_type}, Balance: ${self.__balance:.2f}"


if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("23066598", "Chimobi Eze ", 1000.0, "Savings")

    # Print account details
    print(account)

    # Deposit money
    account.deposit(500.0)
    print(f"Balance after deposit: £{account.get_balance():.2f}")

    # Withdraw money
    account.withdraw(200.0)
    print(f"Balance after withdrawal: £{account.get_balance():.2f}")

    # Try to withdraw an invalid amount
    try:
        account.withdraw(2000.0)
    except ValueError as e:
        print(f"Error: {e}")

    # Try to deposit a negative amount
    try:
        account.deposit(-100.0)
    except ValueError as e:
        print(f"Error: {e}")
