from random import randint
n = randint(100,1000)

a= -1 
guesses = 0
while (a!=n):
    a= int(input("Enter the number: "))
    if(a>n):
        print("Lower")
        guesses += 1
    elif(a<n):
        print("Higher")
        guesses += 1
    
print(f"Your guess is right {n} in guesses {guesses}")

