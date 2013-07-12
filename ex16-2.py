from sys import argv

script, filename = argv

print "It's time open another another file, %." % filename
love = open(filename, 'w')

print "Let's add some text to this file"
firstline = raw_input("firstline = ")
secondline = raw_input("secondline = ")
thirdline = raw_input("thirdline = ")

love.write = firstline
love.write = ("\n")
love.write = secondline
love.write = ("\n")
love.write = ("\t") thirdline

print "Closing time."
love.close()


