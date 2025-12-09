def calc(val1, val2):
    if val2 == 0:
        return 0
    result = (val1 / val2)
    return float(result)
def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


fuel = get_input("How much fuel did you spend?\n")
distance = get_input("How many kms did you go through?\n")

if fuel <= 0 or distance <= 0:
    print("One or more inputs are incorrect! Please make sure to enter a valid input!")
    exit(0)

economy = calc(distance, fuel)
if economy == 0:
    print("Fuel efficiency cannot be zero. Please provide valid input!")
else:
    print(f"Your fuel economy was {economy:.2f}km/l")
    input("Press 'Enter' to exit")
