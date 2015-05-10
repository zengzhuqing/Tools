#!/usr/bin/python
#######################################################
# Coding Style Rule
# 1. Check line length (<80)
# 2. Make sure that no extra blank in line end
########################################################
from sys import argv

def check_line_len(filename):
    print "Checking line len for file " + filename
    print "No output means it is all right!"
    with open(filename) as f:
        i = 0
        while True:
            count = len(f.readline())
            if count == 0:
                break
            i = i + 1
            if count > 80 :
                print  "line " + str(i) + " : " + str(count) 

def check_extra_tail_blank(filename):
    print "Checking whether there are extra blanks in the end of file " + filename
    print "No output means it is all right!"
    with open(filename) as f:
        i = 0
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            i = i + 1
            if len(line) >= 2 and (line[-2] == ' ' or line[-2] == '\t'):
                print  "line " + str(i) + " has extra blanks"
        
if __name__ == "__main__":
    check_line_len(argv[1])
    check_extra_tail_blank(argv[1])
