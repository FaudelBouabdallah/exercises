import urllib.request
import sys
import re
import json


def to_url(string):
    return re.sub(' ', '%20', string)

artist, title = sys.argv[1:]
title = to_url(title)
artist = to_url(artist)

url = f"https://api.lyrics.ovh/v1/{artist}/{title}"

with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['lyrics'])