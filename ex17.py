# Copying Python script to copy one file to another
from sys import argv
from os.path import exists

script, from_file, to_file = argv


# we could do these two on one line too, how?

indata = open(from_file).read() ; to_file = open(to_file 'w').read ; to_file.write(indata) 
print "length equals %d %s" (len(indata), exists(to_file))

print "Alright, all done."

