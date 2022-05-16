from tkinter import HORIZONTAL
from matrix import matrix
import os
from settings import HELP
import controller as ctlr
import colorama
from colorama import Fore
colorama.init(autoreset=True, convert=True)


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
        
        elif command == "HELP":
            print(HELP)

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
            if correct_args(arguments, 1):
                add_col(*arguments)

        elif command == "TRANS":
            if correct_args(arguments, 2):
                transpose_matrix(*arguments)

        elif command == "SYM":
            if correct_args(arguments, 1):
                validate_symmetry(*arguments)

        elif command == "-ROW":
            if correct_args(arguments, 2):
                remove_row(*arguments)

        elif command == "-COL":
            if correct_args(arguments, 2):
                remove_col(*arguments)

        elif command == "DET":
            if correct_args(arguments, 2):
                determinant(*arguments)

        elif command == "INV":
            if correct_args(arguments, 2):
                inverse(*arguments)

        elif command == "JOINV":
            if correct_args(arguments, 3):
                join_vertical(*arguments)

        elif command == "JOINH":
            if correct_args(arguments, 3):
                join_horizontal(*arguments)

        print("")



def intro():
    os.system("cls")
    print(f"{Fore.GREEN}Smart functions to manipulate any 2D matrix.\nUse command 'functions' to list all functions.")


def print_matrix(matrix):
    for rows in matrix.matrix:
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
        
    ctlr.save_matrix(name, new_matrix)
    print(f"{Fore.GREEN}Matrix {name} created.")


def make_random_matrix(name, dims):
    rows, cols = map(int, dims.split("x"))
    new_matrix = matrix()
    new_matrix.random(rows, cols)
    ctlr.save_matrix(name, new_matrix)
    print(f"{Fore.GREEN}Matrix {name} created.")


def show_matrix(name):
    if name.upper() == "ALL":
        matrixes = ctlr.get_matrixes()
        for name, matrix in matrixes.items():
            print(f"{Fore.BLUE}Matrix {name} {matrix.get_dims()}:")
            print_matrix(matrix)
            print("\n")
        return

    matrix = ctlr.get_matrix(name)
    if matrix:
        print(f"{Fore.BLUE}Matrix {name} {matrix.get_dims()}:")
        print_matrix(matrix)
        return
    print(f"{Fore.RED}Matrix {name} doesn't exist.")


def multiply_matrix(a, b, name):
    matrix_a = ctlr.get_matrix(a)
    matrix_b = ctlr.get_matrix(b)
    result = matrix_a.multiply(matrix_b)
    save_matrix(name, result)


def add_matrix(a, b, name):
    matrix_a = ctlr.get_matrix(a)
    matrix_b = ctlr.get_matrix(b)
    result = matrix_a.add(matrix_b)
    save_matrix(name, result)


def save_matrix(name, result):
    ctlr.save_matrix(name, result)

    print(f"{Fore.GREEN}Result saved at matrix {name}.")

    show_matrix(name)


def subtract_matrix(a, b, name):
    matrix_a = ctlr.get_matrix(a)
    matrix_b = ctlr.get_matrix(b)
    result = matrix_a.subtract(matrix_b)
    save_matrix(name, result)


def scale_matrix(name, n):
    result = ctlr.get_matrix(name).scale(int(n))
    save_matrix(name, result)


def transpose_matrix(matrix, name):
    result = ctlr.get_matrix(matrix).transpose()
    save_matrix(name, result)


def validate_symmetry(name):
    is_sym = ctlr.get_matrix(name).is_symmetrical()
    if is_sym:
        print(f"{Fore.GREEN}Matrix {name} is symmetrical.")
        return
    print(f"{Fore.RED}Matrix {name} is not symmetrical.")


def add_row(name):
    while True:
        matrix = ctlr.get_matrix(name)
        row = input(f"{Fore.BLUE}Row: ")
        row = list(map(float, row.split(" ")))
        if len(row) == matrix.cols:
            matrix.add_row(row)
            print(f"{Fore.GREEN}Row added to matrix {name}.")
            show_matrix(name)
            return
        print(f"{Fore.RED}{matrix.cols} elements required in each row.")


def add_col(name):
    while True:
        matrix = ctlr.get_matrix(name)
        col = input(f"{Fore.BLUE}Column: ")
        col = list(map(float, col.split(" ")))
        if len(col) == matrix.rows:
            matrix.add_col(col)
            print(f"{Fore.GREEN}Column added to matrix {name}.")
            show_matrix(name)
            return
        print(f"{Fore.RED}{matrix.rows} elements required in each column.")


def remove_row(matrix_name, row_num):
    ctlr.get_matrix(matrix_name).remove_row(int(row_num))
    print(f"{Fore.GREEN}Row {row_num} removed from {matrix_name}.")
    show_matrix(matrix_name)


def remove_col(matrix_name, col_num):
    ctlr.get_matrix(matrix_name).remove_col(int(col_num))
    print(f"{Fore.GREEN}Col {col_num} removed from {matrix_name}.")
    show_matrix(matrix_name)


def save_constant(name, c):
    ctlr.save_constant(name, c)
    print(f"{Fore.GREEN}Constant {c} saved as {name}.")


def determinant(matrix_name, name):
    det = ctlr.get_matrix(matrix_name).determinant()
    print(f"{Fore.GREEN}|{matrix_name}| = {det}")
    save_constant(name, det)


def inverse(matrix_name, name):
    result = ctlr.get_matrix(matrix_name).inverse()
    save_matrix(name, result)


def join_vertical(matrix_a, matrix_b, name):
    b = ctlr.get_matrix(matrix_b)
    result = ctlr.get_matrix(matrix_a).join(b, horizontal=False)
    save_matrix(name, result)


def join_horizontal(matrix_a, matrix_b, name):
    b = ctlr.get_matrix(matrix_b)
    result = ctlr.get_matrix(matrix_a).join(b, horizontal=True)
    save_matrix(name, result)