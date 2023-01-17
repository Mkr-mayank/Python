import random
print("STONE PAPER SCISSOR")
print("Let's Begin!")
n=1
ch=""
hscore=0
pcscore=0
while(n!=0 and (hscore!=10 and pcscore!=10)):
    pc=random.randrange(1,4)
    if(pc==1):
        ch="stone"
    elif(pc==2):
        ch="paper"

        
    elif(pc==3):
        ch="scissor"
    else:
        n=0
    human=input("Stone/Paper/Scissor: ")
    print(human,ch)
    if(human.casefold()==ch):
        print("Tie")
    elif((human.lower()=="stone" and ch=="paper")or(human.casefold()=="paper" and ch=="scissor")or(human.casefold()=="scissor" and ch=="stone")):
        pcscore=pcscore+1
        print("Computer defeats Human\n")
    elif((human.casefold()=="stone" and ch=="scissor")or(human.casefold()=="paper" and ch=="stone")or(human.casefold()=="scissor" and ch=="paper")):
        hscore=hscore+1
        print("Human defeats Computer\n")
    else:
        print("It's a Cheat or Wrong Symbol")
        n=0
print("Game Over")
print("Total Score - Human:Computer %d:%d"%(hscore,pcscore))
if(hscore>pcscore):
    print("Human won the game and defeated Computer by %d points"%(hscore-pcscore))
elif(hscore<pcscore):
    print("Computer won the game and defeated Human by %d points"%(pcscore-hscore))
elif(hscore==pcscore):
    print("Incredible! It's a Tie")
else:
    print("Error 404") 