import time
import pyktok as pyk
import random as r

from tkinter import *

def download(linkText):
        link = linkText
        
    

        pyk.save_tiktok(link,
                    True)
def downloadData(linkText):
        link = linkText

    

        pyk.save_tiktok(link,
                    True, "data.csv")
   
    
