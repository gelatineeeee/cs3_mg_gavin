class Pizza:
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        if topping in ["pepperoni", "mushrooms", "extra cheese"]:
            self.toppings.append(topping)
        else:
            print("Sorry! Not on the menu.")

    def calculate_total(self):
        return 10.00 + (len(self.toppings) * 1.50)



pizza = Pizza()

pizza.add_topping("pepperoni")
pizza.add_topping("mushrooms")
pizza.add_topping("extra cheese")


print(f"Total: ${pizza.calculate_total()}")
