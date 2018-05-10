

# Snake.py
# Represents a snake on the screen
# @author Clayton Williams
class Snake:

    # The window (frame)
    window = None

    # The body parts attached to the snake
    body_parts = []

    # The velocity
    velocity = [0, 0]

    def __init__(self, window):
        self.window = window

    # Adds a body part to the snake
    def create_body_part(self):
        part = BodyPart(self.window)
        part.set_window_component(self.window.canvas.create_oval(0, 0, 32, 32, outline="blue", fill="gray", width=1))
        if len(self.body_parts) == 0:
            part.set_position(0, 0)
        else:
            last = self.body_parts[-1]
            part.set_position(last.last_position[0], last.last_position[1])
        self.body_parts.append(part)

    # Moves the snake and all parts
    def move_snake(self):
        for i in range(0, len(self.body_parts)):
            part = self.body_parts[i]
            if i == 0:
                part.set_position(part.x + (self.velocity[0] * 5), part.y + (self.velocity[1] * 5))
            else:
                last = self.body_parts[i - 1]
                part.set_position(last.last_position[0], last.last_position[1])

    # Changes the snake's direction of movement
    def change_direction(self, key):
        if key == "Down" and self.velocity != [0, -1]:
            self.velocity = [0, 1]
        elif key == "Up" and self.velocity != [0, 1]:
            self.velocity = [0, -1]
        elif key == "Left" and self.velocity != [1, 0]:
            self.velocity = [-1, 0]
        elif key == "Right" and self.velocity != [-1, 0]:
            self.velocity = [1, 0]


# Represents a body part on the snake
class BodyPart:

    # The window (frame)
    window = None

    # The x and y coordinate for this body part
    x = 0
    y = 0

    # The last position of this part
    last_position = []

    # The component layer on the canvas
    window_component = None

    def __init__(self, window):
        self.window = window

    # Sets the position for this body part
    def set_position(self, x, y):
        self.last_position = [self.x, self.y]
        self.x = x
        self.y = y
        self.window.canvas.coords(self.window_component, x, y, x + 32, y + 32)

    # Sets the window component
    def set_window_component(self, component):
        self.window_component = component

