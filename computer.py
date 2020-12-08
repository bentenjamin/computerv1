import sys
import computer_functions as cf

quadratic_example = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
linear_example =  "5 * X^0 + 4 * X^1 = 4 * X^0"
ex = cf.strip_space(quadratic_example)

if len(sys.argv) != 2:
    raise Exception("Invalid number of arguements")

def left_equals_right(coeffs):
    return not sum(coeffs)

def quadratic(a, b, c):
    discriminant = cf.calc_discriminant(a, b, c)
    if (discriminant > 0):
        print("discriminant is positive")
        print("solutions are:", cf.solve_quadratic(a, b, c))
    elif (discriminant < 0):
        print("discriminant is negative")
        print("solution is imaginary")
    else:
        print("discriminant is zero")
        print("solution is:", cf.quadratic_roots(a, b, c, 1))

def calc(equation):
    coeffs = init_equation(equation)

    print("Reduced Form:", cf.reduced_form_tostring(coeffs))
    print("Polynomial Degree:", len(coeffs) - 1)

    if left_equals_right(coeffs):
        print("solution is all real numbers")
        return

    if (len(coeffs) - 1 > 2):
        print("degree is too damn high")
        return
    
    if (len(coeffs) - 1 == 2):
        quadratic(coeffs[2], coeffs[1], coeffs[0])
        return
    
    if (len(coeffs) - 1 == 1):
        print("solution is:", cf.solve_linear(coeffs[1], coeffs[0]))
        return
    
    if (len(coeffs) == 1 and not coeffs[0] == 0):
        print("invalid equation")

def init_equation(equation):
    equation = cf.strip_space(equation)
    terms = cf.normalise(cf.rhs_to_lhs(equation))
    coeffs = cf.add_terms(terms)
    return coeffs

calc(sys.argv[1])

# if x = y
# reduced form will do + -x
# fraction coefficients
# x -> x^1
# check if anything not x or num or symbol
# try catch the entire thing

