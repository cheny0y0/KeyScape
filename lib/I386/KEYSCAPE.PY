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
        if os.name == "nt" :
            os.system("cls")
        else :
            os.system("clear")
        key = random.randint(0,9)
        if key == 0 :
            print("---------------------\n|1|2|3|4|5|6|7|8|9|0|\n--------------\
-------\n| | | | | | | | | |X|\n---------------------\nRemaining Time: "+str(
    round(destTime-time.time(),1))+" Score: "+str(score))
        else :
            print("---------------------\n|1|2|3|4|5|6|7|8|9|0|\n--------------\
-------\n|"+" |"*(key-1)+"X"+"| "*(10-key)+"|\n---------------------\nRemaining\
 Time: "+str(round(destTime-time.time(),1))+" Score: "+str(score))
        if os.name == "nt" :
            os.system("choice /c:"+str(key)+" /n")
        else :
            os.system("mkdir /tmp/pyscript")
            tty = open("/tmp/pyscript/presskey.sh","w")
            tty.write('tempans=tty\nwhile [ "$tempans" != "'+str(key)+'" ]; do \
read -n 1 tempans; done')
            tty.close()
            if os.system("bash /tmp/pyscript/presskey.sh") == 2 :
                raise KeyboardInterrupt
        score += 1
        if destTime - time.time() < 0.0 :
            print("\nTime is up! Your score is: "+str(score))
            try :
                raw_input
            except NameError :
                historyFile = input("Would you like to append your history scor\
e?(Input file location to append, or enter for none)")
            else :
                historyFile = raw_input("Would you like to append your history \
score?(Input file location to append, or enter for none)")
            if historyFile.strip() != "" :
                if os.name == "nt" :
                    tty = "\\".join(historyFile.split("\\")[:-1])
                else :
                    tty = "/".join(historyFile.split("/")[:-1])
                os.system('mkdir "'+tty+'"')
                try :
                    open(historyFile,"r").close()
                except :
                    try :
                        open(historyFile,"x").close()
                    except :
                        print("An error occured!")
                    else :
                        tty = open(historyFile,"r")
                        history = tty.read()
                        tty.close()
                        tty = open(historyFile,"w")
                        tty.write(history)
                        try :
                            raw_input
                        except NameError :
                            tty.write(time.strftime("%Y-%m-%d-%H:%M:%S")+" Seco\
nd:"+str(userTime)+" Score:"+str(score)+" "+input("More comments for the histor\
y?")+"\n")
                        else :
                            tty.write(time.strftime("%Y-%m-%d-%H:%M:%S")+" Seco\
nd:"+str(userTime)+" Score:"+str(score)+" "+raw_input("More comments for the hi\
story?")+"\n")
                        tty.close()
                else :
                    tty = open(historyFile,"r")
                    history = tty.read()
                    tty.close()
                    tty = open(historyFile,"w")
                    tty.write(history)
                    try :
                        raw_input
                    except NameError :
                        tty.write(time.strftime("%Y-%m-%d-%H:%M:%S")+" Second:\
"+str(userTime)+" Score:"+str(score)+" "+input("More comments for the history?\
")+"\n")
                    else :
                        tty.write(time.strftime("%Y-%m-%d-%H:%M:%S")+" Second:\
"+str(userTime)+" Score:"+str(score)+" "+raw_input("More comments for the histo\
ry?")+"\n")
                    tty.close()
            break
except KeyboardInterrupt :
    print("USER EXITED FORCIBLY.")
    exit(7)
