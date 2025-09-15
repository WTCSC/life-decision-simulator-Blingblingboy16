import time

def start_game(first_time=False):
    if first_time:
        print("You're on a very average path on a very average and usual every day kind of day.")
        print("There's a turn in the road and you must decide if you want to go left or right.")
    else:
        print("\nYou find yourself back at the fork in the road...")

    choice = input("Choose road to the right or to the left? (r/l) ").lower()

    # mean monkey
    if choice == 'r':
        print("You meet a monkey, a rather unkind looking one.")
        choice = input("Try to pick up the monkey or feed it a banana? (pick/feed) ").lower()
        if choice == 'pick':
            print("The monkey attacks, you die instantly. Game over. ") 
        elif choice == 'feed':
            print("The monkey attacks, you die instantly. Game over.")

    # nice monkey
    elif choice == 'l':
        print("You meet a very nice looking monkey.")
        choice = input("Try to pick up the monkey or feed it a banana? (pick/feed) ").lower()
        if choice == 'pick':
            print("The monkey attacks, you die instantly. Game over.")
        elif choice == 'feed':
            print("The monkey attacks you and you die instantly. Game over.")

    else:
        print("Just choose from the only options I gave you, dummy. Game over.")

    time.sleep(2)

def play_again_loop():
    start_game(first_time=True)  # show intro the first time

    while True:
        play_again = input("Wanna try again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Thanks for playing twin, this is your reminder to not feet or pick up monkeys, wether they look nice or mean")
            break
        start_game(first_time=False)  # show shorter reset intro

play_again_loop()
