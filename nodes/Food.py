import random


# Represents a piece of food to eat by the snake!
class Food:

    # The canvas component
    component = None

    # The x and y coordinates
    x = 0
    y = 0

    def __init__(self, window):
        self.x = random.randint(50, 800)
        self.y = random.randint(20, 500)
        self.component = window.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, outline="yellow", fill="red", width=1)

    # Gets the bounds of this node
    def get_bounds(self):
        return [self.x, self.y, self.x + 10, self.y + 10]


