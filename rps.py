# ROCK PAPER SCISSORS (RPS) VERSION 0.3 ALPHA (27/11/2024) - CREATED: 26/09/2024 BY: desyntax

# imports
import random as rng
import array as ar

# variables and tables
cpu = "" # cpu's rps choice
fullopt = ["rock", "paper", "scissors"] # list of all choices in FULL form
opt = ["r", "p", "s"] # list of all choices in ABBREVIATED form
usr = "" # user's rps choice
userscore = 0
cpuscore = 0
ans = "" # game end input response from user
streakHolder = None # who holds the streak
streak = 0
draw = False # boolean for tied result
win = "" # string value for printing who won
error = False # determines whether user inputted incorrect rps choice
update = "[UPDATE 0.3.1 ALPHA | 27/11/2024]: removed redundancies and added more comments in code"

# definitions
def game_end(winner):
    global streak, streakHolder, win
    print(win, " wins", sep="")
    print()
    if(streakHolder != win):
        if(streakHolder is None):
            print("the first winner is ", win, sep="")
        if(streakHolder is not None):
            print(streakHolder, "'s streak of ", streak, " has been beaten!", sep="")
            streak = 0
    streak += 1
    streakHolder = win
    if(streak >= 5):
        if(streak >= 10):
            print(streakHolder, " is on an unbeatable streak of ", streak, sep="")
        else:
            print(streakHolder, " is on an amazing streak of ", streak, sep="")
    if(streakHolder is not None):
        print(streakHolder, " is on a ", streak, " streak", sep="")
    elif(streakHolder is None):
        print("no one has a streak yet")

def record():
    global usr, cpu, userscore, cpuscore, draw, win
    try:
        with open("rpsRecords.txt", "a") as file:
            file.write(f"{usr} vs {cpu}\n")
            if(draw == False):
                file.write(f"OUTCOME: {win}\n")
                file.write(f"SCORE: USER: {userscore}, CPU: {cpuscore}\n")
                file.write("\n")
            if(draw == True):
                file.write("OUTCOME: DRAW\n")
                file.write(f"SCORE: USER: {userscore}, CPU: {cpuscore}\n")
                file.write("\n")
    except FileNotFoundError:
        input("CRITICAL ERROR: 'rpsRecords.txt' not found. shutting down... ")
        exit()

def init_record():
    try:
        with open("rpsRecords.txt", "a") as file:
            file.write("--- NEW GAME ---\n")
    except FileNotFoundError:
        input("CRITICAL ERROR: 'rpsRecords.txt' not found. shutting down... ")
        exit()

# main code

# initialise
print("welcome to rock paper scissors! see how you can stack up against a computer that plays completely randomly :)")
print("you may use full form (rock, paper, scissors) or abbreviated form (r, p, s)! type 'update' in the game end")
print("prompt to view the most recent update")
init_record()

# start permanent loop
while True:
    
# user makes choice
    print("rock paper scissors shoot!")
    usr = input()
    if(usr in opt):
        if(usr == "r"):
            usr = "rock"
        if(usr == "p"):
            usr = "paper"
        if(usr == "s"):
            usr = "scissors"
    if(usr not in fullopt):
        error = True
        print("error: user listed invalid choice")
        print("skipping round...")

# cpu makes random choice
    if(error = False):
        cpu = rng.choice(fullopt)
        print(cpu)

# determine who wins
    if(error = False):
        if(usr == "rock" and cpu == "scissors"):
            win = "user"
            game_end(usr)
            userscore += 1
            draw = False
        if(usr == "rock" and cpu == "paper"):
            win = "cpu"
            game_end(cpu)
            cpuscore += 1
            draw = False
        if(usr == "rock" and cpu == "rock"):
            print("draw!")
            draw = True
            print(streakHolder, " is on a ", streak, " streak", sep="")

        if(usr == "paper" and cpu == "rock"):
            win = "user"
            game_end(usr)
            userscore += 1
            draw = False
        if(usr == "paper" and cpu == "scissors"):
            win = "cpu"
            game_end(cpu)
            cpuscore += 1
            draw = False
        if(usr == "paper" and cpu == "paper"):
            print("draw!")
            draw = True
            print(streakHolder, " is on a ", streak, " streak", sep="")

        if(usr == "scissors" and cpu == "paper"):
            win = "user"
            game_end(usr)
            userscore += 1
            draw = False
        if(usr == "scissors" and cpu == "rock"):
            win = "cpu"
            game_end(cpu)
            cpuscore += 1
            draw = False
        if(usr == "scissors" and cpu == "scissors"):
            print("draw!")
            draw = True
            print(streakHolder, " is on a ", streak, " streak", sep="")

# print results
    if(error = False):
        record()
        print()
        print("user score: ", userscore, ", cpu score: ", cpuscore, sep="")
        print("play again? (type quit to stop; update to view most recent update; clear to clear rpsRecords.txt)")
        ans = input()
        if(ans == "quit"):
            quit()
        if(ans == "update"):
            print(update)
        if(ans == "clear"):
            with open("rpsRecords.txt", "w") as file:
                file.write("--- CLEARED ---\n")
        if(ans == "mario"):
            print("we love mario :D")
            userscore += 1
            try:
                with open("rpsRecords.txt", "a") as file:
                    file.write("mario :D\n")
                    file.write("+1 user score\n")
                    file.write("\n")
            except FileNotFoundError:
                input("CRITICAL ERROR: 'rpsRecords.txt' not found. shutting down... ")
                exit()

