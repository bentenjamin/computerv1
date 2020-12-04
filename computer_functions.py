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
def constant_indeterminate_inserter(terms):
    for i in range(len(terms)):
        if (terms[i].find("*X^") == -1):
            terms[i] = terms[i] + "*X^0"

    return terms

def get_coefficient(term):
    return float(term[:term.index("X") - 1])
    #float(re.search("[+-]?\d*[\.]?\d*(?:(?:[eE])[+-]?\d+)?", term).group())

#returns a list containing the adition of coeffecients of indeterminates where the index is the degree
def add_indeterminates(terms):
    coefficients = [0] * (DEGREE_MAX + 1)

    for term in terms:
        coefficients[get_degree(term)] += get_coefficient(term)
    
    return coefficients

def invert_sign(term):
    return term[1:] if '-' in term else "-" + term

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