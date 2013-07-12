print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
# Snow is not a variable, because it has quotes around it. Variables do not have quotes. 
print "And everywhere that Mary went."
print "." * 10 # what'd that do?

# Good to remember to put quotes around variable definitions. Variable names do not need quotes. 
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# The comma adds a space between the two words. Without the comma, it becomes one word
# These two strings are separated because in Python it is bad form to use more than 80 characters in a line

print end3 + end9 + end11 + end5

print "shit " * 8
print end7 * 8 + end11 * 3

