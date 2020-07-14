secret = 55
guess = int(input("Enter a number from 5 to 50 "))
while guess != secret:

    if guess < secret:
        print("guessed number is low")
        guess = int(input("Enter an integer from 5 to 50 "))
    elif guess > secret:
        print("guessed number is high")
        guess = int(input("Enter an integer from 5 to 50 "))
    else:
        print("invalid")
print("you win!")
