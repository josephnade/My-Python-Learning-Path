import random


def random_prediction():
    life = int(input("Please enter your life: "))
    realnumber = random.randint(1, 100)
    counter = 1
    while life > 0:
        prediction = int(input("Please enter your prediction: "))
        if prediction > realnumber:
            print("Real number is lower")
            life -= 1
            counter += 1
        elif prediction < realnumber:
            print("Real number is higher")
            life -= 1
            counter += 1
        elif prediction == realnumber:
            cong = "Congrulations. You found real number!!!"
            point = 100 / counter
            print(f"Your point is {point:1.4f}")
            print(cong.center(50, "*"))
            break
    else:
        try_content = f"You did not find real number.Real number is {realnumber} " \
                      f"If you try again please press \"y\", " \
                      "if you want to exit please enter \"n\" button: "
        try_again = input(try_content)
        while True:
            if try_again == "y":
                return random_prediction()
            elif try_again == "n":
                print("Have a nice day!")
                break
            else:
                print("You entered wrong letter please try again!")
                try_again = input(try_content)


random_prediction()
