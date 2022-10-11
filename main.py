# VOTING MACHINE

## DUE DATE! 14-10-22, today 11/10/22
import csv
from colorama import Fore
from time import sleep
import pyautogui as pg 
import sys
from read_data import read_data 


filename=(r"C:\MY CODING WORKSPACE\School_Project\Data\votes.csv")
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
    1. Start voting\n
    2. Show result \n 
    3. Exit
    -----------------

    """+Fore.RESET))
    if Ask_main == 3:
        sys.exit()
    if Ask_main==1:
        BJP=0
        NCP=0
        AITC=0
        CPI=0
        CPI_M=0
        SKIP_VOTERS=0
        #####################################
        vote_ask=int(input(Fore.GREEN+"""
            1.BJP 
            2.NCP
            3.ALL INDIA TRINAMOOL CONGRESS 
            4.CPI 
            5.CPI-M
            6.Skip Vote [Null]
        """+Fore.RESET))

        if vote_ask==1:
            BJP+=1
            voted_to=voted_to.join("BJP")
        if vote_ask==2:
            NCP+=1
            voted_to=voted_to.join("NCP")
        if vote_ask==3:
            AITC+=1
            voted_to=voted_to.join("AITC")
        if vote_ask==4:
            CPI+=1
            voted_to=voted_to.join("CPI")
        if vote_ask==5:
            CPI_M+=1
            voted_to=voted_to.join("CPI-M")
        if vote_ask==6:
            SKIP_VOTERS+=1
            voted_to=voted_to.join('SKIPPED')
        if Ask_main==2:
            read_data() 
        rows=[user,age,id_no,region,voted_to] 
        with open(filename,'a') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(rows)


    F_ask_main=pg.confirm('New User?',title='NEW PERSON',buttons=['Yes','No'])
    if F_ask_main=='No':
        print(Fore.BLUE+"Good Bye! Have a nice day👋"+Fore.RESET)
        exit()
    
    

