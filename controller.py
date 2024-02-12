#  Session data
matrixes = {}
constants = {} 

def get_matrix(name):
    try:
        matrix = matrixes[name]
    except KeyError:
        return None
    return matrix


def get_matrixes():
    return matrixes


def save_matrix(name, matrix):
    matrixes[name] = matrix


def get_constant(name):
    try:
        val = constants[name]
    except KeyError:
        return None
    return val


def save_constant(name, value):
    constants[name] = value