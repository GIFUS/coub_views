import os
import random
import string
import threading
import time
from queue import Queue
import platform
import requests

intro = """
----------------------------------------------------------------------------

 ██████╗ ██████╗ ██╗   ██╗██████╗     ██╗   ██╗██╗███████╗██╗    ██╗███████╗
██╔════╝██╔═══██╗██║   ██║██╔══██╗    ██║   ██║██║██╔════╝██║    ██║██╔════╝
██║     ██║   ██║██║   ██║██████╔╝    ██║   ██║██║█████╗  ██║ █╗ ██║███████╗
██║     ██║   ██║██║   ██║██╔══██╗    ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║╚════██║
╚██████╗╚██████╔╝╚██████╔╝██████╔╝     ╚████╔╝ ██║███████╗╚███╔███╔╝███████║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝       ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝

---------------------------------[by GIFUS]---------------------------------
"""

print(intro)

proxy_loading = input("[1] Load Proxys from APIs\n[2] Load Proxys from proxys.txt\nOption: ")
uid = input("Coub id: ")
class main(object):
    def __init__(self):
        self.combolist = Queue()
        self.Writeing = Queue()
        self.printing = []
        self.botted = 0
        self.combolen = self.combolist.qsize()

    def printservice(self): #print screen
        while True:
            if True:
                if platform.system() == "Windows":
                    clear = "cls"
                else:
                    clear = "clear"
                os.system(clear)
                print(intro)
                print(
                    f"                                  Viewed:{self.botted}\n")
                for i in range(len(self.printing) - 10, len(self.printing)):
                    try:
                        print(self.printing[i])
                    except (ValueError, Exception):
                        pass
                time.sleep(0.5)
a = main()
class proxy():
    global proxy_loading
    def update(self):
        global pupd
        pupd = 0
        while True:

            if proxy_loading == "2":
                data = ''
                data = open("proxys.txt", "r").read()
                self.splited += data.split("\n") #scraping and splitting proxies
            else:
                data = ''
                urls = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt","https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes","https://www.proxy-list.download/api/v1/get?type=https&anon=elite"]
                for url in urls:
                    try:
                        data += requests.get(url).text
                        self.splited += data.split("\n")
                        self.splited = [s.replace('\r', "") for s in self.splited]
                    except:
                        print("Proxy loading error!")
                        pass
            pupd = pupd+1
            time.sleep(300)

    def get_proxy(self):
        random1 = random.choice(self.splited)
        return random1
    def FormatProxy(self):
	    proxyOutput = {'https' :'https://'+self.get_proxy()}
	    return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)

proxy1 = proxy()
def bot():
    while True:
        try:
            s = requests.session()
            random_proxy = proxy1.FormatProxy()

            data={
            "player":"html5",
            "type": "site",
            "platform":"desktop"
            }

            headers={
            "cookie": '',
            "user-agent": f'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/{(random.random() * 600)}.36 (KHTML, like Gecko) Chrome/{(random.random() * 59)}.0.3029.110 Safari/${(random.random() * 1000)}.36',
            "sec-fetch-mode": "cors",
            "referer": "https://coub_suck_dick.com",
            "X-Requested-With": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded"
            }

            for x in range(10):
                s.post(f"https://coub.com/coubs/"+uid+"/increment_views?player=html5&type=site&platform=desktop",headers=headers,data=data,proxies=random_proxy,timeout=1)

            s.close()

            a.botted += 1
            pass
        except:
            pass




maxthreads = int(input("Threads (Recommended: 500 | Max: 1000): "))

threading.Thread(target=a.printservice).start()
num = 0
while num < maxthreads :
    num += 1
    threading.Thread(target=bot).start()


threading.Thread(target=bot).start()
