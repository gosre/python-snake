import random


# Represents a piece of food to eat by the snake!
class Food:

    # The canvas component
    component = None

    # The x and y coordinates
    x = 0
    y = 0

    # Food size - for how big we should grow the snake!
    size = 0

    def __init__(self, window):
        self.x = random.randint(50, window.winfo_width() - 50)
        self.y = random.randint(50, window.winfo_height() - 50)
        self.size = random.randint(8, 20)
        self.component = window.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, outline="yellow", fill="red", width=1)

    # Gets the bounds of this node
    def get_bounds(self):
        return [self.x, self.y - self.size, self.x + self.size, self.y + self.size]

    # Gets the size of this food
    def get_size(self):
        return self.size
