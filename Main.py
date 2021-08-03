menu = ("Cappuccino","Espresso","Latte","Iced Coffee")

Order_item = []
Price_item = []
more_orders = True

ordermethod = input("Order Method: ")
while more_orders:
    if ordermethod== "New Order":
        order = input("What would you like?: ")
        if order == "Cappuccino":
            cap_quantity = input("How many would you like?: ")
            Order_item.append(menu[0] + " * " + str(cap_quantity))
        elif order == "Espresso":
            esp_quantity = input("How many would you like?: ")
            Order_item.append(menu[1] + " * " + str(esp_quantity))
        elif order == "Latte":
            lat_quantity = input("How many would you like?: ")
            Order_item.append(menu[2] + " * " + str(lat_quantity))
        elif order == "Iced Coffee":
            ice_quantity = input("How many would you like?: ")
            Order_item.append(menu[3] + " * " + str(ice_quantity))
        else:
            print("Wrong Input")
    next_item = input("Next item?: (Y/N)")
    if next_item == "N":
        more_orders = False
print(Order_item)
print()
