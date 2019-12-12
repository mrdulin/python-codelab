import os


def change_from(lineTag):
    Lines = []
    command = "ls -al"
    lines = os.popen(command).readlines()
    for line in lines:
        if lineTag in line:
            temp = line.split(":")
            Lines.append(temp[1])
    return Lines
