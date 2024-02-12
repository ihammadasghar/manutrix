import colorama
from colorama import Fore
colorama.init(autoreset=True, convert=True)

HELP = f""" - {Fore.GREEN}matrix {Fore.BLUE}name dimensions {Fore.GREEN} -> Create a matrix
 - {Fore.GREEN}random {Fore.BLUE}name dimensions {Fore.GREEN} -> Create a random matrix
 - {Fore.GREEN}show {Fore.BLUE}name {Fore.GREEN} -> Create a random matrix
 - {Fore.GREEN}cls -> Clear screen
 - {Fore.GREEN}add {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Add two matrixes
 - {Fore.GREEN}sub {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Subtract two matrixes
 - {Fore.GREEN}mult {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Multiply two matrixes
 - {Fore.GREEN}trans {Fore.BLUE}matrix_name new_matrix_name {Fore.GREEN} -> Transpose of a matrix
 - {Fore.GREEN}sym {Fore.BLUE}name {Fore.GREEN} -> Check if a matrix is symmetrical
 - {Fore.GREEN}det {Fore.BLUE}matrix_name new_constant_name {Fore.GREEN} -> Calculate and save the determinant of a matrix as a constant
 - {Fore.GREEN}inv {Fore.BLUE}matrix_name inverse_matrix_name {Fore.GREEN} -> Calculate and save the inverse of a matrix as a new matrix
 - {Fore.GREEN}joinv {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Join matrixes verticaly and save as new
 - {Fore.GREEN}joinh {Fore.BLUE}matrix1 matrix2 new_matrix_name {Fore.GREEN} -> Join matrixes horizontaly and save as new
 - {Fore.GREEN}+row {Fore.BLUE}matrix_name{Fore.GREEN} -> Add a row to a existing matrix
 - {Fore.GREEN}+col {Fore.BLUE}matrix_name{Fore.GREEN} -> Add a column to a existing matrix
 - {Fore.GREEN}-row {Fore.BLUE}matrix_name n{Fore.GREEN} -> Remove nth row
 - {Fore.GREEN}-col {Fore.BLUE}matrix_name n{Fore.GREEN} -> Remove nth column"""