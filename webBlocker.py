import time
from datetime import datetime as dnt
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
sites_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
while True:
    if dnt(dnt.now().year,dnt.now().month,dnt.now().day,9)<=dnt.now()<=dnt(dnt.now().year,dnt.now().month,dnt.now().day,17):
        with open(hosts_path,'r+') as file:
            content=file.read()
            for site in sites_list:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
        print("WORKING HOURS")
    else:
        print("FUN HOURS")
    time.sleep(5)
