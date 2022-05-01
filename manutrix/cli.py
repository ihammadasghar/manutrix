from matrix import matrix

def main():
    #  Session data
    matrixes = {}
    
    while True:
        commands = input().split(" ")
        command = commands[0].upper()

        if command == "EXIT":
            break

        elif command == "MATRIX":
            if correct_args(commands, 1):
                name = commands[1]
                dims = input("Dimensions (e.g 3x3): ")
                rows, cols = map(int, dims.split("x"))
                new_matrix = matrix()

                for i in range(rows):
                    row = input(f"Row {i}: ")
                    row = list(map(float, row.split(" ")))
                    if len(row) == cols:
                        new_matrix.add_row(row)
                        continue
                    print("Not enough elements.\n")
                
                matrixes[name] = new_matrix
                print(f"Matrix {name} added.\n")
        
        elif command == "RANDOM":
            if correct_args(commands, 1):
                name = commands[1]
                dims = input("Dimensions (e.g 3x3): ")
                rows, cols = map(int, dims.split("x"))
                new_matrix = matrix()
                new_matrix.random(rows, cols)
                matrixes[name] = new_matrix
                print(f"Matrix {name} added.\n")
        
        elif command == "SHOW":
            if correct_args(commands, 1):
                name = commands[1]
                print(matrixes[name].matrix)

        elif command == "MULT":
            if correct_args(commands, 2):
                a, b = commands[1:]
                result = matrixes[a].multiply(matrixes[b])
                print_matrix(result)

        elif command == "ADD":
            if correct_args(commands, 2):
                a, b = commands[1:]
                result = matrixes[a].add(matrixes[b])
                print_matrix(result)

        elif command == "SUB":
            if correct_args(commands, 2):
                a, b = commands[1:]
                result = matrixes[a].subtract(matrixes[b])
                print_matrix(result)

        elif command == "SCALE":
            if correct_args(commands, 2):
                n, name = commands[1:]
                result = matrixes[name].scale(int(n))
                print_matrix(result)
        
        elif command == "ADDROW":
            pass
        
        elif command == "ADDCOL":
            pass

        elif command == "TRANSPOSE":
            pass

        elif command == "SYM":
            pass


def print_matrix(matrix):
    for rows in matrix:
        print(rows)

def correct_args(commands, n):
    if len(commands) == n+1:
        return True
    print(f"Required number of arguments is {n}")
    return False
                
            