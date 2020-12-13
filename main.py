import cookies
import requests
import urllib.parse
from os import path
from os import stat


def main():
    auth = input("Enter your ADCDownloadAuth cookie: ")
    cookiesDict = {"ADCDownloadAuth": urllib.parse.unquote(auth)}
    url = input("Enter your Xcode download url: ")
    firstByte = 0
    if path.exists("Xcode.xip"):
        print("Found existing Xcode XIP, resuming download...")
        xcodeFile = open("Xcode.xip", "ab")
        firstByte = stat("Xcode.xip").st_size
    else:
        xcodeFile = open("Xcode.xip", "wb")
    headers = {"Cookie": cookies.dict2cookies(cookiesDict), "Range": "bytes=" + str(firstByte) + "-" + "99999999999"}
    r = requests.get(url, stream=True, headers=headers)
    if r.status_code != 200 and r.status_code != 206:
        print("Failed to download Xcode XIP file! Response code ", r.status_code)
        exit(1)
    for byte in r.iter_content():
        if byte:
            xcodeFile.write(byte)
    print("Done :)")
    xcodeFile.close()


if __name__ == '__main__':
    main()
