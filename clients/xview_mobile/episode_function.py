EPISODE = "files/episode.txt"
LIST = "files/list.txt"
PLAYLIST = "files/playlist.m3u"


def read_episode_number():
    with open(EPISODE, "r") as f:
        number = f.read()
        f.close()
    return number


def set_episode_number(number):
    with open(EPISODE, "w") as f:
        f.write(str(number))
        f.close()


def set_next_episode_number(number, c):
    with open(EPISODE, "w") as f:
        number += c
        f.write(str(number))
        f.close()


def get_episode_links(amount):
    with open(LIST, "r") as f:
        episodes = []
        step = 1
        lines = f.readlines()
        for i in range(amount):
            episode_number = int(read_episode_number())
            print(lines[episode_number-1])
            separate = lines[episode_number - 1].split(" ")
            episodes.append(separate[1])
            set_next_episode_number(episode_number, step)
        return episodes


def create_m3u_file(links):
    i = 1
    open(PLAYLIST, 'w').close()
    file = open(PLAYLIST, "w+")
    file.write("#EXTM3U\n")
    for link in links:
        file.write("#EXTINF:-1," + str(i) + "\n" + link)
        i += 1
