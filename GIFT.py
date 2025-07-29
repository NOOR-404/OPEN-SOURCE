"""
----------------------------------------------------------------------------
~/ THIS SCRIPT CREATE BY NOOR X IMRAN
~/ FOR EID GIFT
~/ CREATE DATE : 19 MARCH 2025
~/ LAST UPDATE : 2025
----------------------------------------------------------------------------
"""
#__________/-MODULE-\__________#
import os,time,sys,requests,uuid,json
from os import system
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#__________/-COLOR-\__________#
G="\033[1;92m"
W="\x1b[38;5;15m"
B="\033[1;34m"
Y="\x1b[38;5;226m"
A="\x1b[38;5;123m"
R="\33[1;91m"
O="\x1b[38;5;81m"
X="\x1b[38;5;205m"
P="\033[0;34m"
#__________/-SYTLE-\__________#
xr = f"{G}>{R}>{G}>{W}"
xrx = f"{G}>{R}??{G}<{W}"
xr1 = f"{G}>{R}1{G}<{W}"
xr2 = f"{G}>{R}2{G}<{W}"
xr0 = f"{G}>{R}0{G}<{W}"
#__________/-LOGO-\__________#
logo = (f"""
{R}     ▗▄▄▄▖▗▄▄▄▖▗▄▄▄   ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖
{W}     ▐▌     █  ▐▌  █ ▐▌     █  ▐▌     █  
{W}     ▐▛▀▀▘  █  ▐▌  █ ▐▌▝▜▌  █  ▐▛▀▀▘  █  
{R}     ▐▙▄▄▖▗▄█▄▖▐▙▄▄▀ ▝▚▄▞▘▗▄█▄▖▐▌     █ {W}V{R}/{W}GIFT
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{xr} DEVELOPER {xr} {R}_{W}NOOR X IMRAN{R}_
{xr} TOOLS     {xr} {R}_{W}FILE CLONING{R}_
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________/-SELF-\__________#
class __giftX__:
    def __init__(self):
        self.loop = 0
        self.plist = []
        self.oks = []
        self.cps = []
        self.twf = []
#__________/-CLEAR-\__________#
    def __clearX__(self):
    	system('clear');print(logo)
#__________/-LINE-\__________#
    def __lineX__(self):
    	print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________/-MAIN-MENU-\__________#
    def __meNu__(self):
    	self.__clearX__()
    	print(f"{xr1} FILE CLONING ")
    	print(f"{xr0} EXIT TOOLS ")
    	self.__lineX__()
    	__menU__ = input(f"{xrx} INPUT MENU {xr} ")
    	if __menU__ == ("1"):self.__fileX__()
    	elif __menU__ == ("0"):print(f"{xr} THANKS FOR USING.....! ")
    	else:
    	    self.__lineX__()
    	    print(f"{xr} OPTION NOT FOUND....! ")
    	    time.sleep(1);self.__meNu__()
#__________/-FILE-MENU-\__________#
    def __fileX__(self):
    	self.__clearX__()
    	print(f"{xr} EXAMPLE   {xr} /sdcard/GIFT.txt")
    	self.__lineX__()
    	__fileC__ = input(f"{xr} INPUT FILE {xr} ")
    	try:
    	    __fileL__ = open(__fileC__,'r').read().splitlines()
    	except FileNotFoundError:
    	    self.__lineX__()
    	    print(f"{xr} FILE NOT FOUND....! ")
    	    time.sleep(1);self.__fileX__()
    	self.__clearX__()
    	print(f"{xr} METHOD{R}-{W}1 {G}>{W}GRAPH{G}<{W} ")
    	print(f"{xr} METHOD{R}-{W}2 {G}>{W}B-GRAPH{G}<{W} ")
    	self.__lineX__()
    	__methodX__ = input(f"{xr} INPUT METHOD {xr} ")
    	self.__clearX__()
    	print(f"{xr} AUTO PASSWORD {G}>{W}20{R}-{W}PASS{G}<{W} ")
    	print(f"{xr} CUSTOM PASSWORD ")
    	self.__lineX__()
    	__pasX__ = input(f"{xr} INPUT PASSLIST {xr} ")
    	if __pasX__ == ("1"):
    	    self.plist.append("firstlast")
    	    self.plist.append("first last")
    	    self.plist.append("first12")
    	    self.plist.append("first123")
    	    self.plist.append("first1234")
    	    self.plist.append("first12345")
    	    self.plist.append("first")
    	    self.plist.append("first@")
    	    self.plist.append("first@@")
    	    self.plist.append("first@@@")
    	    self.plist.append("first@@@@")
    	    self.plist.append("first@#")
    	    self.plist.append("first##")
    	    self.plist.append("first111")
    	    self.plist.append("@first@")
    	    self.plist.append("@@first@@")
    	    self.plist.append("First123")
    	    self.plist.append("i love you")
    	    self.plist.append("bangladesh")
    	    self.plist.append("@freefire@")
    	else:
    	    try:
    	        self.__clearX__()
    	        print(f"{xr} EXAMPLE {xr} BANGLADESH PASSWORD 10{R}-{W}15 LIMIT ")
    	        print(f"{xr} EXAMPLE {xr} OTHERS COUNTRY PASSWORD 5{R}-{W}10 LIMIT ")
    	        self.__lineX__()
    	        pas_limit = int(input(f"{xr} PASSWORD LIMIT {xr} "))
    	    except:
    	        pas_limit = 5
    	    self.__clearX__()
    	    print(f"{xr} EXAMPLE {xr} firstlast {G}/{W} first12 {G}/{W} first123 ")
    	    self.__lineX__()
    	    for i in range(pas_limit):
    	        self.plist.append(input(f"{xr} ENTER PASSWORD {W}/{G}{i+1}{W}/ {xr} "))
    	with ThreadPool(max_workers=30) as __giftXX__:
    	    self.__clearX__()
    	    total_ids = str(len(__fileL__))
    	    print(f"{xr} TOTAL UID {xr} {W}{total_ids} ")
    	    print(f"{xr} IF NO RESULT ON{R}/{W}OFF AIRPLANE MODE...! ")
    	    self.__lineX__()
    	    for user in __fileL__:
        	    ids,names = user.split('|')
        	    passlist = self.plist
        	    if __methodX__ in ("1"):__giftXX__.submit(self.___M1X___,ids,names,passlist)
        	    elif __methodX__ in ("2"):__giftXX__.submit(self.___M2X___,ids,names,passlist)
        	    else:
        	        __giftXX__.submit(self.___M1X___,ids,names,passlist)
    	print("\033[1;37m")
    	print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    	print(f"{xr} THE PROCESS HAS COMPLETED...!")
    	print(f"{xr} TOTAL {G}OK{W}/{R}CP {xr}{G} "+str(len(self.oks))+f"{W}/{R}"+str(len(self.cps)))
    	print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    	print(f"{xr} THANKS FOR USING.....! ")
#__________/-FILE-M1-\__________#
#__________/-FILE-M2-\__________#
#__________/-END-CALL-\__________#
if __name__ == "__main__":
    __giftX__().__meNu__()