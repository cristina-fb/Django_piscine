import sys
import dewiki
import requests

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid argument number")
    else:
        S = requests.Session()
        URL = "https://en.wikipedia.org/w/api.php"
        SEARCHPAGE = sys.argv[1]
        PARAMS = {
            "action": "query",
            "srsearch": SEARCHPAGE,
            "srlimit": "1",
            "list": "search",
            "format": "json"
        }
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        print(DATA)