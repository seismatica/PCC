filename = "C:\Projects\PCC\pcc-1\chapter_10\pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())