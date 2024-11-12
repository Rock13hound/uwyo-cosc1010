


class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60
    
    def __init__(self):
        self.orders = 0
        self.pizzas = []

    def placeOrder(self):
        self.orders += 1

        size = int(input("Please enter the size of pizza, as a whole number. The smallest size is 10\n"))
        if size <= 10:
            size = 10
            print("Size was too small. Defaulting to 10 inches.")

        sauce = input("What kind of sauce would you like?\nLeave blank for red sauce\n").strip()
        if not sauce:
            sauce = "red"

        toppings_input = input("Please enter the toppings you would like, leave blank when done\n").strip()
        toppings = []
        while toppings_input:
            toppings.append(toppings_input.strip())
            toppings_input = input()

        pizza = Pizza(size, sauce)
        pizza.add_toppings(*toppings)

        self.pizzas.append(pizza)
        print(f"Order placed: {pizza.get_size()} inch pizza with {pizza.get_sauce()} sauce and {len(pizza.get_toppings())} toppings.")

        self.getReceipt()

    def getPrice(self):
        if not self.pizzas:
            return 0
        
        pizza = self.pizzas[-1]
        size_price = pizza.get_size() * self.price_per_inch
        topping_price = len(pizza.get_toppings()) * self.price_per_topping
        total_price = size_price + topping_price
        
        return total_price

    def getReceipt(self):
        if not self.pizzas:
            print("No pizzas ordered.")
            return
        
        pizza = self.pizzas[-1]
        sauce = pizza.get_sauce()
        size = pizza.get_size()
        toppings = pizza.get_toppings()
        size_price = size * self.price_per_inch
        topping_price = len(toppings) * self.price_per_topping
        total_price = size_price + topping_price

        print(f"\nYou ordered a {size}\" pizza with {sauce} sauce and the following toppings:")

        for topping in toppings:
            print(f"                                                                  {topping}")

        print(f"You ordered a {size}\" pizza for {size_price:.1f}")
        print(f"You had {len(toppings)} topping(s) for ${topping_price:.2f}")
        print(f"Your total price is ${total_price:.2f}")

    def getNumberOfOrders(self):
        return self.orders


# Main interaction loop
pizzeria = Pizzeria()

while True:
    user_input = input("Would you like to place an order? exit to exit\n").strip().lower()
    if user_input == "exit":
        break
    elif user_input == "yes":
        pizzeria.placeOrder()
    else:
        print("Invalid input. Please type 'yes' to order or 'exit' to exit.")

print(f"\nYou placed {pizzeria.getNumberOfOrders()} order(s).")
