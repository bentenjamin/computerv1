import re

DEGREE_MAX = 2

# all functions assume reduced form q = 0 (besides reduce_equation)


def strip_space(reduced):
    return reduced.replace(" ", "")


def highest_degree(terms):
    max_degree = 0

    for term in terms:
        max_degree = max(get_degree(term), max_degree)

    return max_degree


def get_degree(term) -> int:
    return int(term[term.index("^") + 1:])

# larger than 10
# larger than 2


def valid_degrees(terms):
    for term in terms:
        if not (0 <= get_degree(term) <= DEGREE_MAX):
            return False

    return True

# replace x with X
# add X to constants
# add coeff if missing
# add power if missing


def normalise(terms):
    for i in range(len(terms)):
        terms[i] = terms[i].replace("x", "X")

        if (terms[i].find("X") == -1):
            terms[i] += "*X^0"
        else:
            if (terms[i].find("^") == -1):
                terms[i] += "^1"
            if (terms[i][0] == "X"):
                terms[i] = "1*" + terms[i]

        if (terms[i].find("*") == -1):
            terms[i] = terms[i].replace("X", "*X")

    return terms


def get_coefficient(term):
    coeff = term[:term.index("X") - 1]

    if (coeff.find("/") == -1):
        return float(coeff)
    
    nums = coeff.split("/")

    return (float(nums[0]) / float(nums[1]))
    #float(re.search("[+-]?\d*[\.]?\d*(?:(?:[eE])[+-]?\d+)?", term).group())

# returns a list containing the addition of coeffecients of same indeterminates where the index is the degree


def add_terms(terms):
    coefficients = [0] * (highest_degree(terms) + 1)

    for term in terms:
        coefficients[get_degree(term)] += get_coefficient(term)

    return coefficients


def invert_sign(term):
    return term[1:] if '-' in term else ("-" + term)


def remove_pos(term):
    return term.replace("+", "")


def rhs_to_lhs(equation):
    split = equation.split("=")

    lhs_terms = re.findall("([+-]?[^-+]+)", split[0])
    rhs_terms = re.findall("([+-]?[^-+]+)", split[1])

    lhs_terms = [remove_pos(term) for term in lhs_terms]
    rhs_terms = [remove_pos(term) for term in rhs_terms]

    rhs_terms = [invert_sign(term) for term in rhs_terms]

    return lhs_terms + rhs_terms

# linear equation where ax + b = 0


def solve_linear(a, b):
    return (-1 * (b / a))

# i is 1 or -1 to give the 2 different roots


def quadratic_roots(a, b, c, i):
    return ((-1 * b) + (i * (sqrt(calc_discriminant(a, b, c))))) / (2 * a)

# quadratic equation where ax^2 + bx + c = 0


def solve_quadratic(a, b, c):
    return (quadratic_roots(a, b, c, 1), quadratic_roots(a, b, c, -1))


def reduced_form_tostring(coeffecients):
    reduced = ""

    for i in range(len(coeffecients) - 1, 1, -1):
        reduced += f'{coeffecients[i]:g}' + " * X ^ " + str(i) + " + "
    reduced += f'{coeffecients[1]:g} * X + {coeffecients[0]:g}' + " = 0"

    return reduced


def reduce_equation(equation):
    return add_terms(rhs_to_lhs(equation))


def sqrt(num):
    return num**0.5


def calc_discriminant(a, b, c):
    return ((b**2) + ((-4) * a * c))
