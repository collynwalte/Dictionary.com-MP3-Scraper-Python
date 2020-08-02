import requests
import urllib.request
import shutil
import os.path
from bs4 import BeautifulSoup
from pathlib import Path

def get_audio():
    wrapper = soup.find(class_='audio-wrapper')
    audio = wrapper.find(type='audio/mpeg')
    url = audio["src"]
    with urllib.request.urlopen(url) as response, open('audio/' + word + '.mp3', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

listfile = Path('wordlist.txt') # <-- Change this to your wordlist file location

wordlist = [line.rstrip('\n') for line in open(listfile)]

if listfile.is_file():
    for x in wordlist:
        word = x
        page = requests.get('https://www.dictionary.com/browse/' + x)
        soup = BeautifulSoup(page.content, 'html.parser')
        get_audio()
else:
    print("ERROR: Wordlist file not found!")