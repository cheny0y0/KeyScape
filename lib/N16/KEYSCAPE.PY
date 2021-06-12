import os
import random
import sys
import time

try :
    while True :
        try :
            raw_input
        except NameError :
            userTime = input("Input the time(seconds) limit of the game(at leas\
t 0.5):")
        else :
            userTime = raw_input("Input the time(seconds) limit of the game(at \
least 0.5):")
        try :
            float(userTime)
        except :
            print("Invalid argument. Please input another.")
        else :
            if float(userTime) < 0.5 :
                print("Invalid argument. Please input another.")
            else :
                userTime = float(userTime)
                break
except KeyboardInterrupt :
    print("User exited.")
    exit(7)
try :
    score = 0
    destTime = time.time() + userTime
    while True :
        os.system("cls")
        key = random.randint(0,9)
        if key == 0 :
            print("---------------------\n|1|2|3|4|5|6|7|8|9|0|\n--------------\
-------\n| | | | | | | | | |X|\n---------------------\nRemaining Time: "+str(
    round(destTime-time.time(),1))+" Score: "+str(score))
        else :
            print("---------------------\n|1|2|3|4|5|6|7|8|9|0|\n--------------\
-------\n|"+" |"*(key-1)+"X"+"| "*(10-key)+"|\n---------------------\nRemaining\
 Time: "+str(round(destTime-time.time(),1))+" Score: "+str(score))
        os.system("choice /c:"+str(key)+" /n")
        score += 1
        if destTime - time.time() < 0.0 :
            print("Time is up! Your score is: "+str(score))
            try :
                raw_input
            except NameError :
                input("Press enter to exit...")
            else :
                raw_input("Press enter to exit...")
            break
except KeyboardInterrupt :
    print("USER EXITED FORCIBLY.")
    exit(7)
