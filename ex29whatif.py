people = 20
cats = 30
dogs = 15

if people < cats:
  print "Too many cats! The world is doomed!."

if people > cats:
  print "Not many cats! The world is saved!"

if people < dogs:
  print "The world is drooled on."

if people > dogs:
  print "The world is dry!"

dogs += 5

if people >= dogs:
  print "People are greater than or equal to dogs."

if people <= dogs:
  print "People are less than or equal to dogs."

if people == dogs:
  print "People are dogs."

if people == cats and people < cats:
  print "This should be false and will not appear."

if not (people == cats and people < cats):
  print "This should be True. Cats, people!"

if cats != dogs:
  print "This is also True. Cats are not dogs."

if people != cats or cats == dogs:
  print "People are not also not cats. And that is true enough to print."

if not (people != cats or dogs == 200):
  print "Then this will be reversed, into false, and not printed."

if not (dogs == 200 and people != dogs):
  print "Then these false statements will be reversed and this will be printed."
  print "And cats WILL be people!"
  


# Study Drills
# What do you think the "if" does to the code under it?
  # The if operator makes an equality True/False operation and then prints the code depending on whether the return value is True or False
# Why does the code under the if need to be indented four spaces
  # The code under the if is indented because the if operates similarly to a function
# What happens if it isn't indented?
  # The code will not run due to syntax error
# Can you put other boolean expressions from Exercise 27 in the if statement? Try it 
  # 
