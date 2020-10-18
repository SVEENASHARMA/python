# Create a variable called 'name' that holds a string
name = "Sveena Sharma"

# Create a variable called 'country' that holds a string
country = "USA"

# Create a variable called 'age' that holds an integer
age = 25    

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 1700

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8

# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Print out "Hello <name>!"
print("Hello " + name + "!")
print(f"Hello {name}!")

# Print out what country the user entered
print("You live in the " + country)
print(f"You live in {country}")

# Print out the user's age
print("You are " + str(age) + " years old")
print(f"You are {age} years old")

# With an f-string, print out the daily wage that was calculated
print(f"You make {daily_wage} per day")
print("You make " + str(daily_wage) + " per day")

# With an f-string, print out whether the users were satisfied
print(f"Are you satisfied with your current wage? {satisfied}")
print("Are you satisfied with your current wage? " + str(satisfied))
