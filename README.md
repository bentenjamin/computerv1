# Computerv1

a simple polynomial equation solver for linear and quadratic equations

It will always be considered that the input is well formatted, ie. all terms are of the format a\*X^b. The powers are well ordered and all present

# Usage
> python3 comupter.py "5x^2 + 2x +5" <br>

To run a batch of examples: <br>

>python3 tests.py
# Features:
- highest degree is 2
- spaces or no spaces
- implicit multiplication of coefficient (can be written ax)
- upper or lower case X
- implicit degree of 1
- implicit coefficient of 1
- lexicon checking
- reduced form output
- fraction coefficients
- multiple terms of same exponents in any order
- decimal coefficients
- dont need '= 0'
- better reducing (removing zero coefficient terms)

# examples

quadratic_example = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" <br>
linear_example = "5 * X^0 + 4 * X^1 = 4 * X^0"

>"6x -20 = 0" <br>
"5x = 5x" <br>
"4x = 8x" <br>
"5.5 = 4 + 7.2x" <br>
"5 + 13.1x + 3x^2 = 1 + 1x" <br>
"5 + 3x + 3x^2 = 1 + 0" <br>
"3x^3 + 2x+2 + 1x + 1 = 0" <br>
"5 + x + 4*x + x^2" <br>
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" <br>
"5 * X^0 + 4 * X^1 = 4 * X^0" <br>
"4x^2 -28x +49"
