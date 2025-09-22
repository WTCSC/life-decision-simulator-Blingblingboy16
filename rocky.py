pet_name = input("whats your rock guy called?")
hunger = 5
boredom = 5
happiness = 5

while hunger > 0 and boredom > 0 and happiness > 0:
    print(f"{pet_name}'s hunger is at {hunger}")
    print(f"{pet_name}'s boredom is at {boredom}")
    print(f"{pet_name}'s happiness is at {happiness}")

    action = input("do you wanna feed (f), play (p) or pet (pe) your rock guy?").lower()

    if action == "f":
        hunger = hunger - 1
        boredom = boredom + 1
        happiness = happiness + 1
    elif action == "p":
        hunger = hunger + 1
        boredom = boredom - 1
        happiness = happiness + 1
    elif action == "pe":
        hunger = hunger + 1
        boredom = boredom + 1
        happiness = happiness - 1
    else:
        print("literally thats not even an option twin")
    
    if hunger >= 10:
        print(f"{pet_name} just starved, game over :(")
        break
    if boredom >= 10:
        print(f"{pet_name} just died of boredom, game over :(")
        break
    if happiness >= 10:
        print(f"{pet_name} just died of sadness, game over :(")
        break

