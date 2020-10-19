import json
import requests
from bs4 import BeautifulSoup

URL = ''
LIST = "files/list.txt"


def create_list():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    episodes = soup.find("video-player")["episodes"]
    episodes_json = json.loads(episodes)
    with open(LIST , "w") as file:
        for i in episodes_json:
            file.write(i["number"] + " " + i["link"] + "\n")
