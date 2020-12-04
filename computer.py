import sys
import computer_functions as cf

quadratic_example = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
linear_example =  "5 * X^0 + 4 * X^1 = 4 * X^0"
ex = cf.strip_space(linear_example)

if len(sys.argv) != 2:
    raise Exception("Invalid number of arguements")

terms = cf.rhs_to_lhs(ex)

added_terms = cf.add_terms(terms)

# print("equation:", sys.argv[1])

# print(cf.highest_degree(ex))

# print(cf.valid_degrees(ex))

#print(cf.rhs_to_lhs(ex))

#print(cf.valid_degrees(terms))

#print(cf.constant_indeterminate_inserter(terms))

#print(cf.add_indeterminates(terms))

print(cf.solve_linear_equation(added_terms[1], added_terms[0]))
