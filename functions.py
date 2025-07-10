import getpass
import random
import json

# Check Pin Function
def pinChecker(original):
    attempt = 0 
    while attempt < 3:
        userInput = getpass.getpass("Enter your pin: ")
        if userInput == original:
            return True
        else:
            attempt +=1 
            attemptLeft = 3 - attempt
            print(f"You have {attemptLeft} more trials!!!")
    return False


# Read data.json file Function
def readFile():
    with open("data.json", "r") as dataFile:
        accounts = json.load(dataFile)
    return(accounts)


# Create A New Account Function:
def createNewAccount():
    fullName = input("Enter Your name in full, first name should come first, then last name, your surname should come last: ")

    pin = getpass.getpass("Enter your pin")
    confirmPin = getpass.getpass("Enter the pin again")

    if pin != confirmPin:
        print("The password you entered does not match")
        return
    
    userAccount= ""
    accType = int(input("Enter the type of account you want (1= savings, 2= current, 3= student): "))
    if accType == 1:
        userAccount= "Savings"
    elif accType == 2:
        userAccount = "Current"
    elif accType == 3:
        userAccount = "Student"
    else:
        print("Wrong input, Please retry")
        return
    
    accountNumber = random.randint(10**9, 10**10-1)
    newAccount= {
        "Fullname": fullName,
        "pin": pin,
        "Account Type": userAccount,
        "Balance": 0,
        "Locked": False,
        "Account Number": str(accountNumber)
    }
    try:
        with open("data.json", "r") as dataFile:
            accounts = json.load(dataFile)
    except FileNotFoundError:
        accounts= []
    accounts.append(newAccount)

    with open("data.json", "w") as dataFile:
        json.dump(accounts, dataFile, indent=4)
    print("Your account has been created successfully. Thank You for choosing us. Happy Banking!!!")
    print(f"Your account number is {accountNumber}")


# Check Balance Function:
def checkBalance(account):
    for acc in readFile():
        if acc["Account Number"] == account["Account Number"]:
            print(f"\n Your account balance is: ₦{acc['Balance']:,}\n")
            if acc["Balance"] < 1000:
                print("Alert!!! Your balance is low.\n")
            return


# Withdraw Function:
def withdraw(account):
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            amount = int(input("Enter the amount you want to withdraw"))
            checkInput = pinChecker(acc["pin"])
            if checkInput == True:
                if amount > acc["Balance"]:
                    print("Insufficient Balance")
                    return
                else:
                    acc["Balance"] = acc["Balance"] - amount
                    print(f"Withdrawal successful, your new balance is {acc['Balance']}")
                    with open("data.json", "w") as dataFile:
                        json.dump(accounts, dataFile, indent=4)
                    return
            else:
                print("You have entered incorrect pins 3 times, Try again later.")
                return


# Transfer Function:
def getRecipientAccount():
    while True:
        recipient = input("Enter recipient account number (10 digits): ")

        # Check if it's only digits like "1234567890"
        if not recipient.isdigit():
            print("Only numbers allowed. Try again.")
            continue  # Start again

        # Check if it's exactly 11 digits
        if len(recipient) != 11:
            print("Account number must be 11 digits. Try again.")
            continue  # Start again

        # If everything is correct
        confirm = input(f"Please confirm this account number {recipient}: Y/N")
        if confirm.upper() == "Y":
            return recipient
        else:
            continue

def transfer(account):
    accounts = readFile()
    for acc in accounts:
        if acc["Account Number"] == account["Account Number"]:
            recipientAccount = getRecipientAccount()
            try: 
                amount = int(input(f"Enter the amount you want to transfer to {recipientAccount}"))
            except:
                print("Invalid input, numbers only!!!")
                return
            checkInput = pinChecker(acc["pin"])
            if checkInput == True:
                if amount > acc["Balance"]:
                    print("Insufficient Fund")
                    return
                acc["Balance"] = acc["Balance"] - amount
                with open("data.json", "w") as dataFile:
                    json.dump(accounts, dataFile, indent=4)
                print (f"Transfer to ({recipientAccount}) was successful")
                print(f"Your New balance is {acc['Balance']}")
                return
            else:
                print("You have entered incorrect pins 3 times, Try again later.")
                return


# Account Manger Function:
def accountManager(account):
    active = True
    while active is True:
        print(f"Welcome, {account["Fullname"]}")
        userChoice = input("""
    How may we assist you today: 
            1 = Check balance
            2 = withdrawal
            3 = Transfer
            4 = Deposit
            5 = Airtime purchase 
            6 = Change Pin
            7 = Open a new account
            8 = Delete Account
            9 = Log out 
    """)
        if userChoice == "1":
            checkBalance(account)
        elif userChoice == "2":
            withdraw(account)
        elif userChoice == "3":
            transfer(account)
        elif userChoice == "4":
            deposit(account)
        elif userChoice == "5":
            airtimePurchase(account)
        elif userChoice == "6":
            changePin(account)
        elif userChoice == "7":
            createNewAccount(account)
        elif userChoice == "8":
            deleteAccount(account)
        elif userChoice == "9":
            active = False
        else:
            print("Your input is invalid, please try again")
    return


# Account Log In Function:
def accountLogIn():
    userAccount = input("Enter your account number: ")
    try:
        with open("data.json", "r") as datafile:
            accounts = json.load(datafile)
    except FileNotFoundError:
        accounts= []
    
    for account in accounts:
        if userAccount == account["Account Number"]:
            if account["Locked"] != False:
                print("Your account has been blocked, please reach out to our nearest branch to reactivate your account.")
                return
            print("Welcome " + account["Fullname"])
            checkInput = pinChecker(account["pin"])
            if checkInput == True:
                accountManager(account)
                return
            elif checkInput == False:
                print("You have entered incorrect pins 3 times, your account has been locked, reach out to our nearest bank to reactivate your account.")
                account["Locked"] = True
                with open("data.json", "w") as dataFile:
                    json.dump(accounts, dataFile, indent=4)
                return
    print("The account number you enter does not exist")
    userInput = input("Do you want to create a new account, Y/N")
    if userInput.upper()== "Y":
        createNewAccount()
    else:
        print("Have a nice day!!!")
        return