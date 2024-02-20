import csv
import pyperclip

def load_passwords_from_csv(filename):
    account_info = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Skip rows that don't have exactly 3 values
            if len(row) != 3:
                continue
            account_type, username_email, password = row
            account_type = account_type.lower()
            if account_type not in account_info:
                account_info[account_type] = []
            account_info[account_type].append({'username': username_email, 'password': password})
    return account_info

filename = r"C:\Users\D E L L\Documents\GitHub\Password-Locker\Passwords\Passwords.csv" #This needs to be changed accordingly

ACCOUNT_INFO = load_passwords_from_csv(filename)

account_type = input("Account type: ").lower()

# Check if account type exists then list potential accounts
if account_type in ACCOUNT_INFO:
    print(f"\nAccounts for '{account_type}':")
    
    for idx, account in enumerate(ACCOUNT_INFO[account_type], start=1):
        print(f"{idx}. {account['username']}") 
    
    choice = input("\nAccount option: ")
    
    if choice.isdigit() and 0 < int(choice) <= len(ACCOUNT_INFO[account_type]):
        selected_account = ACCOUNT_INFO[account_type][int(choice) - 1]
        pyperclip.copy(selected_account['password'])
        print('\033[92mPassword copied to clipboard.\033[0m')
    elif choice:
        print('\033[91mInvalid selection.\033[0m')
else:
    print('\033[91m' + 'There is no account type named ' + account_type + '\033[0m')





