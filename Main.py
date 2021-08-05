menu = ["Cappuccino","Espresso","Latte","Iced Coffee"]
price = [3.00,2.25,2.50,2.50]

Order_item = []
Price_item = []
more_orders = True

ordermethod = input("Order Method: ")
while more_orders:
    if ordermethod== "New Order":
        order = input("What would you like?: ")
        if order == "Cappuccino":
            cap_quantity = int(input("How many would you like?: "))
            Order_item.append(menu[0] + " * " + str(cap_quantity))
            Price_item.append(price[0] * (cap_quantity))
        elif order == "Espresso":
            esp_quantity = int(input("How many would you like?: "))
            Order_item.append(menu[1] + " * " + str(esp_quantity))
            Price_item.append(price[1] * (esp_quantity))
        elif order == "Latte":
            lat_quantity = int(input("How many would you like?: "))
            Order_item.append(menu[2] + " * " + str(lat_quantity))
            Price_item.append(price[2] * (lat_quantity))
        elif order == "Iced Coffee":
            ice_quantity = int(input("How many would you like?: "))
            Order_item.append(menu[3] + " * " + str(ice_quantity))
            Price_item.append(price[3] * (ice_quantity))
        else:
            print("Wrong Input")
    next_item = input("Next item?: (Y/N)")
    if next_item == "N":
        more_orders = False
dining = input("Dine In or Take Away: (D/T")
print("          Receipt")
print("............................")
print(Order_item)
print(f"${sum(Price_item)}")
print(f"GST=${sum(Price_item)*float(0.1).__round__(2)}")
print(f"With GST=${round(sum(Price_item)*float(1.1),2)}")
if dining == "T":
    print(f"Surcharge =${round(sum(Price_item)*float(0.05),2)}")
else:
    print("Surcharge = $0.00")
