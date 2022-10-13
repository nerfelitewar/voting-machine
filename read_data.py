from colorama import Fore 
from function_result import final_results

def read_data():
    filename=(r"Data\voters_data.csv")
    with open(filename) as csvfile:
            csvfile.seek(0)
            count=0
            for x in csvfile.readlines():
                lst=[]
                lst.append(x)

                count=count+1
                print(Fore.YELLOW+x+Fore.RESET)
            print(Fore.LIGHTBLUE_EX+"Total voters-"+Fore.RESET,(count//2)-1)

read_data()

final_results()


  
  
  
  
