SNAKE_WIDTH = 32
SNAKE_HEIGHT = 32


class Snake:
    """Represents a snake with a variable number of body parts"""

    # The window (frame)
    window = None

    # The body parts attached to the snake
    body_parts = []

    # The directional velocity that our snake is traveling for the next cycle
    # x,y denoted as -1, 0, or 1
    velocity = [0, 0]

    def __init__(self, window):
        self.window = window
        self.body_parts = []

    def create_body_part(self):
        """Adds a body part to the tail of the snake"""
        part = BodyPart(self.window)
        part.set_window_component(self.window.canvas.create_oval(0, 0, SNAKE_WIDTH, SNAKE_HEIGHT, outline="#733913", fill="#A0522D", width=1))
        if len(self.body_parts) == 0:
            part.set_position(400, 300)
            self.window.canvas.itemconfig(part.window_component, fill="#733913")
        else:
            last = self.body_parts[-1]
            part.set_position(last.last_position[0], last.last_position[1])
        self.body_parts.append(part)

    def move_snake(self):
        """Moves the snake and all parts"""
        for i in range(0, len(self.body_parts)):
            part = self.body_parts[i]
            if i == 0:
                part.set_position(part.x + (self.velocity[0] * 5), part.y + (self.velocity[1] * 5))
            else:
                last = self.body_parts[i - 1]
                part.set_position(last.last_position[0], last.last_position[1])

    def change_direction(self, key):
        """Changes the snake's direction of movement based on the key pressed"""
        if key == "Down" and self.velocity != [0, -1]:
            self.velocity = [0, 1]
        elif key == "Up" and self.velocity != [0, 1]:
            self.velocity = [0, -1]
        elif key == "Left" and self.velocity != [1, 0]:
            self.velocity = [-1, 0]
        elif key == "Right" and self.velocity != [-1, 0]:
            self.velocity = [1, 0]

    def get_bounds(self):
        """Gets the bounds of this node"""
        return self.body_parts[0].get_bounds()


class BodyPart:
    """Represents a fixed size body part on a snake"""

    # The window (frame)
    window = None

    # The x and y coordinate for this body part
    x: int = 0
    y: int = 0

    # The last position of this part
    last_position = []

    # The component layer on the canvas
    window_component = None

    def __init__(self, window):
        self.window = window

    def set_position(self, x, y):
        self.last_position = [self.x, self.y]
        self.x = x
        self.y = y
        self.window.canvas.coords(self.window_component, x, y, x + SNAKE_WIDTH, y + SNAKE_HEIGHT)

    def set_window_component(self, component):
        self.window_component = component

    def get_bounds(self):
        return [self.x, self.y, self.x + SNAKE_WIDTH, self.y + SNAKE_HEIGHT]