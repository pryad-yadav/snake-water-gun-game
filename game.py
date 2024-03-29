import random, playsound

def winning_music():
    """
    Plays the winning music.
    """
    win_music  = ["anime wow.mp3", "bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print(e)

def losing_music():
    """
    Plays the losing music.
    """
    lose_music  = ["Nope.mp3", "Fart.mp3"]
    try:
        playsound.playsound(random.choice(lose_music))
    except Exception as e:
        print(e)

def tie_music():
    """
    Plays the tie music.
    """
    try:
        playsound.playsound("Awkward Cricket.mp3")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\nWelcome to the Snake Water Gun game!\n\n")

    attempts = 1
    your_point = 0
    computer_point = 0


    while (attempts<=10):

        lst=["s","w","g"]
        ran=random.choice(lst)
        
        inp = input("Enter your choice (Snake(s), Water(w), Gun(g)): ")
        inp = inp.lower()

        if inp == ran:
            print("Tie")
            print(f"\nYou chose snake and Computer also chose snake! ")
            print("No body gets point\n")
            tie_music()


        elif inp=="s" and ran=="w":
            your_point=your_point+1
            print(f"\nYou choosed snake and Computer chose water! ")
            print("The snake drank water\n")
            print("You won this round")
            print("You got 1 point\n")            
            winning_music()


        elif inp=="w" and ran=="s":
            computer_point = computer_point + 1
            print(f"\nYou choosed water and Computer chose snake! ")
            print("The snake drank water\n")
            print("You lost this round")
            print("Computer gets 1 point\n")
            losing_music()


        elif inp=="w" and ran=="g":
            print(f"\nYou chose water and Computer chose gun! ")
            your_point = your_point + 1
            print("The gun sank in water\n")
            print("You won this round")
            print("You got 1 point\n")
            winning_music()


        elif inp == "g" and ran == "w":
            print(f"\nYou choosed gun and Computer chose water! ")
            computer_point = computer_point + 1
            print("The gun sank in water\n")
            print("You Lost this round")
            print("computer gets 1 point\n")
            losing_music()


        elif inp == "g" and ran == "s":
            print(f"\nYou choosed gun and Computer chose snake! ")
            your_point = your_point + 1
            print("The snake was shot and it died\n")
            print("You won this round")
            print("You get 1 point\n")
            winning_music()

        elif inp == "s" and ran == "g":
            print(f"\nYou choosed snake and Computer chose gun! ")
            computer_point=computer_point+1
            print("The snake was shot and he died\n")
            print("You lost this round!")
            print("Computer gets 1 point\n")

        else:
            print("Invalid input!\n")
            continue


        print("\nNo. of guesses left: {}".format(10 - attempts))
        attempts = attempts + 1

      


    print(f"Your score: {your_point} \nComputer's score: {computer_point}")

    if computer_point > your_point:
        print("\nComputer won and you lost!\n")

    elif computer_point < your_point:
        print("\nYou won and computer lost!\n")

    else:

        print("It was a tie!")
        print("Invalid")

   
    if attempts>10:
        print("\nGame over! ")


print(f"\nYour points are {your_point} and Computer's points are {computer_point}!\n")