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

    # Returns true if the snake can eat this piece of food
    def can_eat(self, snake):
        start1x = snake.body_parts[0].x
        start1y = snake.body_parts[0].y
        end1x = start1x + 32
        end1y = start1y + 32
        start2x = self.x
        start2y = self.y
        end2x = start2x + 10
        end2y = start2y + 10
        if end1x >= start2x and end2x >= start1x and end1y >= start2y and end2y >= start1y:
            return True
        return False



