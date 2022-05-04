#  Session data
matrixes = {}


def get_matrix(name):
    try:
        matrix = matrixes[name]
    except KeyError:
        return None
    return matrix


def save_matrix(name, matrix):
    matrixes[name] = matrix