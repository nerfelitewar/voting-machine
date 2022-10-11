import csv
from time import sleep
from colorama import Fore 


def read_data():
    filename=(r"C:\MY CODING WORKSPACE\School_Project\Data\votes.csv")
    with open(filename) as csvfile:
            csvfile.seek(0)
            for x in csvfile.readlines():
                print(x)
read_data()
       
    

  
  
  
  
