# This line is an import, which is how you add features, or modules, to your feature set
from sys import argv
# This line lists the filename as the argument, the variable that holds the arguments 
# that you pass to your script
script, filename = argv
# This line opens the file that you listed as your argument
txt = open(filename)
# This line is a short print
print "Here's your file %r:" % filename
# This line gives a command for the text. The . is used to give a file a command. 
# The read command tells the txt to do the read command without any parameters
print txt.read()
# This is another line of print
print "Type the filename again:"
# This uses raw input to give the file name. the ">" simply makes a carrot before the raw 
# input
file_again = raw_input ("> ")
# This opens the file listed in the raw input
txt_again = open(file_again)

print txt_again.read()

f = open("ex15_sample.txt")
for line in f:
	print line
f.close()
