import sys
sys.path.insert(0, '../..')

def print_red(string):
    print (chr(27) + "[0;31m" + string + chr(27) + "[0m")

def print_blue(string):
    print (chr(27) + "[0;36m" + string + chr(27) + "[0m")

def print_green(string):
    print (chr(27) + "[0;32m" + string + chr(27) + "[0m")

def print_purple(string):
    print (chr(27) + "[0;35m" + string + chr(27) + "[0m")