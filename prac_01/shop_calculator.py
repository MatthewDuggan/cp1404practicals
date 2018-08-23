#Enter the number of items purchased
number_of_items=int(input("Number of items: "))
if number_of_items < 0:
    print("Invalid number of items!")
else:
    #Depending on number of items purchased, ask user that many times for price and add that to total price
    total_cost = 0
    for i in range(1, number_of_items+1, 1):
        item_cost = float(input("Price of item: $"))
        total_cost = total_cost+item_cost

    #If the total price is over $100, discount by 10%
    if total_cost > 100:
        total_cost=total_cost-(total_cost*0.1)
    elif 0 <= total_cost <= 100:
        total_cost=total_cost
    else:
        print("There has been an error")

    #Display total price
    print("Total price for", number_of_items, "items is $", total_cost)
