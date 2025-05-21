ques=["What is the capital of India?","Which planet is known as the Red Planet?","How many sides does a triangle have?","Which of the following is a programming language?","Which number is even?","What color do you get when you mix red and white?","What is 5 x 6?","Which is the largest animal on land?","How many days are there in a leap year?","Which fruit is known for keeping doctors away if eaten daily?"]
opt=[["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
    ["A. 2", "B. 3", "C. 4", "D. 5"],
    ["A. Python", "B. Snake", "C. Lizard", "D. Cobra"],
    ["A. 3", "B. 7", "C. 9", "D. 8"],
    ["A. Orange", "B. Pink", "C. Purple", "D. Brown"],
    ["A. 11", "B. 30", "C. 35", "D. 56"],
    ["A. Elephant", "B. Lion", "C. Giraffe", "D. Rhino"],
    ["A. 364", "B. 365", "C. 366", "D. 367"],
    ["A. Banana", "B. Apple", "C. Mango", "D. Grapes"]]
ans=["B","C","B","A","D","B","B","A","C","B"]
amt=[500,1000,2000,4000,3200,6400,12500,25000,50000,100000]

def KBC():
    print("Welcome to KBC")
    
    for i in range(0,10):
        print(ques[i])
        for option in opt[i]:
            print(option)

        answer=input("enter your answer as A,B,C or D: ").upper()
        if (answer==ans[i]):
            amt[i]
            print("Good Job you win!",amt[i])
        else:
            print("Game Over!!!")
            break
    else:    
        print("Congrats! Your total winnings: ₹100000")    

KBC()
