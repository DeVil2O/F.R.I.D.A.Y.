"""
Created on NOV 10 12:53 2019
@author: devi
"""
from title import *
import os
import subprocess, sys

def starting_head():            #make a title file and import to it
    title_head()

def check_the_command(command):
    command_list = ["play music"]
    if command in command_list:
        print("COMMAND ACCEPTED !!!")
    else:
        print("Please Enter A Valid Command")

def process_the_command(command):
    print("The Command Is Processing....")

if __name__ == '__main__':
    starting_head()
    command = input("please enter the command : ".title())
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener,'/home/devi/Downloads/song1.mp3'])

