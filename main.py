from bank_class.revise_bank_app import DebitAccount, CreditAccount
from validate import (
    validate_name,
    validate_age,
    validate_contact_no,
    validate_amount,
    validate_account_type,
    validate_credit_score
)


def get_user_info():
    while True:
        try:
            name = input("Enter name: ")
            valid, name = validate_name(name)
            if not valid:
                print(name)
                continue

            age = int(input("Enter age: "))
            valid, age = validate_age(age)
            if not valid:
                print(age)
                continue

            contact = input("Enter contact number: ")
            valid, contact = validate_contact_no(contact)
            if not valid:
                print(contact)
                continue

            return {
                "name": name,
                "age": age,
                "contact_no": contact
            }
        except KeyboardInterrupt:
            print("\nExiting program...")
            exit()
        except Exception as e:
            print(f"Unexpected error: {e}")


def create_account(user_info):
    while True:
        try:
            acc_type = input("Choose account type (debit / credit): ")
            valid, acc_type = validate_account_type(acc_type)
            if not valid:
                print(acc_type)
                continue

            if acc_type == "debit":
                return DebitAccount(user_info)
            else:
                while True:
                    credit_score = input("Enter your credit score (200-600): ")
                    valid, credit_score = validate_credit_score(credit_score)
                    if not valid:
                        print(credit_score)
                        continue
                    return CreditAccount(user_info, credit_score)
        except KeyboardInterrupt:
            print("\nExiting program...")
            exit()
        except Exception as e:
            print(f"Failed to create account: {e}")


def main():
    user_info = get_user_info()
    account = create_account(user_info)

    while True:
        try:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. See Details")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice in ("1", "2"):
                amt = float(input("Enter amount: "))
                valid, amt = validate_amount(amt)
                if not valid:
                    print(amt)
                    continue

                try:
                    if choice == "1":
                        account.deposit(amt)
                        print(f"Deposited: {amt:.2f}")
                    else:
                        account.withdraw(amt)
                        print(f"Withdrawn: {amt:.2f}")
                except Exception as e:
                    print(e)

            elif choice == "3":
                print(f"Balance: {account.check_balance():.2f}")

            elif choice == "4":
                print(account)

            elif choice == "5":
                print("Goodbye")
                break

            else:
                print("Invalid option")

        except KeyboardInterrupt:
            print("\nExiting program...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
