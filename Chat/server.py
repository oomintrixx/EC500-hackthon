import socket
import json
from threading import Thread, Event, Lock

class server(object):
    def __init__(self):
        # Server information
        self.address = ("127.0.0.1", 42000)
        self.UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDP.bind(self.address)

        # Server Thread
        self.run_thread = Thread(target=self.run)

        # Server Database
        self. userlist = {}
        self. userlistR = {}
        self. user_stat = {}

    def start(self):
        self.run_thread.start()

    def run(self):
        while True:
            data, address = self.UDP.recvfrom(1024)
            data = data.decode("utf-8")
            data = json.loads(data)
            if data["cmd"] == "LOGIN":

                print(data.get("username") + " LOGIN")
                self.user_stat[data.get("username")] = True
                self.userlist[data.get("username")] = address
                self.userlistR[address] = data.get("username")
                print(self.userlist)

                package = {}
                package["cmd"] = "SERVER"
                package["userlist"] = self.userlist
                package = json.dumps(package)
                package = package.encode("utf-8")
                for u, returnaddr in self.userlist.items():
                    self.UDP.sendto(package, returnaddr)


            if data["cmd"] == "LOGOFF":
                print(data.get("username") + " LOGOFF")
                del self.user_stat[data.get("username")]
                del self.userlist[data.get("username")]
                print(self.userlist)

                package = {}
                package["cmd"] = "SERVER"
                package["userlist"] = self.userlist
                package = json.dumps(package)
                package = package.encode("utf-8")
                self.UDP.sendto(package, address)

            if data["cmd"] == "UPDATE":
                print(data.get("username") + " UPDATE")
                self.user_stat[data.get("username")] = True

            if data["cmd"] == "GET":
                print(data.get("username") + " GET")
                package = {}
                package["cmd"] = "SERVER"
                package["userlist"] = self.userlist
                data = json.dumps(package)
                data = data.encode("utf-8")
                self.UDP.sendto(data, address)


if __name__ == "__main__":
    s = server()
    s.start()
