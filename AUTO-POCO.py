#---------------------------------------------
#-DECODE BY IMRAN
#-DECODE : 24|02|2025
#-FIX : 24|02|2025
#-FIX BY IMRAN
#-WRITTEN BY MR-POCO
#---------------------------------------------
#_________|MODULE|_________#
import os,sys,re,time,json
import requests,bs4,string
import faker,fake_email,random
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
#_________|LOOP|_________#
oks = [];cps = [];loop = 0
#_________|COLOR|_________#
G = '\x1b[1;32m';W = '\x1b[1;97m';R = '\x1b[38;5;160m';B = '\x1b[1;90m';Y = '\x1b[1;33m';T = '\x1b[1;34m';E = '\x1b[38;5;205m';O = '\x1b[38;5;81m'
#_________|STYLE|_________#
xd = f''' {W}[{G}={W}]{W}''';xd1 = f''' {W}[{G}1{W}]{W}''';xd2 = f''' {W}[{G}2{W}]{W}''';xd0 = f''' {W}[{G}0{W}]{W}''';xdx = f''' {W}[{G}?{W}]{W}'''
#_________|CLEAR|_________#
def clear():os.system('clear');print(logo)
#_________|LINE|_________#
def linex():print(f'''{W}{'──────────────────────────────────────────────────'}''')
#_________|UA|_________#
ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))
#_________|EXTRACTOR|_________#
def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}
#_________|FAKE EMAIL|_________#
def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']
#_________|FAKE EMAIL CODE|_________#
def GetCode(email):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        code = re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None
#_________|LOGO|_________#
logo = (f'''
{W}    F{G}B{W} ┏━┓╻ ╻╺┳╸┏━┓   ┏━╸┏━┓┏━╸┏━┓╺┳╸┏━╸
{G}    F{W}B{W} ┣━┫┃ ┃ ┃ ┃ ┃   ┃  ┣┳┛┣╸ ┣━┫ ┃ ┣╸
{W}    F{G}B{W} ╹ ╹┗━┛ ╹ ┗━┛   ┗━╸╹┗╸┗━╸╹ ╹ ╹ ┗━╸ 1.0
{W}──────────────────────────────────────────────────
{xd} OWNER {R}:{W} MR-POCO
{xd} TOOLS {R}:{W} Facebook Ids Auto Create
{W}──────────────────────────────────────────────────''')
#_________|MENU|_________#
def poco():
    clear();print(f'''{xd1} START AUTO CREATE ''');print(f'''{xd0} EXIT CLONE ''');linex();mr = input(f'''{xdx} SELECT : ''')
    if mr in ('1',):____create____()
    elif mr in ('0',):exit()
    else:linex();print(f'''{xd} OPTION NOT FOUND ''');linex();time.sleep(1);print(f'''{xd} TRY AGAIN ''');time.sleep(1);poco()
#_________|PROGRES|_________#
def progres(current,num_accounts,delay):
    for sleep in range(int(delay), 0, -1):
        print(f'''\r{xd}-[{G}CREATE-START{W}]-[{current}{W}]-[{G}{len(oks)}{W}]-[{R}{len(cps)}{W}] ''', end = '\x1b[1;32m')
        time.sleep(1)
        if not current == num_accounts:
            pass
#_________|CREATE|_________#
def ____create____():
    global num_accounts,delay
    clear();print(f'''{xd} EXAMPLE {R}:{W} Habib {R}|{W} Fahim {R}|{W} Rakib {R}|{W} Sakib ''');linex();firstname = input(f'''{xdx} ENTER FIRST NAME : ''');linex();print(f'''{xd} EXAMPLE {R}:{W} Hossain {R}|{W} Islam {R}|{W} Ahmed {R}|{W} Khan ''');linex();lastname = input(f'''{xdx} ENTER LAST NAME : ''');linex();print(f'''{xd} EXAMPLE {R}:{W} 5000 {R}|{W} 1000 {R}|{W} 7777 {R}|{W} 9999 ''');linex();num_accounts = int(input(f'''{xdx} ENTER LIMIT : '''));linex();print(f'''{xd} EXAMPLE {R}:{W} 1 {R}|{W} 2 {R}|{W} 3 {R}|{W} 4 {R}|{W} 5 {R}|{W} 6 {R}|{W} 7 {R}|{W} 8 ''');linex();delay = int(input(f'''{xdx} ENTER BETWEEN TIME : '''))
    clear();print(f'''{xd} TOTAL CREATE LIMIT {R}:{G} {num_accounts} ''');print(f'''{xd} IF NO RESULT ON{R}|{W}OFF AIRPLANE MODE''');linex()
    for make in range(int(num_accounts)):
        progres(make + 1, num_accounts, delay)
        ses = requests.Session()
        response = ses.get(url = 'https://x.facebook.com/reg',
        params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},)
        mts = ses.get('https://x.facebook.com').text
        m_ts = re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        formula = extractor(response.text)
        email2 = GetEmail()
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],"Mrpoco1971"),
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":ugenX(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = 'https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1'
        py_submit = ses.post(reg_url, data = payload, headers = header1)
        if 'c_user' in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok['c_user'])
            header2 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ugenX(),
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://m.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2).text
            valid = GetCode(email2)
            if valid:
                print("\n");linex();print(f'''{xd}-{W}[{G}ACCOUNTS-NAME{W}]{G} {firstname} {lastname} ''')
                print(f'''{xd}-{W}[{G}VERIFY-CODE{W}]{G} {valid} ''')
                confirm_id(email2,uid,valid,con_sub,ses)
            cps.append(uid)
#_________|CONFIRM ID|_________#
def confirm_id(mail,uid,otp,data,ses):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
        'contact': mail,
        'type': "submit",
        'is_soft_cliff': "false",
        'medium': "email",
        'code': otp}
        payload = {
        'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
        'jazoest': re.search(r'"\d+"', data).group().strip('"'),
        'lsd': re.search(r'"LSD",\[\],{"token":"([^"]+)"}',str(data)).group(1),
        '__dyn': "",
        '__csr': "",
        '__req': "4",
        '__fmt': "1",
        '__a': "",
        '__user': uid}
        headers = {
        'User-Agent': ugenX(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            cps.append(uid)
        else:
            cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            print(f'''\r{xd}-{W}[{G}MRPOCO-OK{W}]{G} {uid} | Mrpoco1971 ''')
            print(f'''\r{xd}-{cookie} ''');linex()
            open('/sdcard/MRPOCO-AUTO-CRATE-OK-ID.txt', 'a').write(uid + '|Mrpoco1971|' + cookie + '\n')
            oks.append(uid)
    except Exception as e:
        pass
#_________|END|_________#
if __name__ == '__main__':
    poco()