import sys
import csv
import re
from word2number import w2n
from datetime import datetime

ages = {
    "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6,
    "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10, "eleven": 11, "twelve" : 12,
    "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, "sixteen" : 16, "seventeen" : 17,
    "eighteen" : 18, "nineteen" : 19, "twenty" : 20, "twentyone" : 21, "twentytwo" : 22,
    "twentythree" : 23, "twentyfour" : 24, "twentyfive" : 25,
}

def main():
    if arg_valid() == True:
        if sys.argv[1] == "buy_horse":
            main_buy()
        if sys.argv[1] == "new_horse":
            main_new()
        if sys.argv[1] == "sold_horse":
            main_sold()

# Opens and reads horses.csv, calls functions to generate horses_level, horses_age and horses_cost.
# If a horse is in all three lists it goes into triple_match; if horses is in horses_cost and one other list, it goes in double_match (promotes responsible spending).
# Prints response to user.  Relevant functions continue to line 156.
def main_buy():
    horses = []
    with open("horses.csv", "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            horses.append(line)
        horses_level = level(horses)
        horses_age = age(horses)
        horses_cost = cost(horses)
        triple_match = []
        double_match = []
        for horse in horses_cost:
            if horse in horses_age and horse in horses_level:
                triple_match.append(horse)
            elif horse in horses_age or horse in horses_level:
                double_match.append(horse)
            else:
                pass
        if triple_match != []:
            print(f"\nHere are some horses you should try! ")
            for horse in triple_match:
                print(f"{horse["name"]} is {horse["age"]} year old {horse["sex"]}, competes at {horse["level"]} level, and costs {horse["cost"]} dollars.")
        if triple_match == [] and double_match != []:
            print("No perfect matches were found, however...")
        if double_match != []:
            print(f"\nYou could also take a look at these horses. ")
            for horse in double_match:
                print(f"{horse["name"]} is {horse["age"]} year old {horse["sex"]}, competes at {horse["level"]} level, and costs {horse["cost"]} dollars.")
        if triple_match == [] and double_match == []:
            print("No suitable matches were found.")

#Get desired level of eventing from user with loop to ask again if the input isn't valid.
def level(horses):
    while True:
        try:
            ask_level = input("What level horse are you looking for? ").strip().lower()
            horses_level = level_list(horses, ask_level)
            if horses_level:
                return horses_level
        except:
            pass

# Generate a list of horses at user's desired level called horses_level.
def level_list(horses, ask_level):
    levels = ["started", "intro", "beginner novice", "novice", "training", "modified", "preliminary", "intermediate", "advanced", "retired"]
    if ask_level in levels:
        horses_level = [horse for horse in horses if horse["level"] == ask_level]
        return horses_level
    else:
        print("Level Not Recognized")

#Get desired age range from user with loop to ask again if the input isn't valid.
def age(horses):
    while True:
        try:
            ask_age = input("What age range are you looking for? ").lower().strip()
            horses_age = age_list(horses, ask_age)
            if horses_age:
                return horses_age
        except:
            pass

# Generate a list of horses within user's desired age range called horses_age.
def age_list(horses, ask_age):
    horses_age = []
    for word, digit in ages.items():
        ask_age = ask_age.replace(word, str(digit))
    pattern = r"^(?P<youngest>\d{1,2})\s*(?:to|-)\s*(?P<oldest>\d{1,2})(?:\s*[a-zA-Z]*)*?$"
    match = re.fullmatch(pattern, ask_age)
    if match:
        youngest = int(match.group("youngest"))
        oldest = int(match.group("oldest"))
        if youngest >=1 and oldest <=25:
            for horse in horses:
                age = int(horse["age"])
                if youngest <= age <= oldest:
                    horses_age.append(horse)
            return horses_age
        else:
            print("Please enter a valid age range")
    else:
        print("Please enter a valid age range")

#Get desired maximum monetary budget from user with loop to ask again if the input isn't valid.
def cost(horses):
    while True:
        try:
            ask_cost = input("What is your maximum budget? ").strip().lower()
            budget = convert_budget(ask_cost)
            horses_cost = cost_list(horses, budget)
            if horses_cost:
                return horses_cost
        except:
            print("Please enter valid number")

# Convert the user's budget to a an integer; accepts a variety of formats.
def convert_budget(ask_cost):
    pattern =r"^\$?(?P<number>(?:\d{1,3}(?:,\d{3})*|\d+)(?:k)?)(?:(?:\s*)?[a-zA-Z\$]+)?$"
    match = re.search(pattern, ask_cost)
    try:
        if match:
            number = match.group("number")
            if "k" in number:
                number = number.replace("k", "")
                budget = (int(number)*1000)
                return budget
            elif "," in number:
                number = number.replace(",", "")
                budget = int(number)
                return budget
            else:
                budget = int(number)
                return budget
        else:
            budget = int(w2n.word_to_num(ask_cost))
            return budget
    except:
        print("Please enter valid number")

# Generate a list of horses within user's desired budget called horses_cost.
def cost_list(horses, budget):
    horses_cost = []
    for horse in horses:
        try:
            cost = int(horse["cost"])
            if cost <= budget:
                horses_cost.append(horse)
        except ValueError:
           print("Please enter valid number.")
    return horses_cost

# Adds new horse to horses.csv. Relevant functions continue to line 248.
def main_new():
    horses = []
    today_date = datetime.now()
    with open("horses.csv", "r") as file, open(f"horses_{today_date}.csv", "w") as copy:
        reader = csv.DictReader(file)
        for line in reader:
            horses.append(line)
        writer = csv.DictWriter(copy, fieldnames = reader.fieldnames)
        writer.writeheader()
        for horse in sorted(horses, key=lambda horse: horse["name"]):
            writer.writerow({"name": horse["name"], "age": horse["age"], "sex": horse["sex"], "level": horse["level"], "cost": horse["cost"]})
    name = input("Name: ").strip().capitalize()
    age = get_age()
    sex = get_sex()
    level = get_level()
    cost = get_cost()
    if check_age(age) == True and check_sex(sex) == True and check_level(level) == True:
        horses.append({"name": name, "age": age, "sex": sex, "level": level, "cost": cost})
    with open("horses.csv", "w") as added_horse:
        writer = csv.DictWriter(added_horse, fieldnames = reader.fieldnames)
        writer.writeheader()
        for horse in sorted(horses, key=lambda horse: horse["name"]):
            writer.writerow({"name": horse["name"], "age": horse["age"], "sex": horse["sex"], "level": horse["level"], "cost": horse["cost"]})

#Asks for age of new horse.
def get_age():
    while True:
        age = input("Age: ").strip().lower()
        for word, digit in ages.items():
            age = age.replace(word, str(digit))
        if check_age(age):
            return age
        else:
            print("Please enter valid age.")

# Verifies age of new horse.
def check_age(age):
    if age == "unknown":
        return True
    try:
        age = int(age)
        if 1 <= age <= 25:
            return True
    except ValueError:
        return False

# Asks for sex of new horse.
def get_sex():
    while True:
        sex = input("Sex (M/G/S): ").strip().lower()
        if sex == "m":
            sex = "mare"
        elif sex == "g":
            sex = "gelding"
        elif sex == "s":
            sex = "stallion"
        else:
            pass
        if check_sex(sex):
            return sex
        else:
            print("Please enter valid sex (M/G/S).")

#Verifies sex of new horse.
def check_sex(sex):
    sexes = ["mare", "gelding", "stallion", "filly", "colt", "unknown"]
    if sex in sexes:
        return True
    else:
        return False

# Asks for level of new horse.
def get_level():
    while True:
        level = input("Level: ").strip().lower()
        if check_level(level):
            return level
        else:
            print("Please enter valid level.")

# Verifies level of new horse.
def check_level(level):
    levels = ["started", "intro", "beginner novice", "novice", "training", "modified", "preliminary", "intermediate", "advanced", "retired", "unknown"]
    if level in levels:
        return True
    else:
        return False

# Asks for cost of new horse.
def get_cost():
    while True:
        ask_cost = input("Price: ").strip().lower()
        cost = convert_budget(ask_cost)
        if cost > 0:
            return cost

# Opens and reads horses.csv, makes new csv without the removed horse.
def main_sold():
    horses = []
    today_date = datetime.now()
    with open("horses.csv", "r") as file, open(f"horses_{today_date}.csv", "w") as copy:
        reader = csv.DictReader(file)
        for line in reader:
            horses.append(line)
        writer = csv.DictWriter(copy, fieldnames = reader.fieldnames)
        writer.writeheader()
        for horse in sorted(horses, key=lambda horse: horse["name"]):
            writer.writerow({"name": horse["name"], "age": horse["age"], "sex": horse["sex"], "level": horse["level"], "cost": horse["cost"]})
    horses = remove_horse(horses)
    with open("horses.csv", "w") as added_horse:
        writer = csv.DictWriter(added_horse, fieldnames = reader.fieldnames)
        writer.writeheader()
        for horse in sorted(horses, key=lambda horse: horse["name"]):
            writer.writerow({"name": horse["name"], "age": horse["age"], "sex": horse["sex"], "level": horse["level"], "cost": horse["cost"]})

# Asks which horse should be removed and removes horse from list.
def remove_horse(horses):
    while True:
        sold_horse = input("Which horse would you like to remove from the barn? ").strip().capitalize()
        for horse in horses:
            if sold_horse == horse["name"]:
                horses.remove(horse)
                return horses
        else:
            print("Horse not found. ")

# Determines if the command line arguments are valid.
def arg_valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    else:
        pass
    if sys.argv[1] == "new_horse" or sys.argv[1] == "buy_horse" or sys.argv[1] == "sold_horse":
        return True
    else:
        sys.exit("Enter new_horse or sold_horse to edit the registry.  Enter buy_horse to get recommendations from the barn.")

if __name__ == "__main__":
    main()

