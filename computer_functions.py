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


def valid_degrees(terms):
    for term in terms:
        if not (0 <= get_degree(term) <= DEGREE_MAX):
            return False

    return True

# replace x with X
# add X to constants
# add coeff if missing
# add power if missing
# insert * for implicit multiplication


def normalise(terms):
    for i in range(len(terms)):
        terms[i] = terms[i].replace("x", "X")

        if (terms[i].find("X") == -1):
            terms[i] += "*X^0"
            continue

        if (terms[i].find("^") == -1):
            terms[i] += "^1"

        if (terms[i][0] == "X"):
            terms[i] = "1*" + terms[i]
        elif (terms[i][1] == "-") and (terms[i][1] == "X"):
            terms[i] = "-1*" + terms[i]
        elif (terms[i].find("*") == -1):
            terms[i] = terms[i].replace("X", "*X")

    return terms


def get_coefficient(term):
    coeff = term[:term.index("*")]

    if not (coeff.find("/") == -1):
        fraction = coeff.split("/")
        return (float(fraction[0]) / float(fraction[1]))

    return float(coeff)
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


def split_to_terms(equation):
    terms = re.findall("([+-]?[^-+]+)", equation)
    terms = [remove_pos(term) for term in terms]
    return terms


def rhs_to_lhs(equation):
    split = equation.split("=")

    terms = split_to_terms(split[0])

    if (len(split) == 2):
        terms += [invert_sign(term) for term in split_to_terms(split[1])]

    return terms

# linear equation where ax + b = 0


def solve_linear(a, b):
    return (-1 * (b / a))

# i is 1 or -1 to give the 2 different roots


def quadratic_roots(a, b, c, i):
    return ((-1 * b) + (i * (sqrt(calc_discriminant(a, b, c))))) / (2 * a)

# quadratic equation where ax^2 + bx + c = 0


def reduced_form_tostring(coeffecients):
    reduced = ""

    for i in range(len(coeffecients) - 1, 0, -1):
        reduced += f'{coeffecients[i]:g}' + " * X ^ " + str(i) + " + "

    reduced += f'{coeffecients[0]:g}' + " = 0"

    return reduced.replace("+ -", "- ")


def reduce_equation(equation):
    return add_terms(rhs_to_lhs(equation))


def sqrt(num):
    return num**0.5


def calc_discriminant(a, b, c):
    return ((b**2) + ((-4) * a * c))


def init_equation(equation):
    equation = strip_space(equation)
    terms = normalise(rhs_to_lhs(equation))
    coeffs = add_terms(terms)
    return coeffs


def left_equals_right(coeffs):
    return not sum(coeffs)


def quadratic(a, b, c):
    discriminant = calc_discriminant(a, b, c)
    if (discriminant > 0):
        print("discriminant is positive")
        print("solutions are:", quadratic_roots(
            a, b, c, 1), quadratic_roots(a, b, c, -1))
    elif (discriminant < 0):
        print("discriminant is negative")
        print("solutions are imaginary:", quadratic_roots(
            a, b, c, 1), quadratic_roots(a, b, c, -1))
    else:
        print("discriminant is zero")
        print("solution is:", quadratic_roots(a, b, c, 1))
