import requests


def getDict() -> dict:
    response = requests.get('https://ttdownloader.com/')
    point = response.text.find('<input type="hidden" id="token" name="token" value="') + \
        len('<input type="hidden" id="token" name="token" value="')
    token = response.text[point:point+64]
    TTDict = {
        'token': token,
    }

    for i in response.cookies:
        TTDict[str(i).split()[1].split('=')[0].strip()] = str(
            i).split()[1].split('=')[1].strip()
    return TTDict
