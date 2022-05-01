import colorama
from colorama import Fore
colorama.init(autoreset=True, convert=True)

HELP = f""" - {Fore.GREEN}matrix {Fore.BLUE}name dimensions {Fore.GREEN} -> Create a matrix
 - {Fore.GREEN}random {Fore.BLUE}name dimensions {Fore.GREEN} -> Create a random matrix
 - {Fore.GREEN}add {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Add two matrixes
 - {Fore.GREEN}sub {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Subtract two matrixes
 - {Fore.GREEN}mult {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Multiply two matrixes
 - {Fore.GREEN}trans {Fore.BLUE}matrix_name new_matrix_name {Fore.GREEN} -> Transpose of a matrix
 - {Fore.GREEN}sym {Fore.BLUE}name {Fore.GREEN} -> Check if a matrix is symmetrical
 - {Fore.GREEN}+row {Fore.BLUE}name {Fore.GREEN} -> Add a row to a existing matrix
 - {Fore.GREEN}+col {Fore.BLUE}name {Fore.GREEN} -> Add a column to a existing matrix"""