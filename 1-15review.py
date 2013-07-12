print """
\tthis is an indented line \n\tthis is one the next line 
"""

food = "bacon"
drink = "milk"
side = "hashbrowns"

print "I need to buy %s\\%s\\%s" % (food, drink, side)

another_item = raw_input ("What do you need at the store? ")
prompt = "> "
# ? What exactly does the prompt on line 12 do? I thought it made a carrot or some other 
# symbol in front of the answer to the question

print "I will add %s to the list. " % another_item

first_item = raw_input ("What is the first item? ")
second_item = raw_input ("What is the second item? ")
prompt = "> "

print "The first item on the list is %s and the second item is %s." % (first_item, second_item)


milk = 1
bacon = 3

print "The cost of milk is %d and the cost of bacon is %d." % (1, 3)
price = raw_input("How many cartons of milk do you need? ")
prompt = "> "
# How can I make it so that the answer to the question will appear on the next line?
number = raw_input (prompt)
cost = number * milk

# ? How can I put in a number to the raw_input on line 26 so that whatever the answer 
# to the question is can be used to calculate the cost?
# To use the value used from the raw_input(question) you can use value = raw_input (prompt)

print "That will cost", cost, "dollars."

# raw_input() put the question into the parenthesis and it will be asked. 
# the answer to the question will equal the value set for raw_input
# numbers do not go inside prints




