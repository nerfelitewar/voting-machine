from time import sleep
from colorama import Fore
def final_results():
    filename=(r"Data\voters_data.csv")
    with open(filename) as csvfile:
            res = "\n".join(csvfile.readlines())
            print(Fore.LIGHTMAGENTA_EX+"Total Bharatiya Janata Party voters"+Fore.LIGHTRED_EX+ "[BJP]-"+Fore.RESET,res.count("BJP"))
            print(Fore.LIGHTMAGENTA_EX+"Total Indian National Congress voters"+Fore.LIGHTRED_EX+ "[INC]-"+Fore.RESET,res.count("INC"))
            print(Fore.LIGHTMAGENTA_EX+"Total Nationalist Congress Party voters"+Fore.LIGHTRED_EX+ "[NCP]-"+Fore.RESET,res.count("NCP"))
            print(Fore.LIGHTMAGENTA_EX+"Total Trinamool Congress voters"+Fore.LIGHTRED_EX+ "[AITC]-"+Fore.RESET,res.count("AITC"))
            print(Fore.LIGHTMAGENTA_EX+"Total Communist Party of India voters"+Fore.LIGHTRED_EX+ "[CPI]-"+Fore.RESET,res.count("CPI"))
            print(Fore.LIGHTMAGENTA_EX+"Total Communist Party of India (Marxist) voters"+Fore.LIGHTRED_EX+ "[CPI-M]-"+Fore.RESET,res.count("C.P.I-M"))
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
            if high==high:
                for high in lst:
                    clash=lst.count(high)
                    str(clash)

                print(Fore.LIGHTRED_EX+str(clash)+Fore.LIGHTCYAN_EX+  " ⚠️ Vote clashed please re-evalute manually or reconduct vote ⚠️ "+Fore.RESET)
            



if __name__=="__main__":
    final_results()

### https://www.github.com/nerfelitewar