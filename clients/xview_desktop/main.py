#!/bin/bash

import sys
import os
from os import system
from insert import Insert
from file import EpisodeFile, ListFile
from controller import Controller

HOST = ""  # Insert host ip
PORT = 65432  # Insert port
LIST = "files/list.txt"
EPISODE = "files/episode.txt"
URl = ""  # Insert anime url

insert = Insert(sys.argv)
link_file = ListFile(LIST)
episode = EpisodeFile(EPISODE)
controller = Controller(HOST, PORT)

file_size = os.path.getsize(LIST)
if file_size == 0:
    link_file.create_list(URl)

queue = ""
amount = insert.check()
old_episode = controller.get_episode()
links = link_file.get_links(episode, amount)
for link in links:
    queue += "\"" + link.strip("\n") + "\" "
system("vlc " + queue)
controller.update_episode(episode, old_episode)
