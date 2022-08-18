# Python Ver:       3.10.6
#
# Author:           Nilesh Mepani
#
# Purpose:          Phonebook demo. Demonstrating OOP, Tkinter GUI module,
#                   using Tkinter Parent and Child relationships.
#
# Tested OS:        This code was written and tested to work with macOS 12

from tkinter import *
from tkinter import messagebox
import tkinter as tk


# Be sure to import our other modules
# so we can have access to them
import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(700,500) #Height,Width
        self.master.maxsize(700,500)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,700,500)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on the macOS
        self.master.protocol("WX_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping the code comparmentalized and cluster free
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
