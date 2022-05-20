import getpass
import json
class func:
    def authentication(self,card_number):  
        with open("B_data.json") as f:
            data = json.load(f)
        for i in range(len(data)):
            if data[i]['Card Number'] == card_number:
                count = 0
                while count < 3:
                    pin = input("enter pin : ")
                    if pin.isdigit() and len(pin)==4 and data[i]['Pin']==pin:
                        print("authenticated successfully")
                        return True
                        
                    else:
                        count=count+1
                        attempt = 3-count
                        print("please enter correct 4 digit pin you have {} attempts left".format(attempt))

                if count==3:
                    print("your card is blocked ! ")
                    return False

                break
        else:
            print("Please enter valid card number")

obj = func()

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

def statment(card_number):
    #if obj.authentication(card_number):

        with open("B_data.json") as f:
            data = json.load(f)
        for i in range(len(data)):
                    amount = data[i]['amount']
                    msg = f'your balance is {amount} rupees'
                    print(msg)
                    break

def deposit(card_number):
    #if obj.authentication(card_number):

            with open("B_data.json") as f:
                data = json.load(f)
            for i in range(len(data)):
                a_of_deposit = int(input("Enter deposit amount : "))
                new=int(data[i]['amount'])+a_of_deposit
                newdata = {'amount':str(new)}
                data[i].update(newdata)
                with open("B_data.json",'w') as f:
                    json.dump(data,f,indent=2)   
                break

def withdrawal(card_number):
            #obj.authentication(card_number)

            with open("B_data.json") as f:
                data = json.load(f)
            for i in range(len(data)):
                    a_of_withd = int(input("Enter withdrawal amount : "))
                    if int(data[i]['amount']) > a_of_withd:
                        new=int(data[i]['amount'])-a_of_withd
                        newdata = {'amount':str(new)}
                        data[i].update(newdata)
                        with open("B_data.json",'w') as f:
                            json.dump(data,f,indent=2)   
                        break
                    else:
                        print("you dont have sufficient balance")


