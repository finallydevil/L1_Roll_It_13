
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

# Main routine

# testing loop...
while True:
    want_instructions = yes_no("Do you want to know the instructions? ")
    print(f"you chose {want_instructions}")

print("we done")