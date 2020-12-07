import sys
import computer_functions as cf

quadratic_example = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
linear_example =  "5 * X^0 + 4 * X^1 = 4 * X^0"
ex = cf.strip_space(quadratic_example)

if len(sys.argv) != 2:
    raise Exception("Invalid number of arguements")

#terms = cf.rhs_to_lhs(ex)

#reduced = cf.reduce_equation(ex)

# = cf.add_terms(terms)

# print("equation:", sys.argv[1])

# print(cf.highest_degree(ex))

# print(cf.valid_degrees(ex))

#print(cf.rhs_to_lhs(ex))

#print(cf.valid_degrees(terms))

#print(cf.constant_indeterminate_inserter(terms))

#print(cf.add_indeterminates(terms))

#print(cf.solve_linear(added_terms[1], added_terms[0]))

#print(cf.reduced_form_tostring(cf.reduce_equation(ex)))

#print(cf.solve_quadratic(reduced[2], reduced[1], reduced[0]))

#print(reduced)

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

    if (len(coeffs) - 1 > 2):
        print("degree is too damn high")
        return
    
    if (len(coeffs) - 1 == 2):
        quadratic(coeffs[2], coeffs[1], coeffs[0])
        return
    
    if (len(coeffs) - 1 == 1):
        print("solutions are:", cf.solve_linear(coeffs[1], coeffs[0]))
        return
    
    if (len(coeffs) == 1 and not coeffs[0] == 0):
        print("invalid equation")

def init_equation(equation):
    equation = cf.strip_space(equation)
    terms = cf.rhs_to_lhs(equation)
    terms = cf.constant_indeterminate_inserter(terms)
    coeffs = cf.add_terms(terms)
    return coeffs

calc(sys.argv[1])

