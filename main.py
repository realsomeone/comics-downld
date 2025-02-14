from api import *
import search
from colorama import Fore
from tqdm import tqdm
from threading import Thread

maxthreads = 4

def downloadcomics(u=None, n=None):
    if u is None:
        print(Fore.GREEN + "Enter lastest URL for comic" + Fore.RESET)
        u = input('url: ')
    if n is None:
        print(Fore.CYAN + "Enter the number of last issue downloaded (skippable)" + Fore.RESET)
        n = input('iss: ')
        if n == '':
            n = 0
        else:
            n = int(n)
    info = search.comic(u)
    makefolder(info[1])
    base = info[0]
    sta = info[2]
    end = n
    year = info[3]
    dlinks = []
    print(Fore.YELLOW + "Getting download links..." + Fore.RESET)
    for i in tqdm(range(sta,end,-1)):
        while True:
            r = get(base + f"/{info[1]}-{i}-{year}/")
            if r != None:
                break
            year -= 1
        urls = search.url(r)
        dlinks.append((urls[0][0],i))
    print(Fore.YELLOW + "Downloading..." + Fore.RESET)
    downthread(dlinks, info)
    print(Fore.GREEN + "Download complete" + Fore.RESET)
        
if __name__ == "__main__":
    downloadcomics()