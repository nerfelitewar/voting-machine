# VOTING MACHINE

## DUE DATE! 14-10-22, today 9/10/22
import csv
from colorama import Fore
import time
import pyautogui as pg 
import sys #will be used to flush buffer data 



#MaxVoteParty,Max_Votes=0,
filename=(r"C:\MY CODING WORKSPACE\School_Project\Data\votes.csv")

#fields=["NAME","AGE","ID","REGION","VOTED TO"]

user=pg.prompt("Who are you?",title='IDENTIFICATION')
age=pg.prompt("Enter your age.",title='YOUR AGE',default=18)
id_no=pg.prompt("Enter your Identification number",title="UID")
region=pg.prompt("Where are you from?",title="Location")
str(user)
str(age)
str(id_no)
str(region)
voted_to=''

#rows=[user,age,id_no,region,voted_to]



time.sleep(1)

F_ask_main=pg.confirm('Start',title="STARTING...",buttons=["Yes","No"])
while F_ask_main=='Yes':

    Ask_main=int(input(Fore.RED+"""
    1. Start voting\n
    2. Show result \n
    3. Exit
    -----------------

    """+Fore.RESET))
    if Ask_main == 3:
        exit()

    if Ask_main==1:
        BJP=0
        NCP=0
        AITC=0
        CPI=0
        CPI_M=0
        SKIP_VOTERS=0
        Total_voters=BJP+NCP+AITC+CPI+CPI_M+SKIP_VOTERS
        #####################################
        vote_ask=int(input(Fore.GREEN+"""
            1.BJP 
            2.NCP
            3.ALL INDIA TRINAMOOL CONGRESS 
            4.CPI 
            5.CPI-M
            6.Skip Vote [Null]
        """+Fore.RESET))
        vote_ask=pg.confirm('Choose your party',title='CHOOSE')

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
            voted_to=voted_to.join("NO VOTE [SKIPPED]")
        
        
        
        



        fields=["NAME","AGE","ID","REGION","VOTED TO"]
        rows=[user,age,id_no,region,voted_to]
        with open(filename,'w') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)









































    C_ask_main=pg.confirm('Want to do again?',title='Again',buttons=['Yes','No'])
    if C_ask_main=='No':
         print(Fore.BLUE+"Good Bye! Have a nice day👋"+Fore.RESET)
         exit()
    

