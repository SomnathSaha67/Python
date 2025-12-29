items=[]
price=[]
while True:
    item=input("Enter the item name (or type 'q' to quit): ").lower()
    if item=='q':
        break
    cost=float(input("Enter the price of {}: ".format(item)))
    items.append(item)
    price.append(cost)
print("\nShopping Cart Summary:")
total=sum(price)
for i in range(len(items)):
    print("- {}: ${:.2f}".format(items[i], price[i]))
print("Total Cost: ${:.2f}".format(total))