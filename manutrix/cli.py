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

                i = 0
                while i < rows:
                    row = input(f"Row {i+1}: ")
                    row = list(map(float, row.split(" ")))
                    if len(row) == cols:
                        print(f"{cols} elements required in each row.")
                        continue
                    new_matrix.add_row(row)
                    i +=1
                    
                
                matrixes[name] = new_matrix
                print(f"Matrix {name} added.")
        
        elif command == "RANDOM":
            if correct_args(commands, 1):
                name = commands[1]
                dims = input("Dimensions (e.g 3x3): ")
                rows, cols = map(int, dims.split("x"))
                new_matrix = matrix()
                new_matrix.random(rows, cols)
                matrixes[name] = new_matrix
                print(f"Matrix {name} added.")
        
        elif command == "SHOW":
            if correct_args(commands, 1):
                name = commands[1]
                print_matrix(matrixes[name].matrix)

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

        print("\n")


def print_matrix(matrix):
    for rows in matrix:
        print(rows)

def correct_args(commands, n):
    if len(commands) == n+1:
        return True
    print(f"Required number of arguments is {n}")
    return False
                
            