from colorama import Fore 


def read_data():
    filename=(r"C:\MY CODING WORKSPACE\School_Project\Data\votes.csv")
    with open(filename) as csvfile:
            csvfile.seek(0)
            count=0
            for x in csvfile.readlines():
                lst=[]
                lst.append(x)

                count=count+1
                print(Fore.YELLOW+x+Fore.RESET)
            print(Fore.LIGHTBLUE_EX+"Total voters-"+Fore.RESET,count//2)
read_data()

  
  
  
  
