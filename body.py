import functions
sessionActive = True 

while sessionActive == True :
    print ("Welcome to Alex & Co Bank.")
    print("""
    Press 1 to log into your bank account
    Press 2 to create a new bank account
    Press 3 to exit 
""")

    userInput = (input("Please enter your choice: "))
    if userInput == "1":
        functions.accountLogIn()
    elif userInput =="2":
        functions.createNewAccount()
    elif userInput == "3":
        print("Thank you for banking with us, See you next time.")
        sessionActive = False
    else: 
        print("Invalid selection, please try again")