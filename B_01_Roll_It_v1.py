# functions here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check if user says yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter 'yes' or 'no'")


def instructions():
    """Prints instructions """

    print("""
*** Instructions ***

Roll the dice and try to win!
    """)


def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("what is the game goal? " ))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine

# ask user if they want instructions
want_instructions = yes_no("Do you want to know the instructions? ")

# display instructions if wanted
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)