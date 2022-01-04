import random

computer = 0
player = 0

attempt = 10
print("You can Play 10 times")

for i in range(1, attempt+1) :
    list1 = [1, 2, 3]
    game = random.choice(list1)

    try :
        user = int(input("Select 1 for \"Snake\" 2 for \"Water\" 3 for \"Gun\" : "))

        if game == user :
            print("Tie")

        elif game == 1 and user == 2 :
            print("Computer Win, \"Snake drinks Water\"")
            computer += 1
        elif game == 2 and user == 3 :
            print("Computer Win, \"Gun dip in Water\"")
            computer += 1
        elif game == 3 and user == 1 :
            print("Computer Win, \"Gun kill Snake\"")
            computer += 1

        elif game == 1 and user == 3 :
            print("You Win, \"Gun kill Snake\"")
            player += 1
        elif game == 2 and user == 1 :
            print("You Win, \"Snake drinks Water\"")
            player += 1
        elif game == 3 and user == 2 :
            print("You Win, \"Gun dip in Water\"")

        else :
            print("Wrong Number")

        print(f"{attempt-1} life left")
        attempt -= 1

    except Exception as e :
        print("Invalid Input!")

if computer > player :
    print("Overall Computer Won")
elif computer < player :
    print("Overall Player Won")
else :
    print("Draw")