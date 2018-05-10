"""
# main.py
# The main program for 2D snake
# @author Clayton Williams
# @date 5-8-2018
"""

from Tkinter import *
from nodes.Snake import Snake, BodyPart
from nodes.Food import Food


# Checks if two bounds (rectangles) are overlapping
# @param bounds1, bounds2 - list of 4 numbers
# @return boolean - true if they are overlapping
def overlapping(bounds1, bounds2):
    if bounds1[2] >= bounds2[0] and bounds2[2] >= bounds1[0] and bounds1[3] >= bounds2[1] and bounds2[3] >= bounds1[1]:
        return True
    return False


# Main method
def main():

    # Create a new instance of Tkinter
    root = Tk()

    # Create an instance of our custom window class
    app = Window(root)

    # Start the main graphical loop for rendering
    root.mainloop()


# Represents our class for displaying a window (inherits from class Frame)
class Window(Frame):

    # Width of the game canvas
    WIDTH = 900

    # Height of the game canvas
    HEIGHT = 600

    # Our interval to update (16 ms)
    UPDATE_INTERVAL = 16  # 60 fps

    # The canvas to draw our game components on
    canvas = None

    # Our snake
    snake = None

    # If the game is running
    running = False

    # The active food on the canvas
    active_food = None

    # The eaten food component
    eaten_food_text = None
    eaten_food = 0

    # The header text (big screen message)
    header_text = None

    # The snake parts remaining to add over time
    parts_to_add = 0

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.initialize()

    # Initialize our game window
    def initialize(self):
        # Set the title of our program
        self.master.title("2D Snake")

        # Set the window size
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

    # Define an update function for game updating and continue to schedule itself on an interval
    def update(self):
        # Only process if player has started the program
        if self.running:
            # Check for overlap with food (yay)
            if overlapping(self.active_food.getBounds(), self.snake.getBounds()):
                self.new_food()
                self.parts_to_add += 5
                self.eaten_food += 1

            print self.parts_to_add
            if self.parts_to_add > 0:
                self.parts_to_add -= 1
                self.snake.create_body_part()
            self.snake.move_snake()

            # Check for collisions with walls
            snake_bounds = self.snake.getBounds()
            if snake_bounds[0] < 0 or snake_bounds[2] > self.WIDTH or snake_bounds[1] < 0 or snake_bounds[3] > self.HEIGHT:
                self.lose_game()

            # Check for collisions with own body parts
            index = 0
            for part in self.snake.body_parts:
                if overlapping(part.getBounds(), self.snake.getBounds()) and index > 8:  # TODO calculate proper amount
                    self.lose_game()
                index += 1
        else:
            return
        self.canvas.itemconfig(self.eaten_food_text, text="Score: " + str(self.eaten_food))

        # Reschedule after updating
        self.after(self.UPDATE_INTERVAL, self.update)

    # Called when a key is pressed on the keyboard
    def key_pressed(self, event):
        self.start_game()
        self.snake.change_direction(event.keysym)

    # Creates a new piece of food
    def new_food(self):
        if self.active_food:
            self.canvas.delete(self.active_food.component)

        self.active_food = Food(self)

    # Start Game
    def start_game(self):
        if not self.running:
            self.eaten_food = 0
            # Make the header text invisible
            self.canvas.itemconfig(self.header_text, state="hidden")

            self.snake = Snake(self)

            # Make the head
            self.snake.create_body_part()

            self.running = True

            # Make a new food
            self.new_food()

            # Start the updater
            self.update()

    # Called when the player loses the game (collision with object)
    def lose_game(self):
        print "lose"
        self.canvas.itemconfig(self.header_text, state="normal")

        for part in self.snake.body_parts:
            self.canvas.delete(part.window_component)
        self.running = False


# Initialize the program
main()
