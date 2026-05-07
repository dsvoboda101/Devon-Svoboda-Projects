# HorseOrganizer
#### Video Demo:  <URL HERE>

## 📌 Description

**HorseOrganizer** is a command-line tool to manage a list of sale horses for the sport of eventing. It allows users to:

1. 🔍 **Search** available horses based on:
   - Maximum budget
   - Desired competition level
   - Age range
        - *Tier I matches*: meet all three criteria
        - *Tier II matches*: match budget and one other criteria

2. ➕ **Add** a new horse to the list of available horses
3. ❌ **Remove** a sold horse from the list of available horses


## How to use HorseOrganizer.

HorseOrganizer operates through command line arguments.
- To search available horses use `buy_horse`.
- To add a new horse use `new_horse`.
- To remove a horse use `sold_horse`.
- Follow the prompts to provide search criteria or edit the list of available horses.


## Required Files

HorseOrganizer requires an included file called `horses.csv` which contains a current list of horses. Each horse entry includes:
- Name
- Age
- Sex
- Level
- Cost

Data Safety: Before making changes, HorseOrganizer automatically makes a timestamped backup file of `horses.csv`.


## Key Concepts - Levels of Eventing

HorseOrganizer often refers to the "level" of horses.  This indicates the levels of an equestrian sport called eventing or combined training.  The following levels (in descending order) or terms will be recognized:
- Advanced
- Intermediate
- Modified
- Training
- Novice
- Beginner Novice
- Intro
- Started (indicates a horse is in training but not ready for competition)
- Retired (indicates a horse that has retired from competition)
- Unknown


## Key Concepts - Inputting Horse Gender

HorseOrganizer uses equestrian sepecific terms to refer to the sex of horses, as opposed to male or female. The following terms will be recognized:
- Mare (or M) is a female horse
- Stallion (or S) is a male horse
- Gelding (or G) is a castrated male horse
- Filly is a female horse under 4 years old
- Colt is a male horse under 4 years old
- Unknown


## Installations

HorseOrganizer requires `pip install w2n`


## Detailed Description for CS50P

**Getting Started**
`main()` detects the command line argument (CLA) and calls `arg_valid()`. If `arg_valid()` determines that the CLA is one of the three accepted, it returns `True` and `main()` directs the program down one of three branches. If `len(CLA) != 2` or if the CLA is not one of those accepted, an appropriate error message is displayed and the program exits.

**Functionality #1: Searching Sale Horses**
If `buy_horse` is entered, `main()` calls `main_buy()`. `main_buy()` opens `horses.csv` and reads it into `horses = []` as a list of dictionaries.  `main_buy()` then calls three functions on `horses` to sort them into new lists based on specific criteria.

**#1** `level(horses)` asks the user for the level they want to search on (see Key Concepts above for details) and stores it as `ask_level`. It then calls `level_list(horses, ask_level)`.
  - If the input is one of the accepted levels, `level_list` makes a list called `horses_level` which contains all the horses in `horses.csv` that are at that level of eventing.  This list is returned to `level(horses)` which then returns it to `main_buy()`.
  - If the input is not valid, the user gets a message `Level Not Recognized` and a while loop in `level(horses)` repeatedly asks the user for a level until a valid level is entered.

**#2** `age(horses)` asks the user for a range of horses' ages and stores it as `ask_age`. It then calls `age_list(horses, ask_age)`.

- Extensive effort was put in so that `age_list` accepts as many formats for `ask_age` as were imagined by the programmer. This was done in three steps. **(1)** Words were substituted for corresponding numbers using the dictionary `ages` found at the top of the file.  This dictionary was used instead of `w2n` to limit acceptable ages to 25 (which is very old for a horse). **(2)** `ask_age` was compared to a regex designed to pick out the digits of the youngest and oldest ages  from surrounding characters.**(3)** `age_list` iterated over `horses` and appended every horse with an age within the acceptable range to a list called `horses_age`. Example accepted formats include:

  - 8-10
  - 8 to 10 years
  - eight to ten
  - 8 to ten years old

- `age_list(horses, ask_age)` returns `horses_age` to `age(horses)` which then returns it to `main_buy()`.

- If the `ask_age` input is not valid, the error message `Please enter a valid age range` is displayed and a while loop in `age(horses)` repeatdly asks the user for input until a valid age range is entered.

**#3** `cost(horses)` asks the user for their maximum budget to spend on a horse and stores it as `ask_cost`. It first calls `convert_budget(ask_cost)` to convert the budget to a usable format. It then calls `cost_list(horses, budget)` to generate the list `horses_cost`.

  - `convert_budget(ask_cost)` accepts as many formats for `ask_cost` as were imagined by the programmer by matching the input to a regex and pulling out the `number`. That number is then converted to an integer called `budget` and returned to `cost(horses)`.  If `ask_cost` doesn't match the regex and cannot be converted to a number through `int(w2n.word_to_num(ask_cost))`, the user receives the error message `Please enter valid number` and is again asked to input their maximum budget. Examples of accepted formats include:

    - 25000
    - 25,000
    - $25,000 dollars
    - 25000$
    - 25K
    - twenty-five thousand dollars

  - `cost_list(horses, budget)` iterates over `horses` and appends any horse with cost less than or equal to the budget into a list called `horses_cost`.  `horses_cost` is returned to `cost(horses)` which returns `horses_cost` to `main_buy()`.

**Search Output** `main_buy()` accepts `horses_level`, `horses_age`, and `horses_cost`. It then iterates over `horses_cost` and if a horse is present in all three lists, it is appended to `triple_match`.  If a horse is in `horses_cost` and one other list, it is appended to `double_match`. `horses_cost` was selected as the necessary criteria to promote responsible spending when buying horses. The results of the search are then printed out for the user, with distinctions between horses in `triple_match` and `double_match`. If either list is empty, an appropriate message is printed to inform the user. Example output is shown here:

  `Here are some horses you should try!`

  `Eli is 9 year old gelding, competes at novice level, and costs 40000 dollars.`

  `Sophie is 7 year old mare, competes at novice level, and costs 30000 dollars.`

  `Summer is 8 year old mare, competes at novice level, and costs 25000 dollars.`



  `You could also take a look at these horses.`

  `Hobbes is 8 year old gelding, competes at training level, and costs 45000 dollars.`

  `Kiva is 7 year old mare, competes at started level, and costs 15000 dollars.`

  `Poppy is 6 year old mare, competes at beginner novice level, and costs 20000 dollars.`

**Functionality #2: Adding a Sale Horse**
If `new_horse` is entered, `main()` calls `main_new()`. `main_new()` opens `horses.csv` and reads it into `horses = []` as a list of dictionaries.  In order to prevent data loss, `main_new()` first reads `horses = []` back into a new csv file with a timestamp in the file name. `main_new()` then asks the user for the necessary information to add a new horse to `horses = []`, starting with asking for the horse's name. For the remaining inputs, `main_new()` calls the following functions: `get_age()`, `get_sex()`, `get_level()` and `get_cost()`.

**#1** `get_age()` asks the user for the age of the horse, replaces any words corresponding to numbers from the dictionary `ages` and calls `check_age(age)` to verify that the input is valid. If `check_age(age)` returns `True`, `get_age()` returns the age to `main_new()`.  If `check_age(age)` returns `False`, the user is informed and asked again to input the age.

**#2 and #3** `get_sex()` and `get_level()` each ask the user for their respective inputs and call `check_sex(sex)` or `check_level(level)`, respectively, to verify that the input is within the list of acceptable terms (see Key Concepts for details). If the input is valid the check function returns `True`. Otherwise it returns `False` and the user is asked to input again.

**#4** `get_cost()` asks the user for the cost of the horse, stores it as `ask_cost` and then calls `convert_budget(ask_cost)` to convert the input into an integer.  By reusing the function, I was able to accept the same range of formats without extending the length of the program. If `ask_cost` can be converted into an integer, `get_cost()` returns the cost to `main_new()`.

**Output Edited File**  `main_new()` accepts the four inputs and, combined with the name, appends the results to `horses` as a new dictionary. It then writes the list back to `horses.csv`.  The final result is a sorted list of all available horses, now including the recently added horse.
  - By backing-up and re-writing `horses.csv`, the new horse is searchable in future sessions.


**Functionality #3: Removing a Sale Horse**
If `sold_horse` is entered, `main()` calls `main_sold()`. `main_sold()` opens `horses.csv` and reads it into `horses = []` as a list of dictionaries. Just like `main_new()`, `main_sold()` saves a copy of `horses.csv` with a timestamp in the file name before editing `horses.csv`. `main_sold()` then calls `remove_horse(horses)`.  `remove_horse(horses)` asks the user which horse they want to remove from the list.  If the input matches the value of the key "name" for a horse in `horses`, that horse is removed from the list `horses` and the new version of horses is returned to `main_sold()`. If the input doesn't match, the user is informed and asked again. `main_sold()`  then writes the list back to `horses.csv`.  The final result is a sorted list of all available horses, notably missing the horse which was removed.

  - By backing-up and re-writing `horses.csv`, the removed horse is no longer searchable in future sessions.

**Unit Tests**

`test_project.py` contains unit tests for the following functions (imported from `project.py`):
- `level_list`
- `age_list`
- `convert_budget`
- `cost_list`
- `check_age`
- `check_level`
- `check_sex`


## License and Credits

HorseOrganizer was developed by Devon Svoboda as a final project for EdX: Harvard CS50P: CS50's Introduction to Programming with Python (https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/home).
Project submitted on June 18th, 2025
All academic integrity guidelines were followed.
