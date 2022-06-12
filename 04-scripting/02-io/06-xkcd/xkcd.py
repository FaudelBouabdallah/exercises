from PIL import Image
import urllib.request
import json
import sys


def fetch_data(n):
    if n:
        url = f'https://xkcd.com/{n}/info.0.json'
    else:
        url = 'https://xkcd.com/info.0.json'

    with urllib.request.urlopen(url) as input:
        data = input.read()
    
    return json.loads(data)

def fetch_image(url):
    with urllib.request.urlopen(url) as stream:
        return Image.open(stream)

data = fetch_data(None if len(sys.argv) == 1 else int(sys.argv[1]))

for key, value in data.items():
    print(f'{key}: {value}')

fetch_image(data['img']).show()