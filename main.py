import re

print("My Interesting Calculator")
print("Type 'quit' to exit\n")

# Holds the result of the previously calcualted equation
previous = 0
run = True

def performMath():
    # Exits the program when the user types 'quit'
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye, person.")
        run = False
    else:
        # Ensures only numbers are entered during calculations
        equation = re.sub(' [a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            # Performs calculations
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()
