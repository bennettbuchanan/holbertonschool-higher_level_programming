'''Program written by Bennett Buchanana for Holberton School. This program asks the user for the price of a meal, the sales tax in percentage and the would like to tip they would like to make in percentage. It then prints the total cost of the meal adding all of these variables.'''

# Print the welcome message to output
print "Welcome to the taxes and tip calculator!"
# Ask the user to input the price
print "What is the price before tax?",
# Store the user's input in the variable price_before
price_before = raw_input()
# Ask the user to input the tax in percentage
print "What are the taxes? (in %)",
# Store the user's input in the variable taxes
taxes = raw_input()
# Ask the user to input the tip they would like to make
print "What do you want to tip? (in %)",
# Store in the user's input in the variable tip
tip = raw_input()
# Transform tax into decimal form and define it as a float
taxes_percentage = float(taxes) * .01
# Transform tip into decimal form and define it as a float
tip_percentage = float(tip) * .01
# Find the total cost of the tax
tax_total = float(price_before) * float(taxes_percentage)
# Add the total cost of the tax with the price_before
price_after_taxes = float(price_before) + tax_total
# Find the tip total with the cost after taxes are applied
price_after_tip = price_after_taxes * tip_percentage
# Add the price with taxes and the tip cost to find the total cost
total = price_after_tip + price_after_taxes
# Print the total cost to the output for the user
print "The price you need to pay is: $%.6f." % total
