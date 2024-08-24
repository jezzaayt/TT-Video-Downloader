
from tkinter import LabelFrame, Label, Button, StringVar, messagebox
import download
from tkinter import *
import tkinter as tk
from tkinter import LabelFrame, Label, Button, StringVar, messagebox
import main

root = Tk()
class GUII():
    
  

    def __init__(self,root):
        self.initUI(root) 

    def initUI(self,root):
        root.geometry("400x400")
        root.title("TT Video Downloader")

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
   

