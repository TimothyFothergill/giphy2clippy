# giphy2clippy

Grabs a gif from giphy, shows you the name and url of the gif and copies the url to clipboard. Initially made because I wanted a fast way to say LGTM on GitHub :)

# Setup

Clone this repo

```
git clone git@github.com:TimothyFothergill/giphy2clippy.git
```

Make a .env file and add:
```
api-key=<your-giphy-api-key>
```

Download Python dependencies: 

```
pip install -r requirements.txt
```

# Usage

`python main.py -s your-search-term`

Args:
```
-s --search: Searches for any string.
-r --rating: Searches within this rating or lower - g, pg, pg-13 or r
-n --num: Limits the search to this many possibilities.
-R --random-disabled: Get the top result. This can be useful to verify you are hitting the same results. Note: This disables copying to clipboard.
-g --github: Style the copied output to a github comment (![your-search-term][output-url])
```
