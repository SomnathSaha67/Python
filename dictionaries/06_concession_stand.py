concession_stand={}
while True:
    item=input("Enter concession stand item to add (or type 'q' to quit): ")
    if item.lower()=='q':
        break
    price=float(input("Enter price for {}: ".format(item)))
    concession_stand[item]=price
print("Concession Stand Menu Dictionary:")
for item, price in concession_stand.items():
    print("{}: ${:.2f}".format(item, price))
add_item=input("Enter concession stand item to add more (or type 'q' to quit): ")
if add_item.lower()!='q':
    new_price=float(input("Enter price for {}: ".format(add_item)))
    concession_stand[add_item]=new_price
print("Updated Concession Stand Menu Dictionary:")
for item, price in concession_stand.items():
    print("{}: ${:.2f}".format(item, price))
purchase_item=input("Enter item to purchase (or type 'q' to quit): ")
total_cost=0.0
if purchase_item.lower()!='q':
    if purchase_item in concession_stand:
        total_cost+=concession_stand[purchase_item]
        print("{} : ${:.2f}".format(purchase_item, concession_stand[purchase_item]))
    else:
        print("Item {} not found in concession stand.".format(purchase_item))
print("Total cost of purchase: ${:.2f}".format(total_cost))             
