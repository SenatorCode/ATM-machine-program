import getpass
import random
import json

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
            accounts= json.load(dataFile)
    except FileNotFoundError:
        accounts= []
    accounts.append(newAccount)

    with open("data.json", "w") as dataFile:
        json.dump(accounts, dataFile, indent=4)
    print("Your account has been created successfully. Thank You for choosing us. Happy Banking!!!")




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
            attempt = 0
            print("Welcome " + account["Fullname"])
            while attempt < 3:
                userPin = getpass.getpass("Enter your pin: ")
                if userPin == account["pin"]:
                    print("You have log into your account successfully")
                    return
                else:
                    attempt +=1
                    attemptLeft = 3 - attempt
                    print(f"You have {attemptLeft} more trials!!!")
            print("You have entered incorrect pins 3 times, your account has been locked, reach out to our nearest bank to reactivate your account.")
            account["Locked"] = True
            with open("data.json", "w") as dataFile:
                json.dump(accounts, dataFile, indent=4)
            return

        else:
            print("The account number you enter does not exist")
            userInput = input("Do you want to create a new account, Y/N")
            if userInput.upper()== "Y":
                createNewAccount()
            else:
                print("Have a nice day!!!")
                return
