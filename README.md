# Exam Practice

## Task 1 - Functions
the correct syntax for functions in python is `def "function name"():`, followed by the indented content of the function in the following lines (which can simply be replaced with `pass`. Either way something needs to be present in the function content).
```commandline
def user_name(): # correct function call, which acquires user's name via input() funtion
    return input("Please enter your name: ")

user_name()
```
## Task 2 - Control Flow
Controlling the flow of the code by using techniques such as if statements, while loops and for loops to iterate through code.

```commandline
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
```

## Task 3 - Operators & Boolean Expression
Boolean is a data type, meaning to be one or the other. Therefore a boolean can either be `True` or `False`. Think of it like binary, it can only be 1 or 0, on or off.
```commandline
input_required = True # condition for while loop
```
```commandline
        input_required = False # boolean is set to false
```
Operators in python (and other languages), operators are used to perform tasks pertaining to variables and values. There are several types:

### Arithmetic Operators

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `%` modulos (divisional remainder)
- `**` exponentiation
- `//` floor division

### Logical Operators

- `and` implementing another condition
- `or` allowing for selection of another condition
- `not` requiring negation of another condition

### 