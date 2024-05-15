def calculate_imc():
    try:
        weight = float(input("Please enter your weight\n>> "))
        height = float(input("Please enter your height\n>> "))
        age = int(input("Please enter your age\n>> "))
    except ValueError:
        print('\nInvalid input. Please try again.\n')
        return calculate_imc()  # Return to the function if there is a ValueError

    imc = weight / (height * height)

    if imc < 18.5:
        print("You are underweight")

    elif imc >= 18.5 and imc < 24.9:
        print("You are at a normal weight")

    elif imc >= 25 and imc < 29.9:
        print("You are overweight")

    elif imc >= 30 and imc < 34.9:
        print("You have obesity type 1")

    elif imc >= 35 and imc < 39.9:
        print("You have obesity type 2")

    elif imc >= 40:
        print("You have obesity type 3")

    else:
        print("You have no salvation my child")
        
calculate_imc()