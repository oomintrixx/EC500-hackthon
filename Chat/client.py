import socket
import json
import threading
from time import  sleep
from threading import Thread, Event, Lock
from queue import Queue
import sys

class Client(object):

    def __init__(self, username, password, port):
        # User information
        self.username = username
        self.password = password

        # User internet configure
        self.address = ("127.0.0.1", port)
        self.ip ="127.0.0.1"
        self.port = str(port)
        self.UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDP.bind(self.address)

        # DNS       //should in a database
        self.DNS = {"server": ("127.0.0.1", 42000)}
        self.DNSR = {("127.0.0.1", 42000): "server"}
        #self. DNS = {"Dog": ("127.0.0.1", 42001), "Cat": ("127.0.0.1", 42002), "server": ("127.0.0.1", 42000)}
        #self. DNSR = {("127.0.0.1", 42001): "Dog", ("127.0.0.1", 42002): "Cat", ("127.0.0.1", 42000): "server" }
        self. DNS_OL = {}
        self. DNSR_OL ={}

        # Database  //should in a database
        self. chat_record = {}
        for user, address in self.DNS.items():
            self.chat_record[user] = []
        self. freind_waitlist ={}

        # Temper variants
        self. connected_peer = None

        # Treads
        self.cmd_tread = Thread(target=self.cmdline)
        self.send_tread = Thread(target=self.send)
        self.receive_tread = Thread(target=self.receive)

        # Control Signal

        # Container
        self.sendbuffer = Queue(5)
        self.sendbuffer_lock = Lock()
        self.receivebuffer = Queue(5)
        self.receivebuffer_lock = Lock()

    def start(self):
        self.cmd_tread.start()
        self.send_tread.start()
        self.receive_tread.start()

    def fresh(self):
        package = {}



    def send(self):
        while True:
            while True:
                if not self.sendbuffer.empty():
                    self.sendbuffer_lock.acquire()
                    target_address, data = self.sendbuffer.get()
                    self.sendbuffer_lock.release()
                    data = bytes(data, encoding="utf-8")
                    if target_address is None:
                        print("Fault, user do not exist")
                        break
                    else:
                        self.UDP.sendto(data, tuple(target_address))

    def receive(self):
        while True:
            data, address = self.UDP.recvfrom(1024)
            #print(data, address)1
            peername = self.DNSR.get(address)
            if peername is None:
                peername = self.DNSR_OL.get(address)
                if self.chat_record.get(peername) is None:
                    self.chat_record[peername]=[]
            if peername is not None:
                data = data.decode("utf-8")
                package = json.loads(data)
                #print(package)
                if package.get("cmd") =="TRANSFER":
                    text = package.get("text")
                    if peername == self.connected_peer:
                        message = peername+": "+text
                        print(message)
                        self.chat_record[peername].append(message)
                    else:

                        message = peername + ": " + text
                        print("                                             You have new nortificatoin from " + peername)
                        self.chat_record[peername].append(message)

                if package.get("cmd") =="FRIEND":
                    self.freind_waitlist[package.get("username")] = address
                    print("                                                 You get a new friend application from "+package.get("username"))

                if package.get("cmd") == "SERVER":
                    self.DNS_OL = package.get("userlist")
                    for a, b in self.DNS_OL.items():
                        self.DNS_OL[a] = tuple(b)
                    for a, b in self.DNS_OL.items():
                        self.DNSR_OL[tuple(b)] = a






    def cmdline(self):
        while True:
            print(">>>CMD>>>", end="")
            string = input()
            string = string.split(" ")
            string[0] = string[0].upper()
            if len(string)>=2:
                cmd, target, *content = string
                if cmd == "SET" and target.upper() == "PUBLIC":
                    # Choose the server address
                    server_address = ("127.0.0.1", 42000)

                    # Build a json-string package
                    package = {}
                    package["cmd"] = "LOGIN"
                    package["username"] = self.username
                    package = json.dumps(package)
                    self.sendbuffer.put((server_address, package))

                if cmd == "SET" and target.upper() == "PRIVATE":
                    # Choose the server address
                    server_address = ("127.0.0.1", 42000)

                    # Build a json-string package
                    package = {}
                    package["cmd"] = "LOGOFF"
                    package["username"] = self.username
                    package = json.dumps(package)
                    self.sendbuffer.put((server_address, package))

                if cmd == "CHAT":
                    target_address = self.DNS.get(target)
                    if target_address is None:
                        target_address = self.DNS_OL.get(target)
                        if self.chat_record.get(target) is None:
                            self.chat_record[target] = []
                    if target_address is None:
                        print("User do not exist")
                    else:
                        self.connected_peer = target
                        print("==================  " + target + "  ==================")
                        for message in self.chat_record[target]:
                            print(message)
                        while True:
                            string = input()
                            if string.upper() == "!DIS!":
                                self.connected_peer = None
                                break
                            else:
                                # Build a json-string package
                                package = {}
                                package["cmd"] = "TRANSFER"
                                package["text"] = string
                                package = json.dumps(package)

                                # Add the message to the chat_record
                                message = self.username + ": " + string
                                self.chat_record[target].append(message)

                                # Send the message
                                self.sendbuffer.put((target_address, package))


                if cmd == "LIST" and target.upper() == "FRIENDS":
                    print("============You have following friends:==============")
                    for a, b in self.DNS.items():
                        if a !="server" and a!=self.username:
                            print(a)

                if cmd == "LIST" and target.upper() == "APPLY":
                    print("============Friend applications pending:==============")
                    for a in self.freind_waitlist.items():
                        print(a)

                if cmd == "LIST" and target.upper() == "ONLINE":
                    # Choose the server address
                    server_address = ("127.0.0.1", 42000)

                    # Build a json-string package
                    package = {}
                    package["cmd"] = "GET"
                    package["username"] = self.username
                    package = json.dumps(package)
                    self.sendbuffer.put((server_address, package))
                    sleep(1)
                    print("Online Users: ")
                    for username, address in self.DNS_OL.items():
                        if username != self.username:
                            print(username)

                if cmd == "ADD":
                    # Choose the server address
                    if self.DNS_OL.get(target) is None:
                        print(target + "is not online")
                    else:
                        # Build a json-string package
                        self.DNS[target] = self.DNS_OL.get(target)
                        self.DNSR[self.DNS_OL.get(target)] =target
                        package = {}
                        package["cmd"] = "FRIEND"
                        package["username"] = self.username
                        package = json.dumps(package)
                        self.sendbuffer.put((self.DNS_OL.get(target), package))

                if cmd == "CONFIRM":
                    addr = self.freind_waitlist.get(target)
                    if  addr is None:
                        print("Friend not in list")
                    else:
                        self.DNS[target] = addr
                        self.DNSR[addr] = target
                        print("Confirm Successfully")
                        print(self.DNS)





if __name__ == "__main__":
    try:
        username = sys.argv[1]
        port = sys.argv[2]
        user = Client(username, "112233", int(port))
        user.start()
    except:
        print("INVALID")




