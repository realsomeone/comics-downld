from api import *
import search
from colorama import Fore
from tqdm.auto import tqdm
from multiprocessing.pool import ThreadPool
import zipfile
import pathlib

dir = pathlib.Path('comics/')

maxthreads = 4

global info

def downloadcomics(u=None, n=None, z=None):
    global info
    if u is None:
        print(Fore.GREEN + "lastest URL" + Fore.RESET)
        u = input('url: ')
    if n is None:
        print(Fore.CYAN + "last issue downloaded" + Fore.RESET)
        n = input('iss: ')
        if n == '':
            n = 0
        else:
            n = int(n)
    if z is None:
        print(Fore.BLUE + "zip end? (Y/n): " + Fore.RESET, end='')
        z = input()
        if z != 'n':
            z = True
        else: z = False
    info = search.comic(u)
    makefolder(info[1])
    base = info[0]
    sta = info[2]
    end = n
    year = info[3]
    dlinks = []
    cont = True
    print(Fore.YELLOW + "Getting download links..." + Fore.RESET)
    for i in tqdm(range(sta,end,-1)):
        while True:
            r = get(base + f"/{info[1]}-{i}-{year}/")
            if r != None:
                ogyear = year
                break
            year -= 1
            if ogyear - year >= 10:
                print(Fore.RED + "More than 10 years without issues; downloading existing ones." + Fore.RESET)
                break; cont=False
        if not cont: break
        urls = search.url(r)
        dlinks.append((urls[0][0],i))
    print(Fore.YELLOW + "Downloading..." + Fore.RESET)
    with ThreadPool(maxthreads) as pool:
        list(tqdm(pool.imap(download, dlinks), total=len(dlinks)))
    if z:
        print(Fore.YELLOW + "Zipping..." + Fore.RESET)
        with zipfile.ZipFile(f'comics/{info[1]}_{end+1}-{sta}.zip', 'w') as z:
            for file in tqdm(dir.rglob(f"{info[1]}*.cbz"), total=len(dlinks)):
                z.write(file, arcname=file.relative_to(dir))
               
def download(l):
    global info
    with requests.get(l[0], stream=True) as r:
        with open(f"comics/{info[1]}/{info[1]}-{l[1]}.cbz", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                 
if __name__ == "__main__":
    downloadcomics()