has_ticket=bool(int(input("Do you have a ticket? Enter 1 for Yes and 0 for No: ")))
has_id=bool(int(input("Do you have an ID? Enter 1 for Yes and 0 for No: ")))
if has_ticket and has_id:
    print("You can enter the event.")
else:                   
    print("You cannot enter the event.")