import getpass
import json
def PinGenerator(cardn,cvv,ex):
        with open("B_data.json") as f:
            data = json.load(f)
            
            for i in range(len(data)):
                if ((data[i]['Card Number'] == cardn) and (data[i]['Expire'] == ex) and (data[i]['CVV'] == cvv)):
                    if "Pin" in data[i]:
                        print("you already genrated your pin ")
                        break
                    else:
                        newpin = str(getpass.getpass("create your new pin:"))
                        if newpin.isdigit() and len(newpin)==4:
                            #newpin = input("create your new pin:")
                            newdata = {'Pin':newpin}
                            data[i].update(newdata)
                            print("pin is created thanks")
                        else:
                            print("Please enter 4 digit pin")
                        break
            else:
                print("data not found")

        with open("B_data.json",'w') as f:
            json.dump(data,f,indent=2)

def PinChange(card_number,old_pin):
    if old_pin.isdigit() and len(old_pin)==4:
                with open("B_data.json") as f:
                    data = json.load(f)
                    for i in range(len(data)):
                        if data[i]['Card Number']==card_number and data[i]['Pin']==old_pin:
                            print("Thanks for authentication !")
                            new_p = str(getpass.getpass("Enter your new pass : "))
                            if new_p.isdigit() and len(new_p)==4:
                                new_cp = str(getpass.getpass("Please confirm your pin : "))
                                if(new_cp==new_p):
                                    newdata = {'Pin':new_cp}
                                    data[i].update(newdata)
                                    print("your pin changed successfully.")
                                    break
                                else:
                                    print("incorrect! please try again.")
                            else:
                                print("please enter 4 digit pin")
                    else:
                        print("Invalid user")
                with open("B_data.json",'w') as f:
                    json.dump(data,f,indent=2)

def statment(card_number,pin):
    with open("B_data.json") as f:
        data = json.load(f)
    for i in range(len(data)):
        if data[i]['Card Number']==card_number and data[i]['Pin']==pin:
            amount = data[i]['amount']
            msg = f'your balance is {amount} rupees'
            print(msg)
            break
    else:
        print("invalid user")

def deposit(card_number,pin):
            with open("B_data.json") as f:
                data = json.load(f)
            for i in range(len(data)):
                if data[i]['Card Number']==card_number and data[i]['Pin']==pin:
                    a_of_deposit = int(input("Enter deposit amount : "))
                    new=int(data[i]['amount'])+a_of_deposit
                    newdata = {'amount':str(new)}
                    data[i].update(newdata)
                    with open("B_data.json",'w') as f:
                        json.dump(data,f,indent=2)   
                    break
            else:
                print("Invalid user")
def withdrawal(card_number,pin):
            with open("B_data.json") as f:
                data = json.load(f)
            for i in range(len(data)):
                if data[i]['Card Number']==card_number and data[i]['Pin']==pin:
                    a_of_withd = int(input("Enter withdrawal amount : "))
                    if data[i]['amount'] > a_of_withd:
                        new=int(data[i]['amount'])-a_of_withd
                        newdata = {'amount':str(new)}
                        data[i].update(newdata)
                        with open("B_data.json",'w') as f:
                            json.dump(data,f,indent=2)   
                        break
                    else:
                        print("you dont have sufficient balance")
            else:
                print("Invalid user")

