# Question no: 1
X = "1"
amount = 10000
pin_code = 2456

while X == "1":
    choice = int(input("Press 1 for debit, press 2 for credit, press 3 for check balance, press 4 for PIN change: "))
    PIN = int(input("Please enter your PIN: "))
    
    if PIN == pin_code:
        if choice == 1:
            debit = int(input("Please enter the amount you want to withdraw: "))
            amount = amount - debit
            print("The amount now available", amount)
        
        elif choice == 2:
            credit = int(input("Enter the amount you want to credit: "))
            amount = amount + credit
            print("The credited amount is", amount)
        
        elif choice == 3:
            print("Your current balance is", amount)
        
        elif choice == 4:
            new_pin = int(input("Enter your new PIN: "))
            pin_code = new_pin
            print("Your PIN has been successfully changed.")
        
        else:
            print("Invalid choice. Please try again.")
        
        # Option to continue or exit
        X = input("Press 1 to continue or any other key to exit: ")
    
    else:
        print("Incorrect PIN. Please try again.")