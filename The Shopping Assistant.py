'''
4. Nested Quick Decisions: The Shopping Assistant 🛍️
Objective:

To practice the use of nested shorthand if statements in assisting a shopping decision.

Task 1: Code Correction

You are provided with a Python script that is supposed to assist in shopping, but it has errors. Identify and fix them.

Buggy Code:

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather = "sunny" else "umbrella" if weather = "rainy" else "sweater"
print(clothing)
Task 2: Clothing Recommendation

Based on the corrected code from Task 1, further enhance the program to recommend additional items like "hat" or "boots" based on the weather.

Task 3: Accessory Recommendation

Based on the clothing recommendation, suggest an accessory. For instance, if "sunglasses" were recommended, suggest "sunscreen" as an accessory.
'''
# Task one.
'''
weather = input("Enter the weather: sunny, rainy, hot, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater" 
print(clothing)
'''

# Task Two. 
'''
weather = input("Enter the weather: sunny, rainy, snowing, hot, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater" if weather == "cold" else "t-shirt" if weather == "hot" else "coat"
print(clothing)
'''

# Task three.


weather = input("Enter the weather: sunny, rainy, snowing, hot, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater" if weather == "cold" else "t-shirt" if weather == "hot" else "coat"
outfit = "hat" if clothing == "sunglasses" else "rain jacket" if clothing == "umbrella" else "pants" if clothing == "sweater" else "shorts" if clothing == "t-shirt" else "heavy pants"
accessory = "sunscreen" if outfit == "hat" else "rain boots" if outfit == "rain jacket" else "boots" if outfit == "pants" else "sandals" if outfit == "shorts" else "winter gloves"

print(clothing, "and", outfit, "is what we suggest with an accessory of", accessory)