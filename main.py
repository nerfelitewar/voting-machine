import csv
from colorama import Fore
from time import sleep
import pyautogui as pg 
import sys


filename=(r"Data\voters_data.csv")
fields=["NAME","AGE","ID","REGION","VOTED TO"]
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)

F_ask_main=pg.confirm('Start',title="STARTING...",buttons=["Yes","No"])
voted_to=""

sleep(1)

'''''NO CHANGE HERE'''

while F_ask_main=='Yes':
    user=pg.prompt("Who are you?",title='IDENTIFICATION')
    age=pg.prompt("Enter your age.",title='YOUR AGE',default=18)
    id_no=pg.prompt("Enter your Identification number",title="UID")
    region=pg.prompt("Where are you from?",title="Location")
    voted_to=''

    pg.alert("Press OK to continue",title="CONTINUE") 
    Ask_main=int(input(Fore.RED+"""
    1. Start the process\n
    2. Exit
    -----------------

    """+Fore.RESET))
    if Ask_main == 2:
        sys.exit(Fore.CYAN+"Exiting the process..."+Fore.RESET)
    if Ask_main==1:
       #####################################
        vote_ask=int(input(Fore.GREEN+"""
            1.Bharatiya Janata Party 
            2.Nationalist Congress Party
            3.All India Trinamool Congress
            4.Communist Party of India
            5.Total Communist Party of India (Marxist)
            6.Indian National Congress 
            7.Skip Vote [Null]
        """+Fore.RESET))

        if vote_ask==1:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to".format(user)+Fore.RESET,vote_ask)
            voted_to=voted_to.join("BJP")
        if vote_ask==2:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to".format(user)+Fore.RESET,vote_ask)
            voted_to=voted_to.join("NCP")
        if vote_ask==3:
           
            print(Fore.BLUE+f"{str(user)}, you have voted to".format(user)+Fore.RESET,vote_ask)
            voted_to=voted_to.join("AITC")
        if vote_ask==4:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to".format(user)+Fore.RESET,vote_ask)
            voted_to=voted_to.join("CPI")
        if vote_ask==5:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to".format(user)+Fore.RESET,vote_ask)
            voted_to=voted_to.join("C.P.I-M")
        if vote_ask==6:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to".format(user)+Fore.RESET,vote_ask)
            voted_to=voted_to.join('INC')
        if vote_ask==7:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to".format(user)+Fore.RESET,vote_ask)
            voted_to=voted_to.join('SKIPPED')
        
        rows=[user,age,id_no,region,voted_to] 
        with open(filename,'a') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(rows)


    F_ask_main=pg.confirm('New User?',title='NEW PERSON',buttons=['Yes','No'])
    if F_ask_main=='No':
        print(Fore.MAGENTA+"Good Bye! Have a nice day👋"+Fore.RESET)
        exit()
    
### https://www.github.com/nerfelitewar

