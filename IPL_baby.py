import random

baby_name=input("What is the baby's name?:");
baby_age = input("How old is the baby?:")
starting_weight=float(input("How much does the baby weigh (oz)?:"))
current_weight=starting_weight

def introduce_baby(baby_name, baby_age, baby_weight):
    activities = [
        "dance with a sock",
        "talk to a banana",
        "practice baby yoga",
        "chase a very slow toy",
    ]
    print("Meet", baby_name + "!")
    print("Age:", baby_age)
    print("Weight:", baby_weight, "oz")
    print(baby_name, "likes to", random.choice(activities) + ".")

introduce_baby(baby_name, baby_age, starting_weight)

eat_count = 0
drink_count = 0
mood = "awake"

def eat(current_weight, eat_count):
    current_weight += 11
    eat_count += 1
    if eat_count % 3 == 0:
        current_weight = poop(current_weight)
    return current_weight, eat_count
current_weight, eat_count = eat(current_weight, eat_count)
def drink(current_weight, drink_count):
    current_weight += 8
    drink_count += 1
    if drink_count % 3 == 0:
            current_weight = pee(current_weight)
    return current_weight, drink_count
current_weight, drink_count = drink(current_weight, drink_count)
def poop(current_weight):
    print("The baby pooped.")
    return current_weight - 5
def pee(current_weight):
    print("The baby peed.")
    return current_weight - 4
def cry():
    print("The baby is crying.")
    return "upset"
def sleep():
    print("The baby is sleeping.")
    return "content"
def display_status(baby_name, current_weight, mood, eat_count, drink_count):
    print("Name:", baby_name)
    print("Current Weight:", current_weight)
    print("Mood:", mood)
    print("Feedings:", eat_count)
    print("Drinks", drink_count)

home = False
class_complete = False

while not home and not class_complete:
    action = input(
        "Choose an action:"
        "(eat, drink, sleep, cry, status, home): "
    ).strip().lower()
    if action == "eat":
        current_weight, eat_count = eat(current_weight, eat_count)
        mood = "happy"
    elif action == "drink":
        current_weight, drink_count = drink(current_weight, drink_count)
        mood = "content"
    elif action == "sleep":
        mood = sleep()
    elif action == "cry":
        mood = cry()
    elif action == "status":
        display_status(
            baby_name, current_weight, mood, eat_count, drink_count
        )
    elif action == "home":
        home = True
    else:
        print("Unknown action — try again.")

print("the baby is home.")
