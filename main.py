
from func import func
obj = func()
import getpass
import json
from func import PinChange, PinGenerator, deposit, statment, withdrawal
print("\nSelect operation.")
print("GP   : Generate Pin")
print("CHP  : Change Pin")
print("S    : Statment")
print("D    : Diposit")
print("W    : Withdrawal")
print("Q    : Quit an application")
with open('data_stor.json','w') as file:
    file.truncate(0)  
    file.write('{}')

while True:
    # take input from the user
    choice = input("Enter choice(GP/CHP/S/D/W/Q): ")

    # check if choice is one of the four options
    if choice in ('GP', 'CHP', 'S','D', 'W', 'Q'):
        if choice == 'GP':
            card_number = input("enter your card number : ")
            cvv = input("Enter CVV : ")
            expiry = input("Enter Expiry : ")
            PinGenerator(card_number,cvv,expiry)   

        elif choice == 'CHP':
            card_number = input("enter your card number : ")
            old_pin = str(getpass.getpass("Enter your old pin:"))
            PinChange(card_number,old_pin)

        elif choice == 'S':
            card_number = input("enter your card number : ")
            if obj.authentication(card_number) :
                statment(card_number)
            
            pass 
        elif choice == 'D':
            card_number = input("enter your card number : ")
            if obj.authentication(card_number) :
                statment(card_number)
                deposit(card_number)

        elif choice == 'W':
            card_number = input("enter your card number : ")
            if obj.authentication(card_number) :
                withdrawal(card_number)
                statment(card_number)
            pass 
        else:
            if choice =='Q':
                break
    else:
        print("invalid Input")