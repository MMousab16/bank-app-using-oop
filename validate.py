def validate_name(name: str):
    if not name or not name.strip():
        return False, "Name cannot be empty"
    name = name.strip()
    for char in name:
        if not (char.isalpha() or char in (" ", "-")):
            return False, "Name can contain letters, spaces, or hyphens only"
    return True, name


def validate_age(age):
    if not isinstance(age, int):
        return False, "Age must be an integer"
    if age <= 18 or age >= 100:
        return False, "Age must be between 19 and 99"
    return True, age


def validate_contact_no(contact_no: str):
    if not contact_no.isdigit():
        return False, "Contact number must contain digits only"
    if len(contact_no) != 11:
        return False, "Contact number must be exactly 11 digits"
    return True, contact_no


def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        return False, "Amount must be numeric"
    if amount <= 0:
        return False, "Amount must be greater than zero"
    return True, float(amount)


def validate_account_type(account_type: str):
    if not isinstance(account_type, str):
        return False, "Account type must be a string"
    account_type = account_type.strip().lower()
    if account_type not in ("debit", "credit"):
        return False, "Account type must be 'debit' or 'credit'"
    return True, account_type


def validate_credit_score(score):
    try:
        score = int(score)
    except ValueError:
        return False, "Credit score must be numeric"
    if not (200 <= score <= 600):
        return False, "Credit score must be between 200 and 600"
    return True, score
