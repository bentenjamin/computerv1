import sys
import computer_functions as cf

example = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
ex = cf.strip_space(example)

if len(sys.argv) != 2:
    raise Exception("Invalid number of arguements")

terms = cf.rhs_to_lhs(ex)

# print("equation:", sys.argv[1])

# print(cf.highest_degree(ex))

# print(cf.valid_degrees(ex))

print(cf.rhs_to_lhs(ex))

#print(cf.valid_degrees(terms))
