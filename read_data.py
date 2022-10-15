from colorama import Fore 
from function_result import final_results
from time import sleep 
import pyautogui as pg 

def read_data():
    filename=(r"Data\voters_data.csv")
    with open(filename) as csvfile:
            csvfile.seek(0)
            count=0
            for x in csvfile.readlines():
                lst=[]
                lst.append(x)

                count=count+1
                sleep(0.3)
                print(Fore.YELLOW+x+Fore.RESET)
            sleep(1)
            print(Fore.LIGHTBLUE_EX+"Total voters-"+Fore.RESET,(count//2)-1)

read_data()
pg.alert("PRESS OK FOR RESULTS",title="READ DATA")
print(Fore.LIGHTGREEN_EX+"***********VOTE DETAILS************"+Fore.RESET)
sleep(2)
final_results()


  
### https://www.github.com/nerfelitewar 
  
  
