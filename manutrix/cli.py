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
        
        elif command == "SHOW":
            name = commands[1]
            print(matrixes[name].matrix)

        elif command == "MULT":
            a, b = commands[1:]
            result = matrixes[a].multiply(matrixes[b])
            print_matrix(result)

        elif command == "ADD":
            a, b = commands[1:]
            result = matrixes[a].add(matrixes[b])
            print_matrix(result)

        elif command == "SUB":
            a, b = commands[1:]
            result = matrixes[a].subtract(matrixes[b])
            print_matrix(result)

        

def print_matrix(matrix):
    for rows in matrix:
        print(rows)

                
            