"""
Created on Tue May 28 19:50:10 2019

@author: devi
"""

def sir():
    print("SIR")

#def make_spell_correct():                                                     #for command
#def make_sys_clear():
#def game():
    
print('\n\n\n'+"                                       You R on..")            #welcome print          

#system clear to be done

print("What can I do for you?")                                                #taking command
command=input()
if command=='nothing':
    print("SO DO YOU WANT TO PLAY A GAME...")
    game=input()
    if game=="YES":
        game_func()
    else:
        pass
else:
    #complete the process
    print("The process name is : "+command)
    list_of_command=['copy','paste','cut']  #make the list as file to store all the commands
    if command not in list_of_command:
        list_of_command.append(command)
        print("COMMAND DOESN'T EXIST")
        print("PLEASE make the command process")
    else:
        if command=="copy": #make all the commands in make_spell_checker func.
            #make process for copy
        elif command=="paste":
            #make process for paste
        elif command=="cut":
            #make process for cut
