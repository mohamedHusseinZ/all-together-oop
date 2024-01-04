#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

    def shoe_info(self):
        return f"{self.brand} - Size {self.size} - Color: {self.color}"

# Example usage:
my_shoe = Shoe(brand="Nike", size=10, color="Blue")

# Display information about the shoe
print(my_shoe.shoe_info())
