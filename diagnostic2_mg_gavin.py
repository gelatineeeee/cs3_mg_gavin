def calculate_total(topping_count):
    return 10.00 + (topping_count * 1.50)

topping_count = 0

while True:
    topping = input("Enter topping: ").lower()

    if topping == "done":
        break

    if  topping == "pepperoni":
        topping_count += 1
    elif topping == "mushrooms":
        topping_count +=1
    elif topping == "extra cheese":
        topping_count += 1
    else:
        print("Sorry! Not on the menu.")
    
print(calculate_total(topping_count))

