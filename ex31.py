print "You enter a dark room with two doors. Do you go through door #1 or door#2?"

door = raw_input("> ")

if door == "1":
  print "There's a giant bear here eating a cheesecake. What do you do?"
  print "1. Take the cake."
  print "2. Scream at the bear."
  
  bear = raw_input("> ")
  
  if bear == "1":
    print "The bear is very angry and comes after you. What do you do?"
    print "1. Take the cake and run away." 
    print "2. Take the cake and throw it at the bear."
    
    cake = raw_input("> ")
    if cake == "1":
      print "The bear is coming after you. Run faster!" 
    elif cake == "2":
      print "The bear starts licking the frosting off his face. Now is the time to run."
    else:
      print "Well, that's no good. The bear eats your face off. Good job!"
  elif bear == "2":
    print "The bear screams back at you. What is he saying?"
    
    speech = raw_input("> ")
    if speech == "Help!":
      print "The bear needs help. Will you help it?"
      print "1. Yes."
      print "2. No."
        
      help = raw_input("> ")
      if help == "1":
        print "What a good person you are. The bear eats you."
      elif help == "2":
        print "That's smart of you. Run away instead."
      else:
        print "That's a cop-out. The bear eats you."
        
    elif speech == "I love you!":
      print "The bear is in love with you! Do you love him?"
      print "1. No."
      print "2. Yes."
        
      love = raw_input("> ")
      if love == "1":
        print "You've broken the bear's heart. Now he will eat you."
      elif love == "2":
        print "Bestiality is a sin. God kills you."
      
    elif speech == "I don't know.":
      print "I guess you don't speak bear. The bear doesn't speak you, either."
      
    elif speech == "What?":
      print "I said! What did the bear say?"
        
      bear_speech = raw_input("> ")
      print "Oh. %s is nice." % bear_speech
      
    else:
      print "We don't understand you. Therefore we will eat you."
      
  else:
    print "Well doing %s is probably better. Bear runs away." % bear

elif door == "2":
  print "You stare into the endless abyss at Cthulhu's retina. What do you see?"
  seen = raw_input("> ")
  
  print "The %s is a manifestation of your childhood regret." % seen
  print "What do you do with it?"
  print "1. Eat it."
  print "2. Drink it."
  print "3. Deny it."
  
  choice = raw_input("> ")
  if choice == "1":
    print "It is so delicious, and so bitter."
  elif choice == "2":
    print "That is a tall drink of water."
  elif choice == "3":
    print "A shadow follows you, follows you, follows you."
  else:
    print "There is nothing left for you."
 
else:
  print "You stumble around and fall on a knife and die. Good job!"