import time
from datetime import datetime as dt

hosts_temp = "hosts"
host_path = "/etc/hosts"
redirect = "127.0.0.1"
blocked_websites = ["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]


while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17)):
        print("Working hours...")
        with open(host_path,"r+") as file:
            content = file.read()
            print(content)
            for websites in blocked_websites:
                if websites in content:
                    pass
                else:
                    file.write(redirect+ "  "+websites+"\n")
    else:
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(websites in line for websites in blocked_websites):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
