#We define a Restaurant class to represent the restaurant. It has attributes for the restaurant name, a dictionary to store the menu items, and a list to store the orders.


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}
        self.orders = []
#The add_dish method is used to add dishes to the menu. It takes a dish name and price as parameters and adds them to the menu dictionary.

    def add_dish(self, dish_name, price):
        self.menu[dish_name] = price
# The place_order method is used to place an order for a dish. It takes a dish name and quantity as parameters. It first checks if the dish is available in the menu. If it is, it calculates the total price based on the dish price and quantity. Then it creates an Order object and adds it to the orders list.


    def place_order(self, dish_name, quantity):
        if dish_name not in self.menu:
            print(f"{dish_name} is not available in the menu.")
            return

        total_price = self.menu[dish_name] * quantity
        order = Order(dish_name, quantity, total_price)
        self.orders.append(order)
        print(f"Order placed: {quantity} x {dish_name}")

#The print_menu method is used to print the menu items along with their prices.
    def print_menu(self):
        print(f"{self.name} Menu:")
        for dish, price in self.menu.items():
            print(f"{dish} - ${price:.2f}")
#The print_orders method is used to print the list of orders, including the dish name, quantity, and total price.

    def print_orders(self):
        print("Orders:")
        for order in self.orders:
            print(f"{order.quantity} x {order.dish_name} - Total: ${order.total_price:.2f}")
# We define an Order class to represent an order. It has attributes for the dish name, quantity, and total price.


class Order:
    def __init__(self, dish_name, quantity, total_price):
        self.dish_name = dish_name
        self.quantity = quantity
        self.total_price = total_price

# he main function serves as the entry point of the program. Inside it, we create an instance of the Restaurant class named restaurant and perform various operations.
def main():
    restaurant = Restaurant("Restaurant XYZ")

    # Adding dishes to the menu
    restaurant.add_dish("Pizza", 10.99)
    restaurant.add_dish("Burger", 8.99)
    restaurant.add_dish("Salad", 6.99)

    # Placing orders
    restaurant.place_order("Pizza", 2)
    restaurant.place_order("Burger", 3)
    restaurant.place_order("Fries", 1)
    # Dish not in the menu

    # Print the menu
    restaurant.print_menu()

    # Print the orders
    restaurant.print_orders()


if __name__ == "__main__":
    main()
