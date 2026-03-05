#! /usr/bin/python3
import time
import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)
import functions

def Type_Command(command: str):
    for type in command:
        print(type, end='', flush=True)
        time.sleep(0.3)
    print()
    
def Power_onMessage():
    functions.clear()
    title = ' COMMODORE 64 BASIC V2 '.center(31, '*')
    status = '64K RAM SYSTEM  38911 BASIC BYTES FREE'
    print()
    print(title.center(40))
    print('\n', status)
    print('\nREADY.')

def List_Basic(program: str):
    Type_Command("LIST")
    try:
        file = open(program, "r")
        file_list = file.readlines()
        file.close()
        for line in file_list:
            print(line, end="")
            time.sleep(0.1)
    except FileNotFoundError:
        print(program)
    print("READY.")
    
def Load_Basic(program: str):
    command = f'LOAD"{program.upper()}",8'
    Type_Command(command)
    time.sleep(0.5) # Kurze Pause nach Enter
    
    time.sleep(2.0)
    print(f"SEARCHING FOR {program.upper()}")
    time.sleep(0.5)
    print(f"FOUND {program.upper()}")
    time.sleep(0.5)
    print("LOADING")
    time.sleep(3.0)
    print("READY.")

if __name__ == "__main__" :
    Power_onMessage()
