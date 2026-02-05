while True:

    want_instructions = input("Do you want to know the instructions?").lower

    #check if user says yes or no
    if want_instructions == "yes" or want_instructions == "y":
        print("You said yes!")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("You said no!")
        break
    else:
        print("please enter 'yes' or 'no'")
        continue
print("we done")