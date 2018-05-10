"""
# main.py
# The main program for 2D snake
# @author Clayton Williams
# @date 5-8-2018
"""

from Tkinter import *
from nodes.Snake import Snake, BodyPart
from nodes.Food import Food


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

    # Our interval to update (16 ms)
    UPDATE_INTERVAL = 16  # 60 fps

    # The canvas to draw our game components on
    canvas = None

    # Our snake
    snake = None

    # If the game is started yet
    started = False

    # The active food on the canvas
    active_food = None

    # The eaten food component
    eaten_food_text = None
    eaten_food = 0

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.snake = Snake(self)
        self.initialize()

        # Make a new food
        self.new_food()

        # Make the head
        self.snake.create_body_part()

        # Start the updater
        self.update()

    # Initialize our game window
    def initialize(self):
        # Set the title of our program
        self.master.title("2D Snake")

        # Set the window size
        self.master.minsize(width=900, height=600)

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

    # Define an update function for game updating and continue to schedule itself on an interval
    def update(self):

        if self.started:
            if self.active_food.can_eat(self.snake):
                self.new_food()
                self.snake.create_body_part()
                self.eaten_food += 1
            self.snake.move_snake()

        self.canvas.itemconfig(self.eaten_food_text, text="Score: " + str(self.eaten_food))

        # Reschedule after updating
        self.after(self.UPDATE_INTERVAL, self.update)

    # Called when a key is pressed on the keyboard
    def key_pressed(self, event):
        self.started = True
        self.snake.change_direction(event.keysym)

    # Creates a new piece of food
    def new_food(self):
        if self.active_food:
            self.canvas.delete(self.active_food.component)

        self.active_food = Food(self)


# Initialize the program
main()
