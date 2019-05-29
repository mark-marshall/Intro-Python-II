# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, key, name, description, items):
        self.key = key
        self.name = name
        self.description = description
        self.items = items
    
    def __repr__(self):
        return f"Room: {self.name}, Description: {self.description}, Items: {self.items}"

    def __str__(self):
        return f"Room: {self.name}, Description: {self.description}, Items: {self.items}"