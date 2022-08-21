import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import os.path, time
import shutil
import datetime


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Set title of GUI window
        self.master.title("File Transfer")

        # create buttons to select files from source
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # position source button in GUI using grid()
        self.sourceDir_btn.grid(row=0, column= 0, padx=(20, 10), pady=(30, 0))
        #create entry for source directory selection
        self.source_dir = Entry(width=75)
        # position entry in GUI using grid() padx & pady same as button to line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        # create button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # position source button in GUI using grid()
        self.destDir_btn.grid(row=1, column= 0, padx=(20, 10), pady=(15, 10))
        #create entry for source directory selection
        self.destination_dir = Entry(width=75)
        # position entry in GUI using grid() padx & pady same as button to line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15, 10))

        # create button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # position transfer file button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # create exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # the .delete(0, END) will clear the cotent that is inserted in the Entry widget,
        # this allows the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        # .insert method will insert the user selection to the source_dir Entry widget
        self.source_dir.insert(0, selectSourceDir)
        return selectSourceDir
        


    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        # the .delete(0, END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the entry widget properly
        self.destination_dir.delete(0, END)
        # .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)
        
        

    # create function to transfer files from one directory to another
    def transferFiles(self):
        # gets source directory
        source = self.source_dir.get()
        # get destination directory
        destination = self.destination_dir.get()
        # gets list of files in the source directory
        source_files = os.listdir(source)
        # getting the current time
        currentTime = datetime.datetime.now()
        # subtracting 24hrs from current time to use for our comparision
        dayEarlier = currentTime - datetime.timedelta(hours=24)        
        # checking root, dirs and files in specified directory
        for root,dirs,files in os.walk(source):
            for file_name in source_files:
                # setting joining directory to filename
                path = os.path.join(root,file_name)
                # getting status of path object
                st = os.stat(path)
                # finding time when files last modified
                mod_time = datetime.datetime.fromtimestamp(st.st_mtime)
                # if statement to compare file modified time to 24hr earlier of current time
                if mod_time > dayEarlier:
                    # where to move file to if if condition satisfied
                    shutil.move(os.path.join(root, file_name), destination)
                    # printing which files moved over to let user know
                    print(file_name, "moved successfully as it was last modified/created less than 24hrs ago")



    # create function to exit program
    def exit_program(self):
        # root in the main GUI window, the tkinter destroy method
        # tells python to terminate root.mainloop and all widgets inside GUI window
        root.destroy()


    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
