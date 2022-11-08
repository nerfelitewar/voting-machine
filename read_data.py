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
                count=count+1
                sleep(0.2)
                print(Fore.YELLOW+x+Fore.RESET)
            sleep(1)
            total_voters=(count//2)-1
            if total_voters==-1 or total_voters==0:
                pg.alert('NO VOTER(S) DATA AVAILABLE ⚠️',title='TOTAL VOTERS')
                exit()
            else:
                print(Fore.LIGHTBLUE_EX+"Total voters-"+Fore.RESET,total_voters)
            pg.alert("PRESS OK FOR RESULTS",title="READ DATA")
            print(Fore.LIGHTGREEN_EX+"***********VOTE DETAILS************"+Fore.RESET)
            sleep(2)
            final_results()



if __name__=='__main__':
    read_data()


  
### https://www.github.com/nerfelitewar 
  
  
