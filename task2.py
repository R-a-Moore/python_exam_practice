solid_principles = ["Single responsability", "Open/close", "Liskov's substitution", "Interface segrgation", "Dependancy inversion"] #a list of 5 items, all of them string

input_required = True # condition for while loop
sentence = "Solid is cool! It's "
while input_required: # while loop which checks if input is required
    concator = ""
    for principle in solid_principles: # for loop which loops through each item in the solid_principles list, concatenating the first letter of them to a pre made string variable.
        concator += (principle[0])

    if sentence == "Solid is cool! It's SOLIDSOLID": # if statement checks if string variable is complete, half done, or not even done
        print(sentence)
        input_required = False

    elif sentence == "Solid is cool! It's SOLID":
        print("needs more solidity")
        sentence += concator

    else:
        print("There is no solid!")
        sentence += concator