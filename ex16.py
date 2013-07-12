from sys import argv
# This line opens up the argument, which are the various names for the script
script, filename = argv
# In this case, the script is a filename. 
# In script, first, second, third = argv, you give the argument several variables
# argv stands for argument variable
# Line 3 unpacks the argument variable, and assigns what is typed into the argument 
#	variable to the variables entered on the left
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "And finally, we close it."
target.close()