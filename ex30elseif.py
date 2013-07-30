people = int(raw_input("How many people are there going to be? "))
cars = int(raw_input("How many cars are there going to be? "))
buses = int(raw_input("How many buses are there? "))

if cars > people:
  print "We should take the cars."
elif cars < people:
  print "We should not take the cars."
else:
  print "We can't decide."

if buses > cars:
  print "That's too many buses."
elif buses < cars:
  print "Maybe we should take the buses."
else:
  print "We still can't decide."

if people > buses:
  print "Alright, let's just take the buses."
else:
  print "Fine, let's stay home then."

print "Well, wait. Let's think about this."
price_of_gas = int(raw_input("How much will gas cost if we drive? "))
cost_of_cars = price_of_gas * cars

bus_ticket = int(raw_input("How much is bus fare these days? "))
cost_of_bus = bus_ticket * people

if cars < people and cost_of_cars < cost_of_bus:
  print "It would be cheaper to take the car."
elif cost_of_cars > cost_of_bus:
  print "Let's think how much it would cost to take the bus."
else:
  print "Oh God. This is just too hard."

if cars < people and cost_of_cars > cost_of_bus:
  print "The bus would be the more economical choice."
elif cost_of_cars < cost_of_bus:
  print "Let's think about taking the car again."
else:
  print "Oh God. This is just too hard."
