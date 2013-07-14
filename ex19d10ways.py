print "Now I will find ten ways to call up a function."

# First, I will create the function.

def ten10_ways_of_calling_up_a_function(value1, value2, value3):
	print "This morning, I ate %s." % value1
	print "For lunch, I ate %s." % value2
	print "For dinner, I ate %s.\n" % value3

print "This is call number one:"

ten10_ways_of_calling_up_a_function("eggs", "ham", "green eggs and ham")

print "This is call number two:"

value1 = "grits"
value2 = "grits"
value3 = "more grits"

ten10_ways_of_calling_up_a_function(value1, value2, value3)

print "This is call number three:"
print "(I am already running out of ways to call up this function.)"

ten10_ways_of_calling_up_a_function(value1, value2, value3)

value1 = "macaroni and cheese"
value2 = "strawberry rhubarb ice cream"
value3 = "your mom!"


print "This is call number 4:"
print ten10_ways_of_calling_up_a_function("hope", "love", "faith")
# Because line 33 started with a print, but there was no actual string, the string will read none.

print "This is call number 5:"
value1 = raw_input("What did you eat for breakfast? " )
value2 = raw_input("What did you eat for lunch? " )
value3 = raw_input("What did you eat for dinner? " )

ten10_ways_of_calling_up_a_function(value1, value2, value3)


print "This is call number 6, or it is simply more practice with raw input."
print "What did you eat for breakfast?"
value1 = raw_input()
print "What did you eat for lunch?", #having this comma here keeps the answer on the same line
# Without the comma, the answer will be prompted for on the next line
value2 = raw_input()
print "What did you eat for dinner?"
value3 = raw_input()

ten10_ways_of_calling_up_a_function(value1, value2, value3) #or more raw input fun

print "This is call number 7, or EVEN MORE FUN with raw input."

from sys import argv
script, value1, value2, value3 = argv

ten10_ways_of_calling_up_a_function(value1, value2, value3)

# BOOYA! That totally worked!

print "This is call number 8, if I can muster a call number 8."
print "All right. I did a good enough job. B+ student!"





