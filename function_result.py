from time import sleep
from colorama import Fore
def final_results():
    filename=(r"Data\voters_data.csv")
    with open(filename) as csvfile:
            res = "\n".join(csvfile.readlines())
            print(Fore.LIGHTMAGENTA_EX+"Total Bharatiya Janata Party voters"+Fore.LIGHTRED_EX+ "[BJP]-"+Fore.RESET,res.count("BJP"))
            sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX+"Total Indian National Congress voters"+Fore.LIGHTRED_EX+ "[INC]-"+Fore.RESET,res.count("INC"))
            sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX+"Total Nationalist Congress Party voters"+Fore.LIGHTRED_EX+ "[NCP]-"+Fore.RESET,res.count("NCP"))
            sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX+"Total Trinamool Congress voters"+Fore.LIGHTRED_EX+ "[AITC]-"+Fore.RESET,res.count("AITC"))
            sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX+"Total Communist Party of India voters"+Fore.LIGHTRED_EX+ "[CPI]-"+Fore.RESET,res.count("CPI"))
            sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX+"Total Communist Party of India (Marxist) voters"+Fore.LIGHTRED_EX+ "[CPI-M]-"+Fore.RESET,res.count("C.P.I-M"))
            sleep(0.5)
            print(Fore.LIGHTMAGENTA_EX+"Total Skip voters"+Fore.LIGHTRED_EX+ "[NULL]-"+Fore.RESET,res.count("SKIPPED"))
            sleep(1)
            lst=[res.count("BJP"),res.count("INC"),
res.count("NCP"),
res.count("AITC"),
res.count("CPI"),
res.count("C.P.I-M"),
res.count("SKIPPED")]


            high=Fore.LIGHTYELLOW_EX+"Higest vote- "+Fore.RESET+str(max(lst))
            print(high)
            sleep(0.5)
            print(Fore.LIGHTYELLOW_EX+"Lowest vote-"+Fore.RESET+str(min(lst)))
            sleep(1)
            clash=lst.count(max(lst))
            if clash!=1:
                str(clash)
                print(Fore.LIGHTRED_EX+str(clash)+Fore.LIGHTCYAN_EX+  " ⚠️ Vote clashed please re-evalute manually or reconduct vote ⚠️ "+Fore.RESET)
            if  res.count("BJP")==max(lst):
                print(Fore.LIGHTBLUE_EX+"Winner is BJP party"+Fore.RESET)
            if  res.count("INC")==max(lst):
                print(Fore.LIGHTBLUE_EX+"Winner is INC party"+Fore.RESET)
            if  res.count("NCP")==max(lst):
                print(Fore.LIGHTBLUE_EX+"Winner is NCP party"+Fore.RESET)
            if  res.count("AITC")==max(lst):
                print(Fore.LIGHTBLUE_EX+"Winner is AITC party"+Fore.RESET)
            if  res.count("CPI")==max(lst):
                print(Fore.LIGHTBLUE_EX+"Winner is CPI party"+Fore.RESET)
            if  res.count("C.P.I-M")==max(lst):
                print(Fore.LIGHTBLUE_EX+"Winner is CPI-M party"+Fore.RESET)
            if  res.count("SKIPPED")==max(lst):
                print(Fore.LIGHTBLUE_EX+"Many people choose to SKIP vote"+Fore.RESET)
            sort_lst=sorted(lst,reverse=True)
            if res.count("SKIPPED")==max(lst):
                if res.count("BJP")==sort_lst[1]:
                    print(Fore.LIGHTGREEN_EX+"Next winner to be considered should be, BJP"+Fore.RESET)

            if res.count("SKIPPED")==max(lst):
                if res.count("INC")==sort_lst[1]:
                    print(Fore.LIGHTGREEN_EX+"Next winner to be considered should be, INC"+Fore.RESET)

            if res.count("SKIPPED")==max(lst):
                if res.count("NCP")==sort_lst[1]:
                    print(Fore.LIGHTGREEN_EX+"Next winner to be considered should be, NCP"+Fore.RESET)

            if res.count("SKIPPED")==max(lst):
                if res.count("AITC")==sort_lst[1]:
                    print(Fore.LIGHTGREEN_EX+"Next winner to be considered should be, AITC"+Fore.RESET)

            if res.count("SKIPPED")==max(lst):
                if res.count("CPI")==sort_lst[1]:
                    print(Fore.LIGHTGREEN_EX+"Next winner to be considered should be, CPI"+Fore.RESET)

            if res.count("SKIPPED")==max(lst):
                if res.count("C.P.I-M")==sort_lst[1]:
                    print(Fore.LIGHTGREEN_EX+"Next winner to be considered should be, CPI-M"+Fore.RESET)


if __name__=="__main__":
    final_results()

### https://www.github.com/nerfelitewar