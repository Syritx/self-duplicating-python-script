import random
import subprocess
import time
import os

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
name = ""

def create_file():
    global name

    for i in range(20):
        rand_letter = random.choice(letters)
        name += rand_letter

    file = open('{name}.py'.format(name=name), 'w+')

    command = ['python3', '{filename}.py'.format(filename=name)]
    this_file = open('source.txt', 'r')
    source = ''

    for l in this_file:
        source += l

    file.write(source)


def execute():
    global name

    time.sleep(1)
    print("hi")
    os.system('python3 {f}.py'.format(f=name))


create_file()
execute()