import requests
from getTTDict import getDict
from getInfo import getLinkDict
import instaloader

def createHeader(parseDict) -> list:

    cookies = {
        'PHPSESSID': parseDict['PHPSESSID'],
        # 'popCookie': parseDict['popCookie'],
    }
    headers = {
        'authority': 'ttdownloader.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://ttdownloader.com',
        'referer': 'https://ttdownloader.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'url': '',
        'format': '',
        'token': parseDict['token'],
    }
    return cookies, headers, data


def TDL(cookies, headers, data, name) -> None:
    response = requests.post('https://ttdownloader.com/search/',
                             cookies=cookies, headers=headers, data=data)
    linkParse = [i for i in str(response.text).split()
                 if i.startswith("href=")][0]

    response = requests.get(linkParse[6:-10])
    with open("./vids/"+"tiktok"+name+".mp4", "wb") as f:
        f.write(response.content)


def TDLALL() -> None:
    parseDict = getDict()
    cookies, headers, data = createHeader(parseDict)
    linkList = getLinkDict()['tiktok']
    for i in linkList:
        try:
            data['url'] = i
            TDL(cookies, headers, data, str(linkList.index(i)))
        except IndexError:
            parseDict = getDict()
            cookies, headers, data = createHeader(parseDict)
        except Exception as err:
            print(err)
            exit(1)


def IDL(url,name) -> None:
    obj = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(obj.context, url.split('p/')[1].strip('/ '))
    photo_url = post.url
    video_url = post.video_url
    if video_url:
        response = requests.get(video_url)
        with open("./vids/"+"insta"+name+".mp4", "wb") as f:
            f.write(response.content)
    elif photo_url:
        response = requests.get(photo_url)
        with open("./vids/"+"insta" +name+".jpg", "wb") as f:
            f.write(response.content)

def IDLALL() -> None:
    linkList = getLinkDict()['instagram']
    for i in linkList:
        try:
            IDL(i,str(linkList.index(i)))
        except Exception as err:
            print(err)
            exit(1)


if __name__ == "__main__":
    # TDLALL()
    # IDLALL()
    pass
