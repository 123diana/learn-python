def boomshaka(booms, shakas):
	print "How many booms does it take to boomshaka? %d booms." % booms
	print "How many shakas does it take to boomshaka? %d shakas. \n" % shakas

print "Let's call this mofo up."
boomshaka(20, 40)

print "I SAID: How many BOOMS does it take to SHAKA?"
booms = 200
shakas = 400

boomshaka(200, 400)

print "Count them again, pig. Count them again."
booms = 200
shakas = 400

boomshaka(booms + 30, shakas + 60)

print "Hey-O!!!"
boomshaka(50 + 60, 40 + 10)

print "Hey! Hey you! I gotta few questions for you?"
q1 = raw_input("How many booms do you think it takes to boomshaka?\n")
q2 = raw_input("How many shakas do you think it takes to boomshaka?\n")

booms = int(q1)
shakas = int(q2)

boomshaka(booms, shakas)
