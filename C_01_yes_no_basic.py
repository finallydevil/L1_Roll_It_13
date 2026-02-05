want_instructions = input("Do you want to know the instructions?").lower

#check if user says yes or no
if want_instructions == "yes":
    print("You said yes!")
elif want_instructions == "no":
    print("You said no!")
else:
    print("please enter 'yes' or 'no'")