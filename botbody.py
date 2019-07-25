"""
Created on Tue May 28 19:50:10 2019
@author: devi
"""
import os
import shutil
from os import path
from sys import stdin,stdout
import datetime
from title import *

def copy_paste_of_file(file_name):
    if path.exists(file_name):
        src_of_file=path.realpath(file_name)
    head,tail=path.split(src_of_file)
    stdout.write("Path of file: "+head)
    stdout.write("File name: "+tail)
    
    dst_of_file=src_of_file + ".bak"                                           #making backup of a file 
    shutil.copy(src_of_file,dst_of_file)                                        #real copy making using shutil
    
def yes_sir():                                                                  # Sir function for respect
    stdout.write("YES SIR")                                                     # make all 3 functions of sir modified according to the question of the user.

def no_sir():
    stdout.write("NO SIR")
    
def sir():
    stdout.write("SIR")

def print_welcome_greetings():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        stdout.write('Good Morning Sir...')
    elif 12 <= currentTime.hour < 18:
        stdout.write('Good AfterNoon Sir...')
    else:
        stdout.write('Good Evening Sir...')
        
#def make_spell_correct():                                                     #for command
#def make_sys_clear():
#def game():

title_head()                                            # welcome print          
print_welcome_greetings()                               # welcome greetings for the user.

#system clear to be done

stdout.write("What can I do for you?")                                                #taking command
command=stdin.readline()
if command=='nothing':
    stdout.write("SO DO YOU WANT TO PLAY A GAME...")
    game=stdin.readline()
    if game=="YES":
        game_func()
    else:
        pass
else:
    #complete the process
    stdout.write("The process name is : "+command)
    list_of_command=['copy','cut','music']  #make the list as file to store all the commands
    if command not in list_of_command:
        list_of_command.append(command)
        stdout.write("COMMAND DOESN'T EXIST")
        stdout.write("PLEASE make the command process")
    else:
        if command=="copy": #make all the commands in make_spell_checker func.
            #check process for copy
            file_name=stdin.readline()
            copy_paste_of_file()
        elif command=="cut":
            #make process for cut
        elif command=="music":
            #also make a music folder
            #make process for music folder
            print("Hell")
