import re

def strip_space(string):
    return string.replace(" ", "")

def highest_degree(equation):
    max_degree = 0

    for i in range(0, len(equation)):
        if equation[i] == '^':
            degree = int(equation[i + 1])
            if degree > max_degree:
                max_degree = degree

    return max_degree

#larger than 10
#larger than 2
def valid_degrees(equation):
    for i in range(0, len(equation)):
        if equation[i] == '^':
            degree = int(re.search('\d+|$', equation[i:]).group())
            if not (0 <= degree <= 2):
                return False

    return True
