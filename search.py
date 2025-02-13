import regex as re

def url(text):
    return re.findall(r"(([^\"]+)(dlds)([^\"]*))", text)

def comic(link):
    r = list(re.findall(r"(h.+\w+)\/([^\/]+)-(\d+)-(\d+)", link)[0])
    r[2] = int(r[2])
    r[3] = int(r[3])
    return r