class Customer:
    def __init__(self, user_info: dict):
        self.name = user_info.get("name")
        self.age = user_info.get("age")
        self.contact_no = user_info.get("contact_no")

        if not all([self.name, self.age, self.contact_no]):
            raise ValueError("Incomplete customer information")


class BankAccount(Customer):
    def __init__(self, user_info: dict):
        super().__init__(user_info)
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nContact: {self.contact_no}\nBalance: {self.balance:.2f}"


class DebitAccount(BankAccount):
    def __init__(self, user_info: dict):
        super().__init__(user_info)
        self.account_type = "debit"


class CreditAccount(BankAccount):
    def __init__(self, user_info: dict, credit_score=200):
        super().__init__(user_info)
        self.account_type = "credit"
        if not (200 <= credit_score <= 600):
            raise ValueError("Credit score must be between 200 and 600 for pakistani user.")
        self.credit_score = credit_score
        self.credit_limit = self.calculate_credit_limit()

    def calculate_credit_limit(self):
        min_score, max_score = 200, 600
        min_limit, max_limit = 200, 600
        return min_limit + ((self.credit_score - min_score) / (max_score - min_score)) * (max_limit - min_limit)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance + self.credit_limit:
            raise ValueError("Withdrawal exceeds balance + credit limit")
        self.balance -= amount
        return self.balance

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nCredit Score: {self.credit_score}\nCredit Limit: {self.credit_limit:.2f}"
