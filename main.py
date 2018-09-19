# !/usr/bin/python
import sys
import argparse
from pprint import pprint


def print_error_message(error_message):
    print(error_message)
    exit()


def read_file(file_name):
    try:
        return open(file_name, 'r')
    except:
        print_error_message("Error open file")


# def ValidationPuzzle()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=argparse.FileType())
    # parser.add_argument('-g', action='store_true', default=False)
    return parser


def parse_int(string):
    try:
        return int(string)
    except:
        print_error_message("Cannot cast to int")


def validate_element(number, arr_size):
    if 0 <= number < arr_size * arr_size:
        return number
    else:
        print_error_message("Number is invalid")


if __name__ == '__main__':
    parser = create_parser()
    argc = len(sys.argv)
    if argc < 2:
        print_error_message("Error. No arguments")
    file = read_file(sys.argv[(argc - 1)])
    size = 0
    array = []
    for row in file:
        row = row.strip()
        if row.startswith("#"):
            continue
        arr = row.split()
        if size == 0:
            if len(arr) == 1:
                size = parse_int(arr[0])
                continue
            else:
                if arr[1].startswith("#"):
                    size = parse_int(arr[0])
                    continue
                else:
                    print_error_message("Cannot parse matrix size")
        if size < 3:
            print_error_message("Matrix size should be more or equal to 3")
        if not size == 0:
            if len(arr) < size:
                print_error_message("Not valid puzzle")
            if len(arr) > size and not arr[size].startswith("#"):
                print_error_message("Not valid puzzle")
            for index, value in enumerate(arr[0:size]):
                num = validate_element(parse_int(value), size)
                if num in array:
                    print_error_message("Not valid puzzle")
                array.append(validate_element(num, size))
    pprint(array)
