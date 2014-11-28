
def horner(x, *polynomial):
    result = 0
    for coefficient in polynomial:
        result = result * x + coefficient
    return result
