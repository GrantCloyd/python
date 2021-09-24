import random 


def main():
    random_int  = random.randint(1,10)
    answer = input("Guess a number from 1 to 10\n")
    answer = int(answer)

    while random_int != answer:
        if answer < random_int:
            answer = int(input("That's not quite right, try higher\n"))
        elif answer > random_int:    
            answer = int(input("That's not quite right, try lower\n"))
    
    print(f"That's right, the number was {random_int}!")     

main()           