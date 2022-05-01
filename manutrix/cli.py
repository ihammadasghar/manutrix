from matrix import matrix
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True, convert=True)

#  Session data
matrixes = {}

def main():
    intro()
    
    while True:
        commands = input().split(" ")
        command = commands[0].upper()
        arguments = commands[1:]

        if command == "EXIT":
            break

        elif command == "CLS":
            intro()

        elif command == "MATRIX":
            if correct_args(commands, 2):
                make_matrix(*arguments)
                
        
        elif command == "RANDOM":
            if correct_args(commands, 1):
                make_random_matrix(*arguments)
        
        elif command == "SHOW":
            if correct_args(commands, 1):
                show_matrix(*arguments)
                

        elif command == "MULT":
            if correct_args(commands, 2):
                multiply_matrix(*arguments)

        elif command == "ADD":
            if correct_args(commands, 3):
                add_matrix(*arguments)

        elif command == "SUB":
            if correct_args(commands, 2):
                subtract_matrix(*arguments)

        elif command == "SCALE":
            if correct_args(commands, 2):
                scale_matrix(*arguments)
        
        elif command == "ADDROW":
            pass
        
        elif command == "ADDCOL":
            pass

        elif command == "TRANSPOSE":
            pass

        elif command == "SYM":
            pass

        print("\n")


def intro():
    os.system("cls")
    print(f"{Fore.GREEN}Smart functions to manipulate any 2D matrix.\nUse command 'functions' to list all functions.\n")


def print_matrix(matrix):
    for rows in matrix:
        print(f"{Fore.GREEN}{rows}")


def correct_args(commands, n):
    if len(commands) == n+1:
        return True
    print(f"{Fore.RED}Required number of arguments is {n}")
    return False
                

def make_matrix(name, dims):
    rows, cols = map(int, dims.split("x"))
    new_matrix = matrix()

    i = 0
    while i < rows:
        row = input(f"{Fore.BLUE}Row {i+1}: ")
        row = list(map(float, row.split(" ")))
        if len(row) != cols:
            print(f"{Fore.RED}{cols} elements required in each row.")
            continue
        new_matrix.add_row(row)
        i +=1
        
    matrixes[name] = new_matrix
    print(f"{Fore.GREEN}Matrix {name} added.")


def make_random_matrix(name, dims):
    rows, cols = map(int, dims.split("x"))
    new_matrix = matrix()
    new_matrix.random(rows, cols)
    matrixes[name] = new_matrix
    print(f"{Fore.GREEN}Matrix {name} added.")


def show_matrix(name):
    print(f"{Fore.BLUEls}Matrix {name} {matrixes[name].get_dims()}:\n")
    print_matrix(matrixes[name].matrix)


def multiply_matrix(a, b):
    result = matrixes[a].multiply(matrixes[b])
    print_matrix(result)


def add_matrix(a, b):
    result = matrixes[a].add(matrixes[b])
    print_matrix(result)


def subtract_matrix(a, b):
    result = matrixes[a].subtract(matrixes[b])
    print_matrix(result)


def scale_matrix(name, n):
    result = matrixes[name].scale(int(n))
    print_matrix(result)
            