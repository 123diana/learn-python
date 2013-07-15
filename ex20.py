# This is the line in which we import an argument value
# Argument values are passed in from the command line using argv
# argv is a module from the system, which is the python library
from sys import argv

# This establishes that the argument value is in the input file
# argv is an array
# an_array = [1, "b", sys]
# an_array = [1, "b", "geeK", [3, 4, 5, [6, 7] ] ]
# an_array[3][3][0] => 6
# argv = [argument1, argument2, argumentN]
script, input_file = argv

# This creates a function that reads the file
def print_all(f):
	print f.read()

# This creates a function that will go back to the beginning of the file after it has been read	
def rewind(f):
	f.seek(0)

# This defines a function that will print one line of the file, as specified by line_count .
def print_a_line(line_count, f):
	print line_count, f.readline()

# This line defines the value of current_file as the opened input_file, 
# The in_put file is the second variable assigned to that argument
current_file = open(input_file)

# This is just a string
print "First, let's print the whole file:\n"

# This calls up the function print_all, which reads the file assigned to the value current_file
print_all(current_file)

# This is just a string
print "Now let's rewind, kind of like a tape."

# This calls up the function to go back to the beginning of the current_file that is opened.
rewind(current_file)

# This is just a string
print "Let's print three lines:"

# This assigns a number value to the variable current_line to be used in the function
current_line = 1
# This calls up the function to print a single line, with the line_count defined by current_line
print_a_line(current_line, current_file)

# This adds another line to the current line, which is 1, making it line 2
current_line = current_line + 1
# This calls up the function, which now prints line 2
print_a_line(current_line, current_file)

# This adds another line to the current line, which is 2, making it line 3
current_line = current_line + 1
# This calls up the function, which now prints line 2
print_a_line(current_line, current_file)

# Now I'm going to figure out what += means and do this shit all over again

# This function brings me back to the start. Oh, take me back to the star-ar-art
rewind(current_file)

# += is used is an Add And operator, so that c += a is equivalent to c = c + a

print "Now I will print the lines again."

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print "Now let's go backwards!\n"

current_line -= 1
print_a_line(current_line, current_file)

current_line -= 1
print_a_line(current_line, current_file)

print "Well, that went backwards, but it did not read the current line!"

current_line -= 1
print_a_line(current_line, current_file)

current_line -= 1
print_a_line(current_line, current_file)

print "Still not reading the lines."
print "How about if I do this the old-fashioned way."

rewind(current_file)

current_line = 3
print_a_line(current_line, current_file)

current_line -= 1
print_a_line(current_line, current_file)

current_line -= 1
print_a_line(current_line, current_file)

print "Okay, so it appears that we are never reading the line number itself"
print "Current_line just sets a value for us, which is the first number that appears in the string"
print "Every time the file is read, it begins from line 1???"






