import requests
from termcolor import cprint
cprint("""

____ ____ _  _ ____ ____ ____ ____    _ ___     _    ____ ____ _  _ _  _ ___  
|__/ |___ |  | |___ |__/ [__  |___    | |__]    |    |  | |  | |_/  |  | |__] 
|  \ |___  \/  |___ |  \ ___] |___    | |       |___ |__| |__| | \_ |__| |    


""", 'white')
try:
    inp = input("Enter Server IP : ")
    url = ("https://api.hackertarget.com/reverseiplookup/?q=")
    re = requests.get(url + inp)
    tex = re.text
    with open('url.txt', 'a') as w:
        w.write(tex + "\n")
    print("*" * 78)
    cprint(" See in your Folder This TEXT (Url.txt) ... ", 'blue')
    print("*"*78)
except NameError:
    print("There is a Problem, try again")
