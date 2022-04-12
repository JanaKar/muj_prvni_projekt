# '''

'''
textovy editor v1.py: Prvni projekt do Engeto Online Python Akademie
author: Jana Karbanova
email: xkarbanovaj@gmail.com
discord: JanaK#0342
'''
# '''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

users = {'bob': '123',
         'ann': 'pass123',
         'mike': 'password',
         'liz': 'pass123'}
analyzed_text = []
analyzed_text_clean = []
number_of_words = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
sum_numbers = 0
amounts={}
occurence=[]
result=[]
oddelovac = "-" * 40

username = input("username: ")
username1 = username.lower()    # to tolerate that user typed his name in capital letters
password = input("password: ")

if username1 in users and password == users[username1]:

    print(oddelovac, f"Welcome to the app, {username}", sep="\n")
    print("We have 3 texts to be analyzed", oddelovac, sep="\n")

    text_number = input("Enter a number btw. 1 and 3 to select: ")
    if text_number.isnumeric():
        text_number_checked = int(text_number)
        if 1 <= text_number_checked <= 3:
            analyzed_text = TEXTS[text_number_checked - 1].split()
            for word in analyzed_text:
                analyzed_text_clean.append(word.strip(".,?!:;()"))
                number_of_words = number_of_words + 1
            for word in analyzed_text_clean:
                titlepositive=False
                length=len(word)
                if not length in amounts:
                    amounts[length]=1
                else:
                    amounts[length] = amounts[length] + 1
                if word.istitle():
                    titlepositive=True
                    titlecase_words = titlecase_words + 1
                if word.isupper() and titlepositive==False:     # exclude counting of words like 30N, which are couted as titlecase
                    uppercase_words = uppercase_words + 1
                if word.islower():
                    lowercase_words = lowercase_words + 1
                if word.isdigit():
                    numeric_strings = numeric_strings + 1
                    sum_numbers=sum_numbers+int(word)

            for key in amounts:                                 # to change dict to list of tuple and sort
                occurence.append((key, amounts[key]))
            result=sorted(occurence)

            print(f"There are {number_of_words} words in the selected text.")
            print(f"There are {titlecase_words} titlecase words.")
            print(f"There are {uppercase_words} uppercase words.")
            print(f"There are {lowercase_words} lowercase words.")
            print(f"There are {numeric_strings} numeric strings.")
            print(f"The sum of all numbers {sum_numbers}")
            print(oddelovac, f"LEN|   OCCURENCES   |NR.      ", oddelovac, sep="\n")
            for number in result:
                stars="*" * number[1]
                print(f"{number[0]:3}| {stars:<15}|{number[1]}", sep="\n")
            print(oddelovac)

        else:
            print(oddelovac, "Wrong number, terminating the program", oddelovac, sep="\n")
    else:
        print(oddelovac, "Wrong selection, terminating the program", oddelovac, sep="\n")
else:
    print("Unregistered user, terminating the program")
