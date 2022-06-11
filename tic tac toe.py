import sys
# q w e
# r t z 
# u i o 
q="q"
w="w"
e="e"
r="r"
t="t"
z="z"
u="u"
i="i"
o="o"
rc1=1
rc2=2
def wincheck():
    if q == "X":
        if w == "X":
            if e == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    if r == "X":
        if t == "X":
            if z == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    if u == "X":
        if i == "X":
            if o == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    if q == "X":
        if r == "X":
            if u == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    if w == "X":
        if t == "X":
            if i == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    if e == "X":
        if z == "X":
            if o == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    if e == "X":
        if t == "X":
            if o == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    if e == "X":
        if t == "X":
            if u == "X":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! X wins")
                sys.exit()
                exit()
    #OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#
    if q == "O":
        if w == "O":
            if e == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    if u == "O":
        if i == "O":
            if o == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    if q == "O":
        if r == "O":
            if u == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    if w == "O":
        if t == "O":
            if i == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    if e == "O":
        if z == "O":
            if o == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    if e == "O":
        if t == "O":
            if o == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    if e == "O":
        if t == "O":
            if u == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    if q == "O":
        if w == "O":
            if e == "O":
                print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o)
                print("game over! O wins")
                sys.exit()
                exit()
    
while rc1<rc2:
    print("q w e")
    print("r t z")
    print("u i o")
    print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o )
    x=str(input("x: "))
    if x=="q":
        q="X"
    if x=="w":
        w="X"
    if x=="e":
        e="X"
    if x=="r":
        r="X"
    if x=="t":
        t="X"
    if x=="z":
        z="X"
    if x=="u":
        u="X"
    if x=="u":
        u="X"
    if x=="i":
        i="X"
    if x=="o":
        o="X"
    wincheck()
    rc1=rc1+1
    while rc1==rc2:
        print("\n",q," ",w," ",e,"\n",r," ",t," ",z,"\n",u," ",i," ",o )
        o=str(input("o: "))
        if o=="q":
            q="O"
        if o=="w":
            w="O"
        if o=="e":
            e="O"
        if o=="r":
            r="O"
        if o=="t":
            t="O"
        if o=="z":
            z="O"
        if o=="u":
            u="O"
        if o=="u":
            u="O"
        if o=="i":
            i="O"
        if o=="o":
            o="O"
        wincheck()
        rc2=rc2+1

       
