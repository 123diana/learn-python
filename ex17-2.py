# Copying Python script to copy one file to another
from sys import argv
from os.path import exists

script, T1, T2 = argv

print "Copying from %s to %s" % (T1, T2)

# we could do these two on one line too, how?

indata = open(T1).read() 
print "The input file is %d long and the output file exists %s" % (len(indata), exists(T2))
print "Ready, hit RETURN to continue, Control-C to abort."
raw_input("Hit it")

T2 = open(T2, 'w').write(indata)

print "Alright, all done."

