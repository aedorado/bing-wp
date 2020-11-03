from urllib.request import urlopen, urlretrieve
import json 
import ctypes
import pathlib

BURL = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-IN'

def main():
    bing_json_resp = urlopen(BURL).read()
    wp_url = json.loads(bing_json_resp)['images'][0]["url"]
    bf_url = 'http://bing.com' + wp_url
    lf_name = wp_url[7: wp_url.find('.jpg') ] + '.jpg'
    urlretrieve(bf_url, lf_name)
    win_path = str(pathlib.Path().absolute()) + '\\' + lf_name
    ctypes.windll.user32.SystemParametersInfoW(20, 0, win_path, 0)

if __name__ == "__main__":
    main()

