import getpass
import random
import json
import os

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def pinChecker(original):
    attempt = 0 
    while attempt < 3:
        userInput = getpass.getpass("Enter your pin: ")
        if userInput == original:
            return True
        else:
            attempt += 1 
            attemptLeft = 3 - attempt
            print(f"You have {attemptLeft} more trials!!!")
    return False

def readFile():
    try:
        with open("data.json", "r") as dataFile:
            accounts = json.load(dataFile)
    except FileNotFoundError:
        accounts = []
    return accounts

def getRecipientAccount(length, action):
    while True:
        recipient = input(f"Enter recipient {action} number, ({length}) digits: ")
        if not recipient.isdigit():
            print("Only numbers allowed. Try again.")
            continue
        if len(recipient) != length:
            print(f"{action} number must be {length} digits. Try again.")
            continue
        confirm = input(f"Confirm {action} number {recipient}? (Y/N): ")
        if confirm.upper() == "Y":
            return recipient

def createNewAccount():
    clearScreen()
    fullName = input("Enter your full name (First Last Surname): ")
    try:
        pin = getpass.getpass("Enter your pin: ")
        confirmPin = getpass.getpass("Re-enter your pin: ")
    except:
        print("Digits only!")
        input("Press Enter to continue...")
        return
    if pin != confirmPin:
        print("The pin does not match.")
        input("Press Enter to continue...")
        return

    accType = input("Enter the type of account (1= Savings, 2= Current, 3= Student): ")
    if accType == "1":
        userAccount = "Savings"
    elif accType == "2":
        userAccount = "Current"
    elif accType == "3":
        userAccount = "Student"
    else:
        print("Wrong input.")
        input("Press Enter to continue...")
        return

    accountNumber = str(random.randint(10**9, 10**10 - 1))
    newAccount = {
        "Fullname": fullName,
        "pin": pin,
        "Account Type": userAccount,
        "Balance": 0,
        "Locked": False,
        "Account Number": accountNumber
    }

    accounts = readFile()
    accounts.append(newAccount)
    with open("data.json", "w") as dataFile:
        json.dump(accounts, dataFile, indent=4)
    print("Account created successfully.")
    print(f"Your account number is {accountNumber}")
    input("Press Enter to continue...")

def checkBalance(account):
    clearScreen()
    for acc in readFile():
        if acc["Account Number"] == account["Account Number"]:
            print(f"Your account balance is: ₦{acc['Balance']:,}")
            if acc["Balance"] < 1000:
                print("Alert!!! Your balance is low.")
            input("Press Enter to continue...")
            return

def withdraw(account):
    clearScreen()
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            try:
                amount = int(input("Enter the amount you want to withdraw: "))
            except:
                print("Invalid input.")
                input("Press Enter to continue...")
                return
            if not pinChecker(acc["pin"]):
                print("You have entered incorrect pins 3 times.")
                input("Press Enter to continue...")
                return
            if amount > acc["Balance"]:
                print("Insufficient balance.")
                input("Press Enter to continue...")
                return
            elif amount <= 0:
                print("Invalid amount.")
                input("Press Enter to continue...")
                return
            acc["Balance"] -= amount
            print(f"Withdrawal successful. New balance: ₦{acc['Balance']:,}")
            with open("data.json", "w") as dataFile:
                json.dump(accounts, dataFile, indent=4)
            input("Press Enter to continue...")
            return

def deposit(account):
    clearScreen()
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            try:
                depoAmount = int(input("Enter the amount you wish to deposit: "))
            except:
                print("Invalid input.")
                input("Press Enter to continue...")
                return
            if depoAmount <= 0:
                print("You cannot deposit ₦0 or a negative number.")
                input("Press Enter to continue...")
                return
            elif depoAmount < 100:
                print("Minimum deposit is ₦100.")
                input("Press Enter to continue...")
                return
            confirm = input(f"Confirm deposit of ₦{depoAmount:,}? Y/N: ")
            if confirm.upper() != "Y":
                print("Deposit cancelled.")
                input("Press Enter to continue...")
                return
            if not pinChecker(acc["pin"]):
                print("Incorrect PIN 3 times.")
                input("Press Enter to continue...")
                return
            acc["Balance"] += depoAmount
            print(f"₦{depoAmount:,} deposited successfully.")
            print(f"New balance: ₦{acc['Balance']:,}")
            with open("data.json", "w") as dataFile:
                json.dump(accounts, dataFile, indent=4)
            input("Press Enter to continue...")
            return

def transfer(account):
    clearScreen()
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            recipientAccount = getRecipientAccount(10, "account")
            try:
                amount = int(input(f"Enter amount to transfer to {recipientAccount}: "))
            except:
                print("Invalid input.")
                input("Press Enter to continue...")
                return
            if not pinChecker(acc["pin"]):
                print("Incorrect PIN 3 times.")
                input("Press Enter to continue...")
                return
            if amount > acc["Balance"]:
                print("Insufficient funds.")
                input("Press Enter to continue...")
                return
            acc["Balance"] -= amount
            print(f"Transfer of ₦{amount:,} to ({recipientAccount}) was successful.")
            print(f"New balance: ₦{acc['Balance']:,}")
            with open("data.json", "w") as dataFile:
                json.dump(accounts, dataFile, indent=4)
            input("Press Enter to continue...")
            return

def airtimePurchase(account):
    clearScreen()
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            recipient = getRecipientAccount(11, "phone")
            try:
                amount = int(input(f"Enter amount of airtime to {recipient}: "))
            except:
                print("Invalid input.")
                input("Press Enter to continue...")
                return
            network = input("Enter network (MTN, GLO, Airtel, Etisalat, 9mobile): ").lower()
            if network not in ["mtn", "glo", "airtel", "etisalat", "9mobile"]:
                print("Invalid network.")
                input("Press Enter to continue...")
                return
            if not pinChecker(acc["pin"]):
                print("Incorrect PIN 3 times.")
                input("Press Enter to continue...")
                return
            if amount > acc["Balance"]:
                print("Insufficient funds.")
                input("Press Enter to continue...")
                return
            elif amount <= 0:
                print("Cannot send ₦0 or negative.")
                input("Press Enter to continue...")
                return
            elif amount > 100000:
                print("Airtime limit is ₦100,000.")
                input("Press Enter to continue...")
                return
            acc["Balance"] -= amount
            print(f"Airtime of ₦{amount:,} sent to {recipient}.")
            print(f"New balance: ₦{acc['Balance']:,}")
            with open("data.json", "w") as dataFile:
                json.dump(accounts, dataFile, indent=4)
            input("Press Enter to continue...")
            return

def changePin(account):
    clearScreen()
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            if not pinChecker(acc["pin"]):
                print("Incorrect PIN 3 times. Account locked.")
                acc["Locked"] = True
                with open("data.json", "w") as dataFile:
                    json.dump(accounts, dataFile, indent=4)
                input("Press Enter to continue...")
                return
            try:
                newPin = int(getpass.getpass("Enter new pin: "))
                confirmPin = int(getpass.getpass("Confirm new pin: "))
            except:
                print("Digits only.")
                input("Press Enter to continue...")
                return
            if newPin != confirmPin:
                print("Pins do not match.")
                input("Press Enter to continue...")
                return
            acc["pin"] = newPin
            print("Pin changed successfully.")
            with open("data.json", "w") as dataFile:
                json.dump(accounts, dataFile, indent=4)
            input("Press Enter to continue...")
            return

def deleteAccount(account):
    clearScreen()
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            confirm = input("Are you sure you want to delete this account? Y/N: ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                input("Press Enter to continue...")
                return
            if not pinChecker(acc["pin"]):
                print("Incorrect PIN 3 times. Account locked.")
                acc["Locked"] = True
                with open("data.json", "w") as dataFile:
                    json.dump(accounts, dataFile, indent=4)
                input("Press Enter to continue...")
                return
            accounts.remove(acc)
            with open("data.json", "w") as dataFile:
                json.dump(accounts, dataFile, indent=4)
            print("Account deleted successfully.")
            input("Press Enter to continue...")
            return

def accountManager(account):
    while True:
        clearScreen()
        print(f"Welcome, {account['Fullname']}")
        print("""
1 = Check balance
2 = Withdrawal
3 = Transfer
4 = Deposit
5 = Airtime purchase
6 = Change Pin
7 = Open new account
8 = Delete account
9 = Log out
        """)
        choice = input("Choose an option: ")
        if choice == "1":
            checkBalance(account)
        elif choice == "2":
            withdraw(account)
        elif choice == "3":
            transfer(account)
        elif choice == "4":
            deposit(account)
        elif choice == "5":
            airtimePurchase(account)
        elif choice == "6":
            changePin(account)
        elif choice == "7":
            createNewAccount()
        elif choice == "8":
            deleteAccount(account)
        elif choice == "9":
            break
        input("\nPress Enter to continue...")

def accountLogIn():
    clearScreen()
    userAccount = input("Enter your account number: ")
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == userAccount:
            if acc["Locked"]:
                print("Your account is locked. Visit branch.")
                input("Press Enter to continue...")
                return
            print("Welcome " + acc["Fullname"])
            if pinChecker(acc["pin"]):
                accountManager(acc)
                return
            else:
                print("Incorrect PIN 3 times. Account locked.")
                acc["Locked"] = True
                with open("data.json", "w") as dataFile:
                    json.dump(accounts, dataFile, indent=4)
                input("Press Enter to continue...")
                return
    print("Account not found.")
    if input("Create new account? Y/N: ").upper() == "Y":
        createNewAccount()
    else:
        print("Goodbye.")
        input("Press Enter to continue...")
