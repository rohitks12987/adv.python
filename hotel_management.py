#Hotel Management System using Inheritance they have class like veg,non veg,sea food ,drinks ,desserts including the menu and bill generation
class Menu:
    def __init__(self):
        self.menu_items = {
            "veg": {"paneer butter masala": 150, "dal makhani": 100},
            "non_veg": {"chicken curry": 200, "mutton curry": 250},
            "sea_food": {"fish curry": 180, "prawn curry": 220},
            "drinks": {"coke": 50, "lemonade": 40},
            "desserts": {"gulab jamun": 80, "ice cream": 60}
        }
    def display_menu(self):
        print("Menu:")
        for category, items in self.menu_items.items():
            print(f"{category.capitalize()}:")
            for item, price in items.items():
                print(f" - {item}: {price} INR")
class Bill(Menu):
    def __init__(self):
        super().__init__()
        self.order = []
    def add_to_order(self, category, item):
        if category in self.menu_items and item in self.menu_items[category]:
            self.order.append((item, self.menu_items[category][item]))
            print(f"Added {item} to order.")
        else:
            print("Item not found in menu.")
    def generate_bill(self):
        total = sum(price for item, price in self.order)
        print("\nBill Summary:")
        for item, price in self.order:
            print(f"{item}: {price} INR")
        print(f"Total: {total} INR")
# Example usage
bill = Bill()
bill.display_menu()
bill.add_to_order("veg", "paneer butter masala")
bill.add_to_order("non_veg", "chicken curry")
bill.add_to_order("drinks", "coke")
bill.generate_bill()