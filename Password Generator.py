exec(open('etc/clear.py').read())#clear

print("Welcome to password generator!")
print("What you will do?\n")
print(" {} {} {} {} {} {} {} {}".format("(1)Numeric Password\n", "(2)Number+word mixed Password\n","(3)Number+word+symbol mixed Password\n","(4)Number+symbol mixed Password\n", "(5)Word Password\n", "(6)Symbol Password\n", "(7)Word+symbol mixed Password\n", "(8)Exit\n"))
Selector=int(input("Please select a number for operation:\nUSER>>"))
if(Selector==1):
    exec(open('etc/N.py').read())
else:
    if(Selector==2):
        exec(open('etc/NW.py').read())
    else:
        if(Selector==3):
            exec(open('etc/NWS.py').read())
        else:
            if(Selector==4):
                exec(open('etc/NS.py').read())
            else:
                if(Selector==5):
                    exec(open('etc/W.py').read())
                else:
                    if(Selector==6):
                        exec(open('etc/S.py').read())
                    else:
                        if(Selector==7):
                            exec(open('etc/WS.py').read())
                        else:
                            if(Selector==8):
                                exit()
                            else:
                                ##Error handler
                                if(Selector>8):
                                    print("Number not found. Please select a number from table.")
                                    exec(open('Password Generator.py').read())#Restart
                                else:
                                    if(Selector<1):
                                        print("Number not found. Please select a number from table.")
                                        exec(open('Password Generator.py').read())#Restart
            