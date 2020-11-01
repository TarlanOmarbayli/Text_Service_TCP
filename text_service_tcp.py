import socket
import optparse
import sys
import json
import os

class Server():
    def __init__ (self,interface,port):
        self.interface = '127.0.0.1'
        self.port = port

    def connect(self):
        sock = socket.socket(socket.AF_INET,sock.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.interface,self.port))
        sock.listen(1)
        print('Listening at', sock.getsockname())
        sc, address = sock.accept()


    def get_data(self):
        j_data = ""
        while True:
            try:
                j_data = j_data + sc.recv(1024).decode()
                return json.loads(j_data)
            except ValueError:
                continue

    def send_data(self, data):
        j_data = json.dumps(data)
        sc.send(j_data.encode())

    def change(self, txt, dict_s):
        words = txt.split()
        f_dict = eval(dict_s)
        for w in words:
            if w in f_dict.keys():
                txt = txt.replace(w, f_dict[w])
        return txt

    def encode_decode(self, txt, key):
        res_text = ""
        for i in range(len(txt)):
            c = txt[i]
            k = key[i%len(key)]
            res_text += chr(ord(c) ^ ord(k))
        return res_text

    def start(self):
        self.connect()
        data_get = self.recieve()
        if data_get[0] == "change_text":
            res = self.change(data_get[1], data_get[2])
        if data_get[0] == "encode_decode":
            res = self.encode_decode(data_get[1], data_get[2])
        self.send(res)



class Client():
    def __init__ (self,hostname,port,mode):
        self.hostname = hostname
        self.port = port
        self. mode = mode

    def connect(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((self.hostname, self.port))

    def get_data(self):
        j_data = ""
        while True:
            try:
                j_data = j_data + sc.recv(1024).decode()
                return json.loads(j_data)
            except ValueError:
                continue

    def send_data(self,data):
        j_data = json.dumps(data)
        sock.send(j_data.encode())

    def send_server(self, file1, file2):
        msg_text = open(file1, 'r').read()
        aux_text = open(file2, 'r').read()
        data = []
        data.append(self.mode)
        data.append(msg_text)
        data.append(aux_text)
        self.send(data)
        data_get = self.get_data()
        print(data_get)


def main():
    parser = optparse.OptionParser()
    parser.add_option("-p", metavar="PORT", type= int, help="Port on which server listens")
    if sys.argv[1] == "client":
        parser.add_option("--host", dest = "host", help="Ip address of server")
        parser.add_option("--mode", dest = "mode", help="Mode which idetifies how program shoud operate")
        parser.add_option("--file1", dest = "file1", help="Path of the file which contains message")
        parser.add_option("--file2", dest = "file2", help="Key or json file according to mode")
    (options,arguments) = parser.parse_args()
    if sys.argv[1] == "client":
        client = Client(options.host, options.p, options.mode)
        client.connect()
        client.send_server(options.file1, options.file2)
    else:
        server = Server(options.p)
        server.start()

if __name__ == "__main__":
    main()
