#!/bin/bash

import sys
import os
from os import system
from insert import Insert
from file import EpisodeFile, PlaylistFile, ListFile
from controller import Controller

HOST = ""  # Insert host ip
PORT = 65432  # Insert port
LIST = "files/list.txt"
EPISODE = "files/episode.txt"
PLAYLIST = "files/playlist.m3u"
URl = ""  # Insert anime url

insert = Insert(sys.argv)
if not os.path.isfile(LIST):
    with open(LIST, 'w'):
        pass

link_file = ListFile(LIST)
file_size = os.path.getsize(LIST)
if file_size == 0:
    link_file.create_list(URl)
episode = EpisodeFile(EPISODE)
controller = Controller(HOST, PORT)
playlist = PlaylistFile(PLAYLIST)
amount = insert.check()
old_episode = controller.get_episode()
links = link_file.get_links(episode, amount)
playlist.create_playlist(links)
system("xdg-open files/playlist.m3u")
controller.update_episode(episode, old_episode)
