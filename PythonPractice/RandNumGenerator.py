import random

def run_guess(answer,guess):
    if 1<=guess<=10:
        if answer==guess:
            print("Correct")
            return True
    else:
        print("enter a number between 1 and 10")

answer=random.randint(1,10)

if __name__ == '__main__':

    while True:
        try:

            guess = int(input("Enter a number"))
            print(guess)

            if (run_guess(answer,guess)):
                print("You got it")
                break
        except ValueError:
            print("enter a number between 1 and 10")

