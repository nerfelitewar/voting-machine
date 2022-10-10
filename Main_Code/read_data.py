import csv
import pyautogui as pg
from time import sleep
from colorama import Fore 


filename=(r"C:\MY CODING WORKSPACE\School_Project\Data\votes.csv")
with open(filename) as csvfile:
    csvwriter = csv.reader(csvfile)
    for data in csvfile:
        csvfile.seek(0) 
        for x in csvfile.readlines():
            print(x)
        #print(x)
       
    

  
  
  
  
