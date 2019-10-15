# Shellpy
Shellpy is a reverse shell command line program for sharing your terminal with others.

#Installation
Firstly Install all the required packages for this porgram through pip command.
pip command pkg_name
1.socket 
2.sys 
3.subprocess
4.OS


#How it Works ?
To use this reverse shell, two scripts need to be running

    Client.py - runs on a public server and add your host system IP  Address and then wait for connection.
    ShellPy.py - connects to a remote server and then wait for commands
    
#ToDo
Trying to make a single module script so that we can easily use this.
