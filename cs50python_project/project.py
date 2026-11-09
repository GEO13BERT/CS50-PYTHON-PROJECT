import csv
import sys
import re
from datetime import datetime




def load_inventory(filename):
    inventory=[]
    try:
        with open(filename ,mode='r') as file:
            reader=csv.DictReader(file)
            for i in reader:
                i['size']= float(i['size'])
                i['price']=float(i['price'])
                i['stock']=float(i['stock'])
                inventory.append(i)
        return inventory
    except FileNotFoundError:
        sys.exit("The file does not exist.")

def check_stock(inventory, size, id):
    for items in inventory:
        if id==items['id'] and size==items['size']:
            return (items['stock'])
    return -1

def get_stock(inventory,expectedStock):
    lowstock=[]
    for i in inventory:
        if i['stock']<=expectedStock:
            lowstock.append(i['stock'])
    return (lowstock)

def reserve(inventory,reserved,id,size):
    for i in inventory:
        if id==i['id'] and size==i['size']:
            if i['stock']>0:
                reserved.append(i['id'])
                i['stock']-=1
                return True
    return False

def defective(inventory,defected,id,size):
    for i in inventory:
        if id==i['id'] and size==i['size']:
            if i['stock']>0:
                defected.append(i['id'])
                i['stock']-=1
                with open("defective.csv", mode='a') as file:
                    writer=csv.writer(file)
                    writer.writerow([id,size])
                return True
    return False

def valid_sku(sku,brand):
    brand=brand.lower()
    if brand=="adidas":
        if re.search(r"^[A-Z]{2}\d{4}$",sku):
            return True
        else:
            return False
    else:
        if re.search(r"^\w{4}\-\d{3}$", sku):
            return True
        else:
            return False





def main():



    if len(sys.argv)<2 or len(sys.argv)>2:
        sys.exit("You must give exactly two files")
    if not sys.argv[0].endswith(".py") and not sys.argv[1].endswith(".csv"):
        sys.exit("The files must end with .py and .csv")
    inventory=load_inventory(sys.argv[1])
    employer=input("Give employer id ")
    login=datetime.now()
    with open("employer_log.csv", mode='a') as file:
        writer=csv.writer(file)
        writer.writerow([employer,login])
    reserved=[]
    defected=[]
    while True:
        print("1.Check store balance")
        print("2.Get Stock")
        print("3.Reserve an item")
        print("4.Add Defective item")
        print("5.Check the validation of a sku code")
        print("6.Exit")
        choice=input("Make a choice through 1-6 ")
        choice=int(choice)
        if choice==6:
            print("Goodbye. Thanks for joining our Cosmos!")
            break
        elif choice==1:
            id=input("Give id ")
            size=input("Give size ")
            size=float(size)
            checking=check_stock(inventory,size,id)
            if checking==-1:
                print("Shoe not found")
            else:
                print(f"Available stock: {checking}")
        elif choice==2:
            minimum_stock=input("How many stocks do we need? ")
            minimum_stock=float(minimum_stock)
            order=get_stock(inventory,minimum_stock)
            print(order)
        elif choice==3:
            size=input("Give size of the item ")
            size=float(size)
            id=input("Give id of the item ")
            reservation=reserve(inventory, reserved, id ,size)
            if reservation==True:
                print("The reservation has been completed")
            else:
                print("Insufficient stock/ Could not find the item")
        elif choice==4:
            size=input("Give the size of the defective shoe ")
            size=float(size)
            id=input("Give the id of the defective item ")
            d=defective(inventory, defected,id,size)
            if d==True:
                print("Item sucesfully added to defective list")
            else:
                print("Insuficcient stock / Could not find the item")
        elif choice==5:
            brand=input("Give the item's brand ")
            sku=input("Give the sku code of the item ")
            valid=valid_sku(sku,brand)
            if valid==True:
                print("The sku code is valid")
            else:
                print("Invalid sku code")

if __name__=="__main__":
    main()







