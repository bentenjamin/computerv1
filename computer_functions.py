import re

DEGREE_MAX = 2

def strip_space(string):
    return string.replace(" ", "")

def highest_degree(terms):
    max_degree = 0

    for term in terms:
        max_degree = max(get_degree(term), max_degree)

    return max_degree

def get_degree(term) -> int:
    return int(term[term.index("^") + 1:])

#larger than 10
#larger than 2
def valid_degrees(terms):
    for term in terms:
        if not (0 <= get_degree(term) <= DEGREE_MAX):
            return False
 
    return True

#add in *X^0 to constants for easier calculation later
def constant_indeterminate_inserter(equation):
    i = 0

    while i <= len(equation):
        if equation[i].isdigit() and i != len(equation) and not equation[i + 1].isdigit() :
            equation = equation[:i] + "*X^0" + equation[i:]
            i += 4
        i += 1
    
    return equation

#returns a list containing the adition of coeffecients of indeterminates where the index is the degree
def list_added_indeterminates(equation):
    sign = 1
    l_or_r_of_equ = 1
    coefficients = []

def invert_sign(term):
    return term[1:] if '-' in term else "-" + term

def remove_pos(term):
    return term.replace("+", "")

def rhs_to_lhs(equation):
    split = equation.split("=")

    lhs_terms = re.findall("([+-]?[^-+]+)", split[0])
    rhs_terms = re.findall("([+-]?[^-+]+)", split[1])

    lhs_terms = list(map(remove_pos, lhs_terms))
    rhs_terms = list(map(remove_pos, rhs_terms))

    rhs_terms = list(map(invert_sign, rhs_terms))

    return lhs_terms + rhs_terms