import socket
import time


class Controller:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @staticmethod
    def create_socket():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_episode(self):
        try:
            s = self.create_socket()
            s.connect((self.host, self.port))
            s.send(b'get_episode')
            data = s.recv(1024)
            return int(data)
        except socket.error:
            return -1

    def update_episode(self, file, old_episode):
        try:
            time.sleep(10)
            s = self.create_socket()
            s.connect((self.host, self.port))
            new_number = file.get_episode()
            if old_episode <= int(new_number):
                s.send(new_number.encode())
        except socket.error:
            print("Controller not found, episode number saved only in local file")
            return 0
