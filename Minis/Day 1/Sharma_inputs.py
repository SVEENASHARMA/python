# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# Collects the user's input for the prompt "How old are you?" and converts the string to an integer.
age = int(input("How old are you? "))

# Collects the user's input for the prompt "Is input truthy?" and converts it to a boolean. Note that non-zero,
#   non-empty objects are truth-y.
trueOrFalse = bool(input("Is the input truthy? "))

boolTest = False

# Creates three print statements that to respond with the output.
print(f"My name is {name}")
print(f"I will be {age + 1} next year.")
print(f"The input was converted to {trueOrFalse}")