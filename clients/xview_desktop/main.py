import sys
import os
from os import system

from checks import *
from episode_function import get_episode_links
from file_function import *

LIST = "files/list.txt"

file_size = os.path.getsize(LIST)
if file_size == 0:
    create_list()

queue = ""
amount = input_check(sys.argv)
old_episode = main_episode_number_check()
links = get_episode_links(amount)
for link in links:
    queue += "\"" + link.strip("\n") + "\" "
system("vlc " + queue)
update_main_episode_number(old_episode)
