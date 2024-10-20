
import download
from tkinter import *
import tkinter as tk
from tkinter import LabelFrame, Label, Button, StringVar, messagebox
import main
import webview
import os 
import subprocess

size = "500x550"
title = "TT Video Downloader"

root = Tk()
class GUII():
    


    def __init__(self,root):
        self.initUI(root) 

    def initUI(self,root):
        root.geometry(size)
        root.title(title)

    def RunDataBtn():


        link = GUII.linkText.get(1.0,"end-1c")

        try:
            if GUII.linkText.get(1.0,"end-1c") == "":
                GUII.PopUpWarning()
                return
            else:
                download.downloadData(link)
                
                tk.messagebox.showinfo("Succesfully Downloaded",f"Video downloaded from TT: {link}")
        except Exception as e:

            tk.messagebox.showerror("Warning",str(e) + "\n This link is invalid. Please try again with a different link")


    
    def RunText():
        link = GUII.linkText.get(1.0,"end-1c")

        try:
            if GUII.linkText.get(1.0,"end-1c") == "":
                GUII.PopUpWarning()
                return
            else:
                download.download(link)
                
                
                tk.messagebox.showinfo("Succesfully Downloaded",f"Video downloaded from TT: {link}")

        except Exception as e:

            tk.messagebox.showerror("Warning",str(e) + "\n This link is invalid. Please try again with a different link")
    def PopUpWarning():
        tk.messagebox.showerror("Warning",  "Please Enter a TT URL to download")
       
    def ShowLink():
        
        link = GUII.linkText.get(1.0,"end-1c")
        # if link does not include https://www.tiktok.com/ else use ""
        
      


        if link.startswith("https://www.tiktok.com/"):
            webview.create_window("Link",link)
            webview.start()
        else:
            tk.messagebox.showerror("Warning",  "Please Enter a TT URL to view")


    def open_root_folder():
    # Get the current working directory (root folder of the script)
        root_folder = os.getcwd()

        try:
            # Open the folder in file explorer
            if os.name == 'nt':  # For Windows
                subprocess.Popen(f'explorer "{root_folder}"')
            elif os.name == 'posix':  # For MacOS and Linux
                subprocess.Popen(['open', root_folder] if sys.platform == 'darwin' else ['xdg-open', root_folder])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open folder: {e}")

    
    text_var = StringVar()
    text_var.set("Enter TT Link")
    label = Label(root, 
                textvariable=text_var, 
                anchor=tk.CENTER,       
                
                height=3,               
                bd=3,                  
                font=("Arial", 16, "bold"), 

                underline=0,           
                )


    label.pack(pady=20)
    
    open_button = tk.Button(root, text="Open Root Folder", command=open_root_folder)
    open_button.pack(pady=20)
    linkText = Text(root, height = 5)
    linkText.pack()

    linkText.insert(END, "")


    # Create button widget from tkinter
    buttonDownload = Button(root, 
                    text="Download Video", 
                    command=RunText,
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",)

    buttonDownload.pack(padx=20, pady=20)   

    buttonWithData = Button(root, 
                    text="Download Video With Data",   
                    command=RunDataBtn, 
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",)

    buttonWithData.pack(padx=20, pady=20)  

    buttonShowLink = Button(root, 
                    text="Go To Video",    
                    command=ShowLink, 
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",)

    buttonShowLink.pack(padx=20, pady=20)  

