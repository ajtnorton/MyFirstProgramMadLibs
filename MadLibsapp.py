name_author = input("Enter your name: ")
name_author_gender = input("Are you a boy or a girl? Please enter: ")
if name_author_gender == "boy":
    name_author_genderpronoun = "he"
    name_author_genderpronoun2 = "his"
if name_author_gender == "girl":
    name_author_genderpronoun = "she"
    name_author_genderpronoun2 = "her"
name_other = input("Enter a friend's name: ")
adjective_b = input ("Enter an adjective (like beautiful, big, nasty, something like that): ")
adjective_a = input ("Enter another adjective (like ugly, small, sweet, something like that): ")
animal = input ("Enter an animal: ")
animal_name = input ("Enter an adjective ending with 'y' (like silly, snuggly, tricky): ")
place = input ("Enter a place you like to go (like park, library, zoo): ")
print("This is a story by " + name_author + ".")
print("A long time ago, in a faraway kingdom, there lived a " + adjective_a + " " + name_author_gender + " named " + name_author + ".")
print("And " + name_author_genderpronoun + " had a " + adjective_b + " friend named " + name_other + ".")
print(name_author_genderpronoun.capitalize() + " also had a pet " + animal + " named " + animal_name.capitalize() + ".")
print("One day, " + name_author + " lost " + name_author_genderpronoun2 + " pet " + animal + ".")
print("\"Oh no!\" " + name_author_genderpronoun + " cried. \"I don't know where " + animal_name.capitalize() + " is!\"")
print("But just then " + name_other + " walked through the door. \"Sorry, I took " + animal_name.capitalize() + " for a walk in the " + place + "!\"")
print("And everyone laughed and was happy. The end.")
