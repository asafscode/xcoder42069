import urllib.parse


def cookies2dict(cookieString):
    cookies = cookieString.split(";")
    cookieDict = {}
    for cookie in cookies:
        splitCookie = cookie.split("=")
        if splitCookie[0] != "":
            cookieDict[splitCookie[0]] = urllib.parse.unquote(splitCookie[1])
    return cookieDict


def dict2cookies(cookieDict):
    cookies = ""
    for key in cookieDict:
        cookies += key + "=" + urllib.parse.quote(cookieDict[key], safe='') + ";"
    return cookies
