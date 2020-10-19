import socket
from episode_function import read_episode_number, set_episode_number

HOST = '192.168.0.50'
PORT = 65432


def main_episode_number_check():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(b'get_episode')
        data = s.recv(1024)
    episode_number = read_episode_number()
    if int(episode_number) < int(data):
        set_episode_number(int(data))
    return int(data)


def update_main_episode_number(old_episode):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        if old_episode <= int(read_episode_number()):
            s.send(read_episode_number().encode())
        

def input_check(arg):
    try:
        if len(arg) - 1 == 1:
            if arg[1].isdigit():
                return int(arg[1])
            else:
                raise NoDigitsError
        if len(arg) - 1 == 0:
            return 0
        else:
            raise ManyArgumentsError
    except NoDigitsError:
        print("please insert the number of episodes that you want to see")
        exit()
    except ManyArgumentsError:
        print("too many arguments")
        exit()


class Error(Exception):
    pass


class ManyArgumentsError(Error):
    pass


class NoDigitsError(Error):
    pass
