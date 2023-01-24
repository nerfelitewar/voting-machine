import csv
from colorama import Fore
from time import sleep
import pyautogui as pg 
import sys
from read_data import read_data

pg.alert("""1.DO NOT TRY TO RE-VOTE WITH THE SAME DATA.\n
2.CITIZEN SHOULD BE 18 OR ABOVE 18 YEARS.\n
3.YOUR UID SHOULD BE UNIQUE.\n
4.DO NOT EXIT IN BETWEEN THE PROCESS.\n
5.CONTACT YOUR ORGANIZER/HELPER IF STUCK ANYWHERE.\n
6.ENTERED DATA SHOULD BE ACCURATE.
""",title="⚠️NOTE⚠️")

filename=(r"Data\voters_data.csv")
fields=["NAME","AGE","ID","REGION","VOTED TO"]
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)

F_ask_main=pg.confirm('START',title="STARTING...",buttons=["Yes","No"])
if F_ask_main=='No':
    sys.exit(Fore.LIGHTRED_EX+'Good bye! Have a nice day ahead!!'+Fore.RESET)
##      '''''NO CHANGE HERE'''        ##

voted_to=""

sleep(1)

while F_ask_main=='Yes':
    user=pg.prompt("Who are you?",title='IDENTIFICATION')
    age=pg.prompt("Enter your age.",title='YOUR AGE',default=18)
    id_no=pg.prompt("Enter your Identification number",title="UID")
    

    uid_file=open(filename)
    uid_data=uid_file.read()
    if id_no in set(uid_data): #uniqueness of UID 
        pg.alert("SYSTEM CRASHED ⚠️",title="SYSTEM CRASH DUE TO UID CLASH")
        uid_file=open(filename,'a+')
        uid_file.seek(0,2)
        uid_file.write("")
        uid_file.close()
        break 
        
    else:
        pass 



    region=pg.prompt("Where are you from?",title="LOCATION")

    voted_to='' #voted to for csv file 

    pg.alert("Press OK to continue",title="CONTINUE") 
    Ask_main=pg.confirm('SELECT ANY ONE OF THESE',buttons=['START','EXIT'],title='PROCEED NEXT?')
    if Ask_main == "EXIT":
        del_data=pg.confirm("THIS WILL DELETE ALL RECORDS",title="WARNING ⚠️",buttons=["PROCEED","STOP"]) #deleted rec and my data will not be included
        if del_data=="STOP":
            null_file=open(filename,'a+')
            null_file.seek(0,2)
            null_file.close()
            
        elif del_data=="PROCEED":
            null_file=open(filename,'w')
            null_file.seek(0)
            null=''
            null_file.write(null)
            null_file.close()
        
            pg.alert("PROCESS STOPPED...👋")
            sys.exit(Fore.CYAN+"Exiting the process...👋"+Fore.RESET)
    if Ask_main=="START":

       #####################################
        vote_ask=pg.confirm("""1.Bharatiya Janata Party                   
2.Nationalist Congress Party               
3.All India Trinamool Congress             
4.Communist Party of India                 
5.Total Communist Party of India (Marxist) 
6.Indian National Congress                 
7.Skip Vote [Null]""",title="VOTE YOUR PARTY",buttons=[1,2,3,4,5,6,7])

        vote_ask=int(vote_ask)
        parties=['1.Bharatiya Janata Party' ,                  
'2.Nationalist Congress Party' ,             
'3.All India Trinamool Congress' ,            
'4.Communist Party of India'  ,              
'5.Total Communist Party of India (Marxist)' ,
'6.Indian National Congress' ,                
'7.Skip Vote [Null]']

        if vote_ask==1:
            print(Fore.BLUE+f"{str(user)}, you have voted to {parties[vote_ask-1]}"+Fore.RESET)
            voted_to=voted_to.join("BJP")
        if vote_ask==2:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to {parties[vote_ask-1]}"+Fore.RESET)
            voted_to=voted_to.join("NCP")
        if vote_ask==3:
           
            print(Fore.BLUE+f"{str(user)}, you have voted to {parties[vote_ask-1]}"+Fore.RESET)
            voted_to=voted_to.join("AITC")
        if vote_ask==4:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to {parties[vote_ask-1]}"+Fore.RESET)
            voted_to=voted_to.join("CPI")
        if vote_ask==5:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to {parties[vote_ask-1]}"+Fore.RESET)
            voted_to=voted_to.join("C.P.I-M")
        if vote_ask==6:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to {parties[vote_ask-1]}"+Fore.RESET)
            voted_to=voted_to.join('INC')
        if vote_ask==7:
            
            print(Fore.BLUE+f"{str(user)}, you have voted to {parties[vote_ask-1]}"+Fore.RESET)
            voted_to=voted_to.join('SKIPPED')
        
        rows=[user,age,id_no,region,voted_to] 
        with open(filename,'a') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(rows)


    F_ask_main=pg.confirm('NEW USER?',title='NEW PERSON',buttons=['Yes','No'])
    if F_ask_main=='No':
        pass
        

res=pg.confirm('SHOW VOTE RESULTS',title='VOTE RESULTS',buttons=['YES','NO','MAYBE'])
if res=='YES':
    read_data()
if res=='NO':
    sys.exit(Fore.MAGENTA+"Good Bye! Have a nice day!!👋"+Fore.RESET)
if res=='MAYBE':
    pg.alert('To see vote results go to "read_data.py" file!',title='WANNA SEE RESULTS?')
exit()
    
### https://www.github.com/nerfelitewar

