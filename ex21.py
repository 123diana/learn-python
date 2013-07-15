def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b

def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b
  
def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78,4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
print "I think the answer is -4391."

print "\n"
print "Okay, now let's make some neeeeeew functions."

# This is what I would like the function to do.
def math(a, b, c):
  a + (b - c)
  return a + (b - c)

one = 12
two = 10
three = 5

print "You have %d flowers and you give %d away, but then you find %d more flowers." % (one, two, three)
print "How many flowers will you have now?"
print math(one, two, three)

print "\n"
print "Moving on....Is it time for some raaaaaaw_input??"
def magic_by_numbers(a, b, c):
  a * b * c
  return a * b * c

width = float(raw_input("How wide is your swimming pool? "))
length = float(raw_input("How long is your swimming pool? "))
depth = float(raw_input("How deep is your swimming pool? "))

print "Man, you can put %d liters of water in your swimming pool." % magic_by_numbers(width, length, depth)
print "Word.\n"

print "Now on to the last exercise."
# This is the exercise:
# Try 24 + 34 / 100 - 1023 as a start. Convert that to use the functions. 
# Now come up with your own similar math equation and use variables so it's more like a formula.

def last_exercise(a, b, c, d):
  value = a + b / c - d
  print "This is what we're going to do: a + b / c - d."
  return value

print last_exercise(20, 10, 5, 2)
print "\n"

print "Should I break down that last formula into MULTIPLE functions??"
def divide(a, b):
  a / b
  return a / b

def subtract(a, b):
  a - b
  return a - b

def add(a, b):
  a + b
  return a + b

print "All ready. Let's go."
print add(20, subtract(divide(10, 5), 2))
print subtract(add(20, divide(10, 5)), 2)
print 

    


