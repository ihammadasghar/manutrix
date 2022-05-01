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
            if correct_args(arguments, 2):
                make_matrix(*arguments)
                
        
        elif command == "RANDOM":
            if correct_args(arguments, 2):
                make_random_matrix(*arguments)
        
        elif command == "SHOW":
            if correct_args(arguments, 1):
                show_matrix(*arguments)
                

        elif command == "MULT":
            if correct_args(arguments, 3):
                multiply_matrix(*arguments)

        elif command == "ADD":
            if correct_args(arguments, 3):
                add_matrix(*arguments)

        elif command == "SUB":
            if correct_args(arguments, 3):
                subtract_matrix(*arguments)

        elif command == "SCALE":
            if correct_args(arguments, 3):
                scale_matrix(*arguments)
        
        elif command == "+ROW":
            if correct_args(arguments, 1):
                add_row(*arguments)
        
        elif command == "+COL":
            pass

        elif command == "TRANS":
            if correct_args(arguments, 2):
                transpose_matrix(*arguments)

        elif command == "SYM":
            if correct_args(arguments, 1):
                validate_symmetry(*arguments)

        print("\n")


def intro():
    os.system("cls")
    print(f"{Fore.GREEN}Smart functions to manipulate any 2D matrix.\nUse command 'functions' to list all functions.")


def print_matrix(matrix):
    for rows in matrix:
        print(f"{Fore.GREEN}{rows}")


def correct_args(arguments, n):
    if len(arguments) == n:
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
    print(f"{Fore.BLUE}Matrix {name} {matrixes[name].get_dims()}:")
    print_matrix(matrixes[name].matrix)


def multiply_matrix(a, b, name):
    result = matrixes[a].multiply(matrixes[b])
    save_as_new_matrix(name, result)


def add_matrix(a, b, name):
    result = matrixes[a].add(matrixes[b])
    save_as_new_matrix(name, result)


def save_as_new_matrix(name, result):
    new_matrix = matrix()
    new_matrix.set_matrix(result)
    matrixes[name] = new_matrix
    print(f"{Fore.GREEN}Result saved at matrix {name}.")
    show_matrix(name)


def subtract_matrix(a, b, name):
    result = matrixes[a].subtract(matrixes[b])
    save_as_new_matrix(name, result)


def scale_matrix(name, n):
    result = matrixes[name].scale(int(n))
    save_as_new_matrix(name, result)


def transpose_matrix(matrix, name):
    result = matrixes[matrix].transpose()
    save_as_new_matrix(name, result)


def validate_symmetry(name):
    is_sym = matrixes[name].is_symmetrical()
    if is_sym:
        print(f"{Fore.GREEN}Matrix {name} is symmetrical.")
        return
    print(f"{Fore.RED}Matrix {name} is not symmetrical.")


def add_row(name):
    while True:
        row = input(f"{Fore.BLUE}Row: ")
        row = list(map(float, row.split(" ")))
        if len(row) == matrixes[name].cols:
            matrixes[name].add_row(row)
            print(f"{Fore.GREEN}Row added to matrix {name}.")
            show_matrix(name)
            return
        print(f"{Fore.RED}{matrixes[name].cols} elements required in each row.")
    