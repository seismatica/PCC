import os

filename = 'programming.txt'

with open(filename, 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()