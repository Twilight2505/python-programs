from random import randint
print("Welcome to snake water gun ")
try:
        user =int (input("Enter 0 for snake, 1 for water or 2 for gun: "))
        
        if user > 2 or user < 0:
            raise ValueError("Number must be 0, 1, or 2 only.")
        
except ValueError as e:
        print("Invalid input!", e)

lt= [0,1,2]

idx = randint (0,len(lt)-1)

comp= lt.pop(idx)
print(comp)

if comp==0 and user==0:
        print(" Its Draw")
elif     comp==0 and user==1:
        print("You Win")
elif     comp==0 and user==2:
        print("You Lose")
elif     comp==1 and user==0:
        print("You Lose")
elif     comp==1 and user==1:
        print("Its Draw")
elif     comp==1 and user==2:
        print("You Win")
elif     comp==2 and user==0:
        print("You Win")
elif     comp==2 and user==1:
        print("You Lose")
elif     comp==2 and user==2:
            print("Its Draw")
