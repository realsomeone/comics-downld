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

