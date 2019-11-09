"""
Created on NOV 10 12:53 2019
@author: devi
"""
from title import *
import os
import subprocess, sys
import msv

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

class welcome_to_the_new_hell:
    def starting_head(self):
        title_head()
    def get_id(self):
        self.usr_id = input("please enter the user id".title())
        return self.usr_id
    def get_password(self):
        self.usr_password = input("please enter the password".title())
        return self.usr_password
    def print_id_and_password(self):
        print(self.usr_id)
        print(self.usr_password)

if __name__ == '__main__':
    c = welcome_to_the_new_hell()
    c.starting_head()
    c.get_id()
    c.get_password()
    c.print_id_and_password()
    #opener ="open" if sys.platform == "darwin" else "xdg-open"
    #subprocess.call([opener,'/home/devi/Downloads/song1.mp3'])
