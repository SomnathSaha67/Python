bill_amount=float(input("Enter the bill amount: "))
if bill_amount>=1000:
    discount=bill_amount*0.2
    print("You get a 20% discount of:", discount)
    final_amount=bill_amount-discount
    print("Final amount to be paid:", final_amount)
elif bill_amount>=500:
    discount=bill_amount*0.1
    print("You get a 10% discount of:", discount)
    final_amount=bill_amount-discount
    print("Final amount to be paid:", final_amount)
else:
    print("No discount applicable.")
    print("Final amount to be paid:", bill_amount)