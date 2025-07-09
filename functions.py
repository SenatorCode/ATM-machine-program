def accountLogIn ():
    accountNumber = input("Please enter your account number: ")

def newAccount():
    fullName = input("Enter Your name in full, first name should come first, then last name, your surname should come last: ")

    import getpass
    pin = getpass.getpass("Enter your pin")
    confirmPin = getpass.getpass("Enter the pin again")

    if pin != confirmPin:
        print("The password you entered does not match")
        return
    
    userAccount= ""
    def accountType ():
        accType = input("Enter the type of account you want, 1 for savings, 2 for current, 3 for student:")
        if accType == 1:
            userAccount= "Savings"
        elif accType == 2:
            userAccount = "Current"
        elif accType == 3:
            userAccount = "Student"
        else:
            print("Wrong input, Please retry")
            accountType()
    import random
    accountNumber = random.randint(10^9, 10^10-1)
    accounts = {

    }
    accounts[random.randint(10**9, 10**10-1)] = {
        "Fullname": fullName,
        "pin": pin,
        "AccountType": userAccount,
        "Balance": 0,
        "Locked": False
    }
    print(accounts)