import computer

tests = [
    "6x -20 = 0",
    "5x = 5x",
    "4 = 8",
    "5.5 = 4 + 7.2x",
    "5 + 13.1x + 3x^2 = 1 + 1x",
    "5 + 3x + 3x^2 = 1 + 0",
    "3x^3 + 2x+2 + 1x + 1 = 0",
    "5 + x + 4*x + x^2",
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    "5 * X^0 + 4 * X^1 = 4 * X^0",
    "5/2x^2 - 4x + 8"
]

print("Running tests:")
print("")

for test in tests:
    print(test)
    computer.exec(test)
    print("")

print("Tests complete")