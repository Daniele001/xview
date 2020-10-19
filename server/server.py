import socket

HOST = "0.0.0.0"
PORT = 65432
EPISODE = "episode.txt"


def set_episode_number(number):
    with open(EPISODE, "w") as f:
        f.write(str(number))
        f.close()


def read_episode_number():
    with open(EPISODE, "r") as f:
        number = f.read()
        f.close()
    return str.encode(number)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if data.decode("utf-8") == "get_episode":
                conn.send(read_episode_number())
            if data.decode("utf-8").isdigit():
                set_episode_number(int(data))
            if not data:
                break
