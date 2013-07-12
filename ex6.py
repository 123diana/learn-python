# This sets up the variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# When there are multiple variables, the variable name needs to go in parentheses, separated by a comma.
# This is an example of a string inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# These next two lines are also examples of a string inside a string. 
print "I said: %r" % x
print "I also said: '%s'" % y

hilarious = False
# I'm not sure where %r comes from. Oh wait. %d is for digits. %s is for strings. %r is for ???
# %r is for debugging. 
# Still not clear what this line is doing. 
joke_evaluation = "Isn't that joke so funny?! %r"

# Not sure what this line is doing.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# This adds the strings together to create a longer string.
print w + e
print e + w 
