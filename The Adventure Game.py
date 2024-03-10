'''
1. Nested Decisions: The Adventure Game 🏰
Objective:

To practice the use of nested if statements in creating a simple text-based adventure game.

Task 1: Code Correction

You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

Buggy Code:

place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")
Task 2: Setting the Scene

Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

Task 3: Default Path

If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.
'''

# Question one task one.
'''

place = input("Choose a place: forest or cave? ")


if place == "forest":
  action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":

'''
#Question one task two.
'''
place = input("Choose a place: forest or cave? ")


if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
  light_source = input("light a torch or proceed in the dark? ")
  if light_source == "light a torch":
      print("The cave opens up into a massive underground city!")
  else:
      print("You stumble and break your leg!")
'''

# Question one task three.

place = input("Choose a place: forest or cave? ")



if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
      pass


elif place == "cave":
    light_source = input("light a torch or proceed in the dark? ")
    if light_source == "light a torch":
      print("The cave opens up into a massive underground city!")
      explore = input("go to the castle or go into the great hall? ") 
      if explore == "go to the castle":
         pass
      elif explore == "go into the great hall":
         print("You fine all sorts of tressure!")
      else:
         pass
    elif light_source == "proceed in the dark":
      print("You stumble and break your leg!")
    else:
       pass


else:
  pass