'''
2. Quick Decisions: The Event Planner 🎉
Objective:

To practice the use of shorthand if statements in determining event-related decisions.

Task 1: Code Correction

You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

Buggy Code:

attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
Task 2: Venue Selection

Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.

Task 3: Catering Choices

Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".


'''
#Question two task one 
'''
attendees = int(input("Enter number of attendees: "))
print("large hall" if attendees > 100 else "conference room")
'''

#Question two task two
'''
attendees = int(input("Enter number of attendees: "))
print("large hall" if attendees > 100 else "conference room")
print("projector" if attendees > 100 else "audio system")
'''

# Question 2 task 3
attendees = int(input("Enter number of attendees: "))
food = input("Do you want vegetarian food yes or no? ")
print("large hall" if attendees >100 else "conference room")
print("projector" if attendees > 100 else "audio system")
print("Veggie Delight Caterers" if food == "yes" else "Gourmet Meals Caterers")


