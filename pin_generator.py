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
                        newpin = input("create your new pin:")
                        newdata = {'Pin':newpin}
                        data[i].update(newdata)
                        print("pin is created thanks")
                        break
                else:
                    print("data not found")

        with open("B_data.json",'w') as f:
            json.dump(data,f,indent=2)