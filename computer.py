import sys
import computer_functions as cf

def main():
    if len(sys.argv) != 2:
        print("invalid number of arguements")
        return False

    exec(sys.argv[1])

def exec(input):
    if validate_input(input):
        try:
            calc(input)
        except Exception as e:
            print("there was an error")
            print(e)

def calc(equation):
    coeffs = cf.init_equation(equation)

    print("Reduced Form:", cf.reduced_form_tostring(coeffs))
    print("Polynomial Degree:", len(coeffs) - 1)

    if cf.left_equals_right(coeffs):
        print("solution is all real numbers")
        return

    if (len(coeffs) - 1 > 2):
        print("degree is too damn high")
        return
    
    if (len(coeffs) - 1 == 2):
        cf.quadratic(coeffs[2], coeffs[1], coeffs[0])
        return
    
    if (len(coeffs) - 1 == 1):
        print("solution is:", cf.solve_linear(coeffs[1], coeffs[0]))
        return
    
    if (len(coeffs) == 1 and not coeffs[0] == 0):
        print("no solution")

def validate_input(input):
    for char in input:
        if not ((char.isdigit()) or (char in "+-*/ =.^xX")):
            print("invalid character in input")
            return False
    
    return True

if __name__ == '__main__':
    main()
