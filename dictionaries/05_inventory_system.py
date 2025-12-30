stock={}
while True:
    item=input("Enter item name to add to inventory (or type 'q' to quit): ")
    if item.lower()=='q':
        break
    quantity=int(input("Enter quantity for {}: ".format(item)))
    stock[item]=quantity
print("Inventory Stock Dictionary:")
for item, quantity in stock.items():
    print("{}: {}".format(item, quantity))
add_item=input("Enter item name to add more stock (or type 'q' to quit): ")
if add_item.lower()!='q':
    add_quantity=int(input("Enter quantity to add for {}: ".format(add_item)))
    if add_item in stock:
        stock[add_item]+=add_quantity
    else:
        stock[add_item]=add_quantity
print("Updated Inventory Stock Dictionary:")
for item, quantity in stock.items():
    print("{}: {}".format(item, quantity))