import requests
import os

def get(url):
    req = requests.get(url)
    if req.status_code == 200:
        return req.text
    else: return None

def wget(url, fname, dir):
    os.system(f"wget {url} -O {dir}/{fname}.cbz -q --show-progress")
    
def makefolder(name):
    os.system(f"mkdir comics/{name}")

def download(l, info):
    wget(l[0], f'{info[1]}-{l[1]}', f"comics/{info[1]}")
    
def downthread(links, info):
    while len(links) > 0:
        download(links.pop(), info)