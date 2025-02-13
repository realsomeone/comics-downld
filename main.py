from api import *
import search
from colorama import Fore, init
from threading import Thread
init()

maxthreads = 4

def downloadcomics(u=None, n=None):
    if u is None:
        print(Fore.GREEN + "Enter lastest URL for comic")
        u = input('url: ')
    if n is None:
        print(Fore.CYAN + "Enter the number of last issue downloaded (skippable)")
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
    for i in range(sta,end,-1):
        while True:
            r = get(base + f"/{info[1]}-{i}-{year}/")
            if r != None:
                break
            year -= 1
        urls = search.url(r)
        dlinks.append((urls[0][0],i))
    for l in dlinks:
        download(l, info) # add multi-threading here
    print(Fore.GREEN + "Download complete")
        
if __name__ == "__main__":
    downloadcomics()