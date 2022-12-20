import random


class Food:
    """Represents a piece of food that the snake can eat to gain points and increase its length"""

    # The canvas component
    component = None

    # The x and y coordinates
    x: int = 0
    y: int = 0

    # Food size - for how big we should grow the snake!
    size: int = 0

    def __init__(self, window):
        self.x = random.randint(50, window.winfo_width() - 50)
        self.y = random.randint(50, window.winfo_height() - 50)
        self.size = random.randint(8, 20)
        self.component = window.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, outline="yellow", fill="red", width=1)

    def get_bounds(self):
        return [self.x, self.y - self.size, self.x + self.size, self.y + self.size]

    def get_size(self):
        return self.size
