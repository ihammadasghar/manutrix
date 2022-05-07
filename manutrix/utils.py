def dot_product(a: list, b: list) -> float:
    len_a = len(a)
    len_b = len(b)
    if len_a == len_b:
        multiplied_elements = [(a[i]*b[i]) for i in range(len_a)]
        return sum(multiplied_elements)
    return None
    