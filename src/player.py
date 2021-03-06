# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, items):
        self.name = name
        self.location = location
        self.items = items

    def __str__(self):
        return f"Player: {self.name}, Location: {self.location}"