import csv
import os
import time
import pyperclip

def load_passwords_from_csv(filename):
    account_info = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                continue
            account_type, username_email, password = row
            account_type = account_type.strip().lower()
            if account_type not in account_info:
                account_info[account_type] = []
            account_info[account_type].append({
                'username': username_email.strip(),
                'password': password.strip()
            })
    return account_info

def main():
    filename = os.path.join(os.getcwd(), "example.csv")

    if not os.path.exists(filename):
        print('\033[91mCould not find example.csv in the current directory.\033[0m')
        print(f'Looked in: {filename}')
        return

    try:
        ACCOUNT_INFO = load_passwords_from_csv(filename)
    except Exception as e:
        print('\033[91mFailed to read CSV:\033[0m', e)
        return

    while True:
        account_type = input("Account type: ").strip().lower()

        if account_type not in ACCOUNT_INFO:
            print('\033[91mThere is no account type named ' + account_type + '\033[0m')
            continue

        # Account selection loop
        while True:
            print(f"\nAccounts for '{account_type}':")
            for idx, account in enumerate(ACCOUNT_INFO[account_type], start=1):
                print(f"{idx}. {account['username']}")

            choice = input("\nAccount option: ").strip()

            if not (choice.isdigit() and 1 <= int(choice) <= len(ACCOUNT_INFO[account_type])):
                print('\033[91mInvalid selection.\033[0m')
                # Re-ask only the account option
                continue

            selected_account = ACCOUNT_INFO[account_type][int(choice) - 1]

            pyperclip.copy(selected_account['password'])
            print('\033[92mPassword copied to clipboard.\033[0m')

            # Wait 10 seconds, clear clipboard, and exit
            time.sleep(10)
            pyperclip.copy('')
            print('\033[93mClipboard cleared. Exiting.\033[0m')
            return  # Exit the program

if __name__ == "__main__":
    main()
