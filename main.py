import json
import os
import pyperclip
import sys, getopt

from urllib import parse, request
from random import randrange

from dotenv import load_dotenv
load_dotenv()

def generate_giphy(query, rating="g", num=10, random=True):
    url = "http://api.giphy.com/v1/gifs/search"
    params = parse.urlencode({
        "q"         : query,
        "api_key"   : os.getenv("api-key"),
        "rating"    : rating,
        "limit"     : num
    })

    data = []
    if(random):
        with request.urlopen("".join((url, "?", params))) as response:
            data = json.loads(response.read())
            n = randrange(0,num)
            print(
                json.dumps(data["data"][n]["title"] + 
                ": " + 
                json.dumps(data["data"][n]["images"]["original"]["url"], sort_keys=True, indent=4))
            )
            clip = json.dumps(data["data"][n]["images"]["original"]["url"])
            clip = clip.strip('\"')
            pyperclip.copy(clip)
    else:
        for n in range(num):
            with request.urlopen("".join((url, "?", params))) as response:
                data = json.loads(response.read())
                print(
                    json.dumps(data["data"][n]["title"] + 
                    ": " + 
                    json.dumps(data["data"][n]["images"]["original"]["url"], sort_keys=True, indent=4))
                )

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hs:",["search="])
    except getopt.GetoptError:
        print('main.py -s <search>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -s <search>')
            sys.exit(2)
        elif opt in ("-s", "--search"):
            generate_giphy(arg)
        else:
            generate_giphy("LGTM")        

if __name__ == "__main__":
    main(sys.argv[1:])
