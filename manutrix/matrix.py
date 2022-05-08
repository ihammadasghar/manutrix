from copy import deepcopy
from utils import dot_product
import random

class matrix:
    def __init__(self) -> None:
        self.rows = 0
        self.cols = 0
        self.matrix = []


    def random(self, rows, cols, start=1, end=10):
        self.matrix = [[float(random.randrange(start, end)) for _ in range(cols)] for _ in range(rows)]
        self.update_dims()


    def identity(self, rows, cols):
        self.matrix = [[1.0 if i==j else 0.0 for i in range(cols)] for j in range(rows)]
        self.update_dims()


    def get_identity(self):
        matrix = [[1.0 if i==j else 0.0 for i in range(self.cols)] for j in range(self.rows)]
        return matrix

    
    def update_dims(self):
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    
    def add_row(self, row, pos=None):
        if pos:
            self.matrix.insert(pos, row)
        else:
            self.matrix.append(row)
        self.update_dims()


    def remove_row(self, row_num):
        if row_num in range(self.rows):
            del self.matrix[row_num]
            self.update_dims()

    
    def add_col(self, col, pos=None):
        if pos:
            for i in range(self.rows):
                self.matrix[i].insert(pos, col[i])
        else:
            for i in range(self.rows):
                self.matrix[i].append(col[i])
        
        self.update_dims()

    
    def remove_col(self, col_num):
        if col_num in range(self.cols):
            for i in range(self.rows):
                del self.matrix[i][col_num]
            self.update_dims()


    def get_col(self, col_num):
        col = [row[col_num] for row in self.matrix]
        return col

    
    def set_col(self, new_col, col_num):
        for i in range(self.rows):
            self.matrix[i][col_num] = new_col[i]


    def get_row(self, row_num):
        return self.matrix[row_num]

    
    def set_row(self, new_row, row_num):
        self.matrix[row_num] = new_row


    def set_matrix(self, matrix):
        self.matrix = deepcopy(matrix)
        self.update_dims()


    def add(self, b):
        if (self.rows == b.rows) and (self.cols == b.cols):
            result_matrix = []

            for i in range(self.rows):
                sumed_row = []
                for j in range(self.cols):
                    sum_of_element = self.matrix[i][j] + b.matrix[i][j]
                    sumed_row.append(sum_of_element)
                result_matrix.append(sumed_row)
            
            return result_matrix
        return None


    def subtract(self, b):
        if (self.rows == b.rows) and (self.cols == b.cols):
            result_matrix = []

            for i in range(self.rows):
                subtracted_row = []
                for j in range(self.cols):
                    subtracted_elements = self.matrix[i][j] - b.matrix[i][j]
                    subtracted_row.append(subtracted_elements)
                result_matrix.append(subtracted_row)
                
            return result_matrix
        return None


    def multiply(self, b):
        if self.cols == b.rows:
            result_matrix = []
            for i in range(self.rows):
                multiplied_row = [dot_product(self.matrix[i], b.get_col(j)) for j in range(b.cols)]
                result_matrix.append(multiplied_row)
                
            return result_matrix
        return None

    
    def scale(self, n):
        result_matrix = self.matrix.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                result_matrix[i][j] *= n
        return result_matrix

    
    def transpose(self):
        result_matrix = []
        for i in range(self.cols):
            result_matrix.append(self.get_col(i))
        return result_matrix

    
    def is_symmetrical(self):
        if self.transpose() == self.matrix:
            return True
        return False


    def get_dims(self):
        return (self.rows, self.cols)


    def is_squared(self):
        if self.rows == self.cols:
            return True
        return False
