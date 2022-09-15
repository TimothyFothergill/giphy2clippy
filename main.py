import json
import os
import pyperclip
import sys, getopt

from urllib import parse, request
from random import randrange

from dotenv import load_dotenv
load_dotenv()

def generate_giphy(query, rating="g", num=10, random=True, github=False, outputOnly=False):
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
            if(num > len(data)):
                num == len(data)
            n = randrange(0,num)
            print(
                json.dumps(data["data"][n]["title"] + 
                ": " + 
                json.dumps(data["data"][n]["images"]["original"]["url"], sort_keys=True, indent=4))
            )
            clip = json.dumps(data["data"][n]["images"]["original"]["url"])
            clip = clip.strip('\"')
            if(outputOnly == False):
                if(github):
                    pyperclip.copy("![" + query + "](" + clip + ")")
                else:
                    pyperclip.copy(clip)
            else:
                if(github):
                    print("![" + query + "](" + clip + ")\n")
                else:
                    print(clip+"\n")

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
    s = "LGTM"
    r = "g"
    num = 10
    random=True
    github=False
    outputOnly=False

    try:
        opts, args = getopt.getopt(argv,"hs:r:n:Rgd",["search=", "rating=", "num=", "random-disabled", "github", "output-only"])
    except getopt.GetoptError:
        print('main.py -s <search> -r <rating> -n <number> -R <random-disabled> -g <github> -d <output-only>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -s <search> -r <rating> -n <number> -R <random-disabled> -g <github> -d <output-only>')
            sys.exit(2)
        elif opt in ("-s", "--search"):
            s = arg
        elif opt in ("-r", "--rating"):
            r = arg
        elif opt in ("-n", "--num"):
            num = arg
        elif opt in ("-R", "--random-disable"):
            random = False
        elif opt in ("-g", "--github"):
            github = True
        elif opt in ("-d", "--output-only"):
            outputOnly = True
    generate_giphy(s,r,int(num),random,github,outputOnly)

if __name__ == "__main__":
    main(sys.argv[1:])
