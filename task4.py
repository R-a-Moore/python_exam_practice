
# declare a list
jacks_kids = ["X.K4", "Beelzebub", "Donna"]

#declare a tuple
matts_kids = ("Anantashesha the primordial consumer", "the unchangable abyss")

#declare a dictionary
children = {
    "Sam's children" : "Mara",
    "Xena's children" : ["Xolotl", "Misha"],
    "Jack's children" : jacks_kids,
    "Matt's children" : matts_kids
}

gods = { # a nested dictionary containing multiple
    "pantheon 1" : {
        "big god" : "he is big",
        "small god" : "she is small"
    },
    "pantheon 2" : {
        "many headed god" : "has many heads",
        "one legged god" : "has one leg"
    }
}

#adding/removing/modifying a list
jacks_kids.remove("Donna") # remove from a list
jacks_kids.append("Shah Hazda Mohammed II") # add to end of a list
jacks_kids[0] = "Jonathan Joestar"

try: # try catch exception used, as you can't add or remove from a tuple, they are immutable
    matts_kids.remove("Anantashesha the primordial consumer")
except:
    print("You can't kill the universe, kid!")

# adding/removing/modifying a dictionary
children("Sam's children").remove() # remove the key value
# present list, tuple, dictionary