

class PizzaOrder:
    def __init__(self):
        self.topping_count = 0

    def add_topping(self, topping):
        if topping == "pepperoni":
            self.topping_count += 1
        if topping == "mushrooms":
            self.topping_count += 1
        if topping == "extra cheese":
            self.topping_count +=1
            return True
        return False

def calculate_total(self):
    return 10.00 + (self.topping_count * 1.50)


order = PizzaOrder()

while True:
    topping = input("Enter topping: ").lower()

    if topping == "done":
        break
        print("Sorry! Not on the menu.")

print(order.calculate_total())