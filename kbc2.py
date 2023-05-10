print("                                       Welcome to KBC!!!!")

print("The rules of the game are follows:")
rules = [
    "1.You will have a topic to choose to get questions about. ",
    "2.You will be presented with 5 questions on the topic of your choice.",
    "3.You will have to answer the Questions to move on to the next one.",
    "4.You can press 0 to quit."
]
sportsq = [
    ["When was the first cricket world cup held?", "1922", "1945", "1908", "1912"],
    ["What is the national sport of india?", "Football", "Basketball", "Kabbadi", "Hockey"],
    ["Who is the captain of the indian cricket team?", "Sachin", "Dhoni", "Rohit", "Virat"],
    ["Who is the chairman of International Cricket Council?", "John Doe", "Amy Adam", "Joe Goldberg", "Greg Barclay"],
    ["What is the national sport of USA?", "Basketball", "Rugby", "Cricket", "Baseball"]
]

politicsq = [
    ["Who is India's Prime Minister?", "Arvind Kejriwal", "Rahul Gandhi", "Ashwin", "Modi"],
    ["Who is Delhi's Chief Minister?", "Modi", "Ashwin", "Akhilesh Yadav", "Arvind Kejriwal"],
    ["Which is the biggest political party of India?", "AAP", "Congress", "BJD", "BJP"],
    ["Who is the leader of AAP?", "Rahul Gandhi", "Mahatma Gandhi", "Riti", "Arvind Kejriwal"],
    ["What is India?", "Patriarchy", "Dictatorship", "Republic", "Democracy"]
]
hollywoodq = [
    ["Which is the biggest movie of all time?", "Endgame", "Spider man", "Mission Impossible", "Avatar"],
    ["Who is the best director od all time?", "Joe Rusell", "Karan Johar", "Riti", "Christopher Nolan"],
    ["Who is the Richest Actor in the world?", "Shah Rukh khan", "Salman Khan", "Tom Holland", "RJD"],
    ["Which of the following movie is the oldest?", "Maze Runner", "King Kong", "Avengers", "Mr.Bean"],
    ["What movie broke the box office on the first day?", "Avatar", "Terminator", "Iron Man", "Endgame"]
]
musicq = [
    ["Who is the best singer of all time ?", "KSI", "Arman Malik", "Dj Snake", "Eminem"],
    ["Who is the biggest band of all time?", "Beattles", "Falling in Reverse", "The Queen", "Team Evergreen"],
    ["What is the hit song of 2020?", "Levels", "Summer is Over ", "Jalebi Baby", "On my Way"],
    ["Who is known as the god father of music?", "Pritam", "Freddy Mercury", "Riti", "Mozzart"],
    ["What is the highest streams a song has gotten?", "Imagine", "One", "Young", "Stay"]
]
generalq = [
    ["What colour is the sun?", "red", "blue", "black", "yellow"],
    ["What colour is the rose?", "black", "blue", "yellow", "red"],
    ["What colour is the sea?", "red", "black", "yellow", "blue"],
    ["What colour is hair?", "red", "blue", "yellow", "black"],
    ["What colour is the Moon?", "red", "blue", "yellow", "white"],

]
levels = [1000, 3000, 5000, 10000, 20000]
money = 0

def kbc2(p):
    if t.upper() == topics[0]:
        for i in range(len(p)):
            qs = p[i]
            print(f"Question for rs {levels[i]}")
            print(f"{qs[0]}")
            print(f"a.{qs[1]}   b.{qs[2]}")
            print(f"c.{qs[3]}   d.{qs[4]}")
            rep = input("Enter your answer or 0 to quit:")

            if rep == 0:
                money = levels[i - 1]
                break
            if rep == qs[-1]:
                print(f"correct answer you've won {levels[i]}")
                if i == 0:
                    money = 1000
                elif i == 1:
                    money = 4000
                elif i == 2:
                    money = 9000
                elif i == 3:
                    money = 19000
                elif i == 4:
                    money = 39000
            else:
                print("wrong answer")
                break

        print(f"the total money ypu take home {money}")
for i in rules:
    print(i)
name = str(input("Enter your name:"))
x = str(input(f"Are you ready to start the gam {name}(type Yes or No):"))
topics = ["SPORTS", ",", "POLITICS", ",", "HOLLYWOOD", ",", "MUSIC", ",", "GENERAL"]
if len(x) >= 3:
    for i in topics:
        print(i, end="")
    t = str(input("\nChoose a Topic:"))
    if t.upper() == topics[0]:
        kbc2(sportsq)
    elif t.upper() == topics[2]:
        kbc2(ploticsq)
    elif t.upper() == topics[4]:
        kbc2(hollywoodq)
    elif t.upper() == topics[6]:
        kbc2(musicq)
    elif t.upper() == topics[0]:
        kbc2(generalq)
    else:
        print("done")























