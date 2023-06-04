ts = 0
import time
import random
cong = ['you got it !!', 'congratulations', 'wow !! you won']
los = ['oops you lost ..', 'game over', 'Unluckly . try again later ']
win = random.choice(cong)
lose =  random.choice(los)
def main():
    print('while on a walk in the woods , at a dark night ...')
    time.sleep(2)
    print("a strange man with a tall magic wood is calling you.")
    time.sleep(2)
    print("you stumbled upon a secret pathway you had never seen before")
    time.sleep(2)
    print("Total score = " + str(ts) )
    print("Enter 1 to follow the pathway. ")
    print("Enter 2 to respond to the strange man.")
    ans = int(input("(please enter 1 or 2)"))
    while ans != 1 and ans != 2 :
        ans = int(input("(please enter 1 or 2)"))
    def pathway ():
        if ans == 1 :
            ts = 5
            time.sleep(2)
            print(" Curious, you followed the path and found yourself in front of an old, abandoned mansion.")
            time.sleep(2)
            print("you felt a strange pull towards the mansion and decided to investigate further.")
            time.sleep(1)
            print("Total score = " + str(ts) )
            print("Enter 1 to continue ")
            print("Enter 2 to run away ")
    def man ():
        if ans == 2 :
            ts =  5
            time.sleep(2)
            print("you followed the strange man")
            time.sleep(2)
            print("the man: Hi! I am Karl , let's play with me hahaha!!")
            time.sleep(1)
            print("Total score = " + str(ts) )
            print("Enter 1 to follow him ")
            print("Enter 2 to run away ")
    pathway()
    man()
    ans2 = int(input("(please enter 1 or 2)"))
    while ans2 != 1 and ans2 != 2 :
        ans2 = int(input("(please enter 1 or 2)"))
    def Continue ():
        if ans== 1 and ans2 == 1:
            ts =  10
            time.sleep(2)
            print("you slowly pushed open the creaky door and entered the dark and dusty house.")
            time.sleep(2)
            print("you noticed that every room was filled with books.")
            print("the mansion is a library that had been abandoned for years.")
            time.sleep(2)
            print("there are two books on the table . blue and red one")
            time.sleep(1)
            print("Total score = " + str(ts) )
            print("Enter 1 to open the blue book ")
            print("Enter 2 to open the red book ")
    def runaway ():
        if ans== 1 and ans2 == 2:
            ts = 0
            time.sleep(2)
            print("the strange man was following you !")
            time.sleep(2)
            print("You became a frog using his magic wood !!!!")
            print(lose)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    def follow ():
        if ans== 2 and ans2 == 1:
            ts = 0
            time.sleep(2)
            print("You became a frog using his magic wood !!!!")
            time.sleep(2)
            print(lose)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    def Runaway():
        if ans== 2 and ans2 == 2:
            ts =  10
            time.sleep(2)
            print("you passed the secret pathway and found yourself in front of a ...")
            time.sleep(2)
            print("dark and dusty house.")
            time.sleep(1)
            print("Total score = " + str(ts) )
            print("Enter 1 to Enter the house")
            print("Enter 2 to come back")
    Continue()
    runaway()
    follow()
    Runaway()
    ans3 = int(input("(please enter 1 or 2)"))
    while ans3 != 1 and ans3 != 2 :
        ans3 = int(input("(please enter 1 or 2)"))
    def blue ():
        if ans== 1 and ans2 == 1 and ans3 ==1 :
            ts = 5
            time.sleep(2)
            print("The blue book is fake , it was a box!!")
            time.sleep(2)
            print("Total score = " + str(ts) )
            time.sleep(1)
            print("Enter 1 to open the box")
            print("Enter 2 to open the red book ")
    def red ():
        if ans== 1 and ans2 == 1 and ans3 ==2 :
            ts = 15
            time.sleep(2)
            print("The red book is guiding you to the second room !! ")
            time.sleep(2)
            print("Total score = " + str(ts) )
            time.sleep(1)
            print("Enter 1 to go to the room")
            print("Enter 2 to run away ")
    def enter ():
        if ans== 2 and ans2 == 2 and ans3==1 :
            ts = 0
            time.sleep(2)
            print("the house is very dark !!")
            time.sleep(2)
            print("A ghost came out of one of the rooms and killed you!!!!")
            time.sleep(2)
            print(lose)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    def come():
        if ans== 2 and ans2 == 2 and ans3==2 :
            ts = 0
            time.sleep(2)
            print("You became a frog using his magic wood !!!!")
            time.sleep(2)
            print(lose)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    blue ()
    red()
    enter()
    come()
    ans4 = int(input('(Please enter 1 or 2)'))
    while ans4 != 1 and ans4 != 2 :
        ans4 = int(input("(please enter 1 or 2)"))
    def box() :
        if ans== 1 and ans2 == 1 and ans3 ==1 and ans4 ==1 :
            ts = 0
            time.sleep(2)
            print("A snake got out of the box and killed you !!")
            time.sleep(2)
            print(lose)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    def Red ():
        if ans== 1 and ans2 == 1 and ans3 ==1 and ans4 ==2 :
            ts = 10
            time.sleep(2)
            print("The red book is guiding you to the second room !! ")
            time.sleep(2)
            print("Total score = " + str(ts) )
            time.sleep(1)
            print("Enter 1 to go to the room")
            print("Enter 2 to run away ")
    def room () :
        if ans== 1 and ans2 == 1 and ans3 ==2 and ans4==1 :
            ts = 20
            time.sleep(2)
            print ("You got a treasure in the room !!")
            time.sleep(1)
            print(win)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    def RUN() :
        if ans== 1 and ans2 == 1 and ans3 ==2 and ans4==2 :
            ts = 0
            time.sleep(2)
            print("the strange man was following you !")
            time.sleep(2)
            print("You became a frog using his magic wood !!!!")
            print(lose)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    RUN()
    room()
    box()
    Red()
    ans5 = int(input('(Please enter 1 or 2)'))
    while ans5 != 1 and ans5 != 2 :
        ans5 = int(input("(please enter 1 or 2)"))
    def GR ():
        if ans== 1 and ans2 == 1 and ans3 ==1 and ans4 ==2 and ans5 ==1:
            ts=15
            time.sleep(2)
            print ("You got a treasure in the room !!")
            time.sleep(1)
            print(win)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    def RA():
        if ans== 1 and ans2 == 1 and ans3 ==1 and ans4 ==2 and ans5 ==2:
            ts=0
            time.sleep(2)
            print("the strange man was following you !")
            time.sleep(2)
            print("You became a frog using his magic wood !!!!")
            print(lose)
            print("Total score = " + str(ts) )
            replay = input("Play again ?  y/n ")
            while str(replay)!="y" and str(replay)!="n":
                replay = input("Play again ?  y/n ")
            if str(replay)== "y" :
                main()
            elif str(replay)== "n" :
                print("see you later .")
                time.sleep(2)
                exit()
    GR()
    RA()
main()