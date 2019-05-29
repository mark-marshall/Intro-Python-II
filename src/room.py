# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, key, name, description, items):
        self.key = key
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        if self.items:
            print_items = [item.name for item in self.items]
        else:
            print_items = "There are currently no items in this room"
        return f"Room: {self.name}, Description: {self.description}, Items: {print_items}"