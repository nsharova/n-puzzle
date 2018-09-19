
#!/usr/bin/python

import sys
import argparse
from pprint import pprint


def PrintErrorMessage(ErrorText):
	print (ErrorText)
	sys.exit(1)

#def ValidationPuzzle()


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=argparse.FileType())
    #parser.add_argument('-g', action='store_true', default=False)
    return parser

if __name__ == '__main__':
    parser = createParser()
    argc = len (sys.argv)
    if (argc < 2) :
        PrintErrorMessage("Error. No arguments")
    try:
        with open(sys.argv[(argc - 1)],'r') as file:
            array = []
            for row in file:
                arr = row.strip().split()
                for x in arr:
                    array.append(int(x))
            pprint(array)
    except:
         PrintErrorMessage("Error open file")



    # print(array[0])
    # print(array[1])
    # print(array[2])