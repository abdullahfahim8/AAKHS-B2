import random

lower = int(input("Enter Lower Bound : "))
upper = int(input("Enter Upper Bound : "))


x = random.randint(lower , upper)

chance = ((upper - lower)//2)-2
Try = 0

while chance!=0:
    print("You've ", chance , "More Chances!")
    chance-=1
    Try+=1

    
    guess = int(input("Enter Number: "))
    if guess>x:
        print("Your Guess Is Too High..!")
    elif guess<x:
        print("Your Guess is Too Low..!")
    elif guess == x:
        print("Congratulations, You Did it!You gussed at ",Try , "Try!")
        break

    else:
        print("You've Entered Wrong!")


if chance == 0:
    print("You Failed To Guess The Number!")
    print("The Number Was ", x)





##############Project Done By AAKHS Batch -2#################################
#jihad , azad , shanto , niloy , pranto , sojit , parves #