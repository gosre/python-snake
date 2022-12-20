"""
@author Clayton Williams
@date 5-8-2018
"""
from tkinter import *

from nodes.Food import Food
from nodes.Snake import Snake


def overlapping(bounds1, bounds2):
    """
    Checks if two rectangle boundaries are overlapping

    Returns:
        bool: true if boundaries were overlapping
    """
    return bounds1[2] >= bounds2[0] and bounds2[2] >= bounds1[0] \
        and bounds1[3] >= bounds2[1] and bounds2[3] >= bounds1[1]


def main():

    # Create a new instance of Tkinter
    root = Tk()

    # Create an instance of our custom window class
    app = Window(root)

    # Start the main graphical loop for rendering
    root.mainloop()


class Window(Frame):

    # Default dimensions of the game canvas
    WIDTH = 900
    HEIGHT = 600

    # Interval for our main game loop to process at (in milliseconds)
    UPDATE_INTERVAL = 16  # 60 fps

    # The canvas to draw our game components on
    canvas = None

    # Our snake
    snake: Snake = None

    # If the game is running
    running: bool = False

    # The active food on the canvas
    active_food: Food = None

    # The eaten food component
    eaten_food_text: str = None
    eaten_food: int = 0

    # The player's high score for the session
    high_score_text: str = None
    high_score: int = 0

    # The header text (big screen message)
    header_text: str = None

    # The snake parts remaining to add over time
    parts_to_add: int = 0

    master: Tk = None

    def __init__(self, master: Tk = None):
        Frame.__init__(self, master)
        self.master = master
        self.initialize()

    def initialize(self):
        """Initializes our game window and sets up static components"""

        # Basic window setup
        self.master.title("2D Snake")
        self.master.minsize(width=self.WIDTH, height=self.HEIGHT)

        # Set a handler for keyboard
        self.master.bind("<Key>", self.key_pressed)

        # And the following can set the window to fill (wrap around) its contents if we don't have the above set
        self.pack(fill=BOTH, expand=1)

        # Create a canvas to draw the game on
        self.canvas = Canvas(self)

        # Give the canvas some color!
        self.canvas.config(background="#008000")

        # Pack the canvas - expand canvas to edges
        self.canvas.pack(fill=BOTH, expand=1)

        # Create a text box for score keeping
        self.eaten_food_text = self.canvas.create_text(10, 5, text="Score: 0", font=("courier", 20, "bold"), fill="white", anchor=NW)

        # Create the big header text for game instructions
        self.header_text = self.canvas.create_text(440, 200, text="Press Any Key To Play", anchor=N, fill="black", font=("sans-serif", 40, "bold"))

        # Text area for the player's high score
        self.high_score_text = self.canvas.create_text(11, 30, text="High-score: N/A", font=("sans-serif", 10, "normal"), fill="white", anchor=NW)

    def update(self):
        """Define an update function for game updating and continue to schedule itself on an interval"""

        # Only process if player has started the program
        if self.running:
            # Check for overlap with food (yay)
            if overlapping(self.active_food.get_bounds(), self.snake.get_bounds()):
                self.parts_to_add += self.active_food.get_size()
                self.new_food()
                self.eaten_food += 1

            # Add parts to the snake (to "replicate" animation)
            if self.parts_to_add > 0:
                self.parts_to_add -= 1
                self.snake.create_body_part()
            self.snake.move_snake()

            # Check for collisions with walls
            snake_bounds = self.snake.get_bounds()
            if snake_bounds[0] < 0 or snake_bounds[2] > self.winfo_width() or snake_bounds[1] < 0 \
                    or snake_bounds[3] > self.winfo_height():
                self.lose_game()

            # Check for collisions with own body parts
            index = 0
            for part in self.snake.body_parts:
                # TODO calculate proper amount of ignored parts (near head)
                if overlapping(part.get_bounds(), self.snake.get_bounds()) and index > 15:
                    self.lose_game()
                index += 1
        else:
            return

        # Update the player's current score
        self.canvas.itemconfig(self.eaten_food_text, text="Score: " + str(self.eaten_food))

        # Reschedule after updating
        self.after(self.UPDATE_INTERVAL, self.update)

    def key_pressed(self, event):
        """Called when a key is pressed on the keyboard"""
        self.start_game()
        self.snake.change_direction(event.keysym)

    def new_food(self):
        """Creates a new piece of food and randomly places it"""
        if self.active_food:
            self.canvas.delete(self.active_food.component)
        self.active_food = Food(self)

    def start_game(self):
        """Called when the player triggers the start of a game"""
        if not self.running:
            self.eaten_food = 0
            # Make the header text invisible
            self.canvas.itemconfig(self.header_text, state="hidden")

            # Initialize a new snake and construct the first body part (head)
            self.snake = Snake(self)
            self.snake.create_body_part()

            # Set program flag
            self.running = True

            # Make a new food
            self.new_food()

            # Start the updater
            self.update()

    def lose_game(self):
        """Called when the player loses the game (collision with object)"""
        self.canvas.itemconfig(self.header_text, state="normal")
        for part in self.snake.body_parts:
            self.canvas.delete(part.window_component)
        self.running = False
        # Update the player's high-score (if achieved)
        if self.eaten_food > self.high_score:
            self.high_score = self.eaten_food
            self.canvas.itemconfig(self.high_score_text, text="High-score: " + str(self.high_score))


# Initialize the program
main()
