"""
# main.py
# The main program for 2D snake
# @author Clayton Williams
# @date 5-8-2018
"""

from Tkinter import *


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

    # Our interval to update (100 ms)
    UPDATE_INTERVAL = 100

    # The canvas to draw our game components on
    canvas = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.initialize()
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

        # Pack the canvas
        self.canvas.pack(fill=BOTH, expand=1)

    # Define an update function for game updating and continue to schedule itself on an interval
    def update(self):

        # Reschedule after updating
        self.after(self.UPDATE_INTERVAL, self.update)

    # Called when a key is pressed on the keyboard
    def key_pressed(self, event):
        print "pressed", event.keysym


# Initialize the program
main()
