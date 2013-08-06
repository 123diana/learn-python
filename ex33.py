i = 0
numbers = []

while i < 6:
  print "At the top i is %d" % i
  numbers.append(i)
  
  i = i + 1
  print "Numbers now: ", numbers
  print "At the bottom i is % d" % i

print "The numbers: "

# This begins a new function?? It begins after the while loop as run its course.
# But how is num defined? Does it just print "numbers" instead?"
for num in numbers:
  print num