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
            


final_results()

