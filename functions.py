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
    accType = int(input("Enter the type of account you want (1=savings, 2=current, 3=student): "))
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
    except emptyFileError:
        accounts= []
    
    accounts.append(newAccount)

    with open("data.json", "w") as dataFile:
        json.dump(accounts, dataFile)

def accountLogIn():
    