import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
def getArt(option):
    if option==0:
        return rock
    elif option==1:
        return paper
    elif option==2:
        return scissors
    else:
        return 'Invalid Input'
    
def whoWins(a,b):
    return (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0)

person=int(input("What do you chose, 0 for rock, 1 for Paper and 2 for scissors."))
computer=random.randint(0,2)      
personArt = getArt(person)
computerArt = getArt(computer)

print("\nyou chose")
print(personArt)
print("Computer chose")
print(computerArt)

if person==computer:
    print("It's a draw")
elif whoWins(computer,person):
    print("Yayyy!! You won")
elif whoWins(computer,person):
    print("Oops!! You lose")
else:
    print("Something went wrong")


    
