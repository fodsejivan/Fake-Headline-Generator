# import random module
import random
#Create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group Of Monkeys",
    "Prime Minister Modi",
    "Auto Rikshaw Driver From Delhi"
]
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]
places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a Plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]
# Start The Headline Generation Loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {places_or_thing}"
    print ("\n" + headline)
    user_input = input("\n DO YOU WANT ANOTHER HEADLINE? (Yes/No)").strip().lower()
    if user_input == "no":
        break
# Print Goodbye message
print("\nThanks For Using The Fake Headline Generator. Have A Fun Day")