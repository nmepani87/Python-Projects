import tkinter as tk
from tkinter import *
import webbrowser
import os

# creating class to display tkinter window
class ParentWindow(Frame):
    # defining function, open tkinter window and inputs given
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        # creating object to accept user input
        self.varCustom = StringVar()
        
        #creating a label and displaying via grid input in tkinter
        self.lblentertxt = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lblentertxt.grid(row=0, column=0, padx=(20,20), pady=(20,20))

        #creating an entrybox for user to write text for custompage and displaying via grid input in tkinter
        self.custom_entry = Entry(self.master, text=self.varCustom, width=110)
        self.custom_entry.grid(row=1, column=0, columnspan=6, padx=(0,0), pady=(0,10))

        #creating a button and displaying via grid input in tkinter and giving it a method to do upon it being pressed
        self.default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default.grid(row=2, column=2, padx=(10,5), pady=(10,10))

        #creating a button and displaying via grid input in tkinter and giving it a method to do upon it being pressed
        self.customtxt = Button(text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.customtxt.grid(row=2, column=4, padx=(10,20), pady=(10,10))
        
    # defining function that is called when user presses default page button
    def defaultHTML(self):
        # putting string into an object
        htmlText = "Stay tuned for our amazing summer sale!"
        # 'opening' html file specified so it can be editing, if it doesn't exist it will be creating
        htmlFile = open("index.html", "w")
        # setting what code is to be written into the file
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # writting in the code into the file
        htmlFile.write(htmlContent)
        # 'closing' file that was opened for editing
        htmlFile.close()
        # getting the web browser to open html file in new tab in default web browser
        webbrowser.open_new_tab('file://' + os.path.realpath("index.html"))

    # defining function that is called when user presses custom button
    def customHTML(self):
        # getting data within entrybox
        htmlCustomText = self.varCustom.get()
        # turning data from entrybox into string format
        htmlText = str(htmlCustomText)
        # 'opening' html file specified so it can be editing, if it doesn't exist it will be creating
        htmlFile = open("custom_index.html", "w")
        # setting what code is to be written into the file
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # writting in the code into the file
        htmlFile.write(htmlContent)
        # 'closing' file that was opened for editing
        htmlFile.close()
        # getting the web browser to open html file in new tab in default web browser
        webbrowser.open_new_tab('file://' + os.path.realpath("custom_index.html"))
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
