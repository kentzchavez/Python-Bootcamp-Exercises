# Variables provided by the course
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculation
amount = round(((bill/people) * ((tip/100)+1)),2)
print(f"\n[] Each person should pay: ${amount}")
