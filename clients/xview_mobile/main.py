import sys
import os
import time
from os import system

from episode_function import *
from checks import *
from file_function import *

LIST = "files/list.txt"
EPISODE = "files/episode.txt"
URL = 'https://animeunity.it/anime/743-detective-conan/17780'

file_size = os.path.getsize(LIST)
if file_size == 0:
    create_list()

old_episode = 0
amount = input_check(sys.argv)
queue = ""
# noinspection PyBroadException
try:
    old_episode = main_episode_number_check()
except Exception(ConnectionRefusedError):
    links = get_episode_links(amount)
    create_m3u_file(links)
    system("xdg-open playlist.m3u")
    # noinspection PyBroadException
    try:
        time.sleep(15)
        update_main_episode_number(old_episode)
    except Exception(ConnectionError):
        pass
