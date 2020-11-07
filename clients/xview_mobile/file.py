import json
import requests
from bs4 import BeautifulSoup


class File:
    def __init__(self, path):
        self.path = path

    def read_file(self):
        with open(self.path, "r") as f:
            return f.read()

    def write_file(self, data):
        with open(self.path, "w+") as f:
            f.write(data)


class EpisodeFile(File):
    def __init__(self, path):
        super(EpisodeFile, self).__init__(path)

    def get_episode(self):
        return self.read_file()

    def set_episode(self, number):
        self.write_file(str(number))

    def set_next_episode(self):
        number = int(self.get_episode()) + 1
        self.write_file(str(number))


class ListFile(File):
    def __init__(self, path):
        super(ListFile, self).__init__(path)

    def get_links(self, file, amount):
        with open(self.path, "r") as f:
            episodes = []
            lines = f.readlines()
            for i in range(amount):
                episode_number = int(file.get_episode())
                separate = lines[episode_number - 1].split(" ")
                episodes.append(separate[1])
                file.set_next_episode()
            return episodes

    def create_list(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        episodes = soup.find("video-player")["episodes"]
        episodes_json = json.loads(episodes)
        with open(self.path, "w") as file:
            for i in episodes_json:
                file.write(i["number"] + " " + i["link"] + "\n")


class PlaylistFile(File):
    def __init__(self, path):
        super(PlaylistFile, self).__init__(path)

    def create_playlist(self, links):
        i = 1
        open(self.path, 'w').close()
        file = open(self.path, "w+")
        file.write("#EXTM3U\n")
        for link in links:
            file.write("#EXTINF:-1," + str(i) + "\n" + link)
            i += 1
