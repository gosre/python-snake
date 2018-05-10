

# Snake.py
# Represents a snake on the screen
# @author Clayton Williams
class Snake:

    # The body parts attached to the snake
    body_parts = []

    def __init__(self):
        self.add_body_part(BodyPart())

    # Adds a body part to the snake
    def add_body_part(self, part):
        self.body_parts.append(part)


# Represents a body part on the snake
class BodyPart:

    # The x and y coordinate for this body part
    x = 0
    y = 0

    def __init__(self):
        pass

    # Sets the position for this body part
    def set_position(self, x, y):
        self.x = x
        self.y = y




