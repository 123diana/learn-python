# This chapter is about variables. Variables can be set for numbers and things.
# In this exercise, variables are embedded into format strings.
# Format strings are marked off using "string"
# Placement of variables depends on the syntax %
# I think %d is for numbers, like %digit
# And %s is for text. I might be wrong.  
# The number 1 cannot be used as a variable

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

a = 'berries'
b = 'flour'
c = 'sugar'
d = 'raspberry'
f = 'mango'

print "This recipe calls for %s" % b
print "You can also add %s and %s" % (a, c)
print "Do not add %s or %s" % (d, f)
