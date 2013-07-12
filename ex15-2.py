print "Which file do you want to open? "
file = raw_input("> ")
txt = open(file)
print txt.read()

print "What do you like to eat? "
eat = raw_input()
# This method of raw_input puts the answer on the next line

print "So, you like to eat %s." % (eat)

food = raw_input("What do you like to eat? ")
# This method of raw_input puts the answer right after the question
print "So you like to eat %s." % food

print "Which file do you want to open? "
file_again = raw_input("- ")
print "Here is your file %s. " % file_again
txt = open(file_again)
print txt.read()
