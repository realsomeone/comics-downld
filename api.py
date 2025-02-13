import requests
import os

def get(url):
    req = requests.get(url)
    if req.status_code == 200:
        return req.text
    else: return None

def wget(url, fname, dir):
    os.system(f"wget {url} -O {fname} -P {dir}")
    
def makefolder(name):
    os.system(f"mkdir comics/{name}")

def download(l, info):
    print(f"Downloading issue {l[1]}...")
    wget(l[0], f'{info[1]}-{l[1]}', f"comics/{info[1]}")