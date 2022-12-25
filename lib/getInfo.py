def getList()->list:
    with open("../data/data.txt") as f: return [item.strip() for item in f.read().split('\n')]

def getLinkDict()->dict:
    values={"tiktok":[],"instagram":[]}
    for item in getList():
        if item.startswith('https://www.instagram.com'):
            values['instagram'].append(item)
        elif item.startswith('https://www.tiktok.com') or item.startswith('https://m.tiktok.com'):
            values['tiktok'].append(item)
    return values

