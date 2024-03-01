print(30*'=',"welcome to vivek super market",30*'=')
name=input("Enter your name   :")
address=input("Enter your address:")
#To prsent the list

it='''
rice   = 50rs/kg
sugar  = 40rs/1kg
oil    = 175rs/1liter
milk   = 60rs/1liter
coffee = 5rs/1packet
tea    = 5rs/1packet
chips  = 20rs/1packet
maggie = 10rs/1packet
soap   = 30rs/1unit
egg    = 6rs/1unit
'''
#declaration
price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]

# rates for  list
items={"rice":50,"sugar":40,"oil":175,"milk":60,"coffee":5,"tea":5,"chips":20,"maggie":10,"soap":30,"egg":6}
print("To see the list of items print 1 or press any number to  to exit")
i1=int(input("Enter the number:"))
if i1==1:
    print(it)
    for i in range(len(items)):
        print("To purchase press 1 or press 2 to exit ")
        x=int(input("Enter the number:"))
        if x==2:
            break
        if x==1:
            item=input(("Enter your item name:"))
            quantity=int(input("Enter the item quantity:"))
            if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,items,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
            else:
                print("sorry you enterd item is not available")
        else:
            print("you enterd wrong number")
        print("can i bill the items yes(press 1) or no (press 0)")
        inp=int(input())
        if inp==1:
            pass
            if totalprice!=0:
                print(35*"=","Vivek Super Market",35*"=")
                print("Name   :",name)
                print("Address:",address)
                print(90*"-")
                print("Sno",15*" ","Items",15*" ","Quantity",18*" ","Price",)
                print(90*"-")
                for i in range(len(pricelist)):
                    print(" ",i,15*" ",ilist[i],19*" ",qlist[i],22*" ",plist[i])
                print(90*"-")
                print(60*" ","TotalAmount:","Rs",totalprice)
                print(90*"-")
                print(32*"-","Thank you visit again",35*"-")
            
else:
    print("thank you visit again")
    
