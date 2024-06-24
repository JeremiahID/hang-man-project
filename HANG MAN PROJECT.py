from random import choice

#W_L means word list

W_L=["divine","jeremiah","vanessa","esther","God","samuel","crystal","solution",]

#W means word
W=choice([W_L])

# L means life
L=10

#L_E means letter entered

L_E=input("ENTER A LETTER: ")
if L_E in W:
    print("corect letter")
elif L_E not in W:
    print("Letter not found in word ")
else:
    print("")
for L_E in W:
    while L>0:
        print("YOU HAVE",L,"TRIALS REMANINIG")
        L-=1
        L_E=""
              
            

