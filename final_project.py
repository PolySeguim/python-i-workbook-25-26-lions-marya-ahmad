# CYOA: Zombie Apocalypse

#game intro
print("WELCOME TO Z-DAY: SURVIVE OR FALL")
player_name = input("What is your name, survivor: ")
print("\nGood luck,", player_name, "(you will need it). Your journey starts now...\n")


def start():
    print(player_name, ", you wake up in an abandoned house during a zombie apocalypse.")
    print("Your head hurts really bad and you barely remember how you got here.")
    print("Do you:")
    print("1) Look outside the window")
    print("2) Search the house")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        outside()
    elif choice == "2":
        house()
    else:
        print("\nInvalid choice. Game over.")
        quit()


def outside():
    print("\nWatch out! There are zombies in the street,", player_name, "!")
    print("You see a car with keys inside in the distance, but it will make too much noise.")
    print("You also see a sewer cover nearby.")
    print("Do you:")
    print("1) Take the car and drive")
    print("2) Go down into the sewer")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        car_run()
    elif choice == "2":
        sewer()
    else:
        print("\nInvalid choice. Game over.")
        quit()


def house():
    print("\nYou search the house and find food and a pocket knife.")
    print("Suddenly, another survivor appears, she says her name is Lucy.")
    print("Do you:")
    print("1) Trust Lucy")
    print("2) Leave her alone")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        team_with_lucy()
    elif choice == "2":
        alone_path()
    else:
        print("\nInvalid choice. Game over.")
        quit()


#car
def car_run():
    print("\nYou start the car,", player_name, ", zombies are chasing you but they're slow.")
    print("Up ahead you see:")
    print("1) A survivor camp")
    print("2) A mysterious lab with guards and 'POLYLAB' written on the side")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        camp()
    elif choice == "2":
        lab_entrance()
    else:
        print("\nInvalid choice. Game over.")
        quit()


#sewer
def sewer():
    print("\nYou crawl into the sewer,", player_name, ". It's dark and smells terrible.")
    print("You notice lights and machinery deeper in the tunnel.")
    print("Do you:")
    print("1) Explore further into the tunnel")
    print("2) Climb out through a hatch to the surface")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        lab_core()
    elif choice == "2":
        rooftop_escape()
    else:
        print("\nInvalid choice. Game over.")
        quit()


#house
def team_with_lucy():
    print("\nLucy is happy you trusted her she decides to trust you too.")
    print("She tells you that there is a rumor about a cure in a lab nearby.")
    print("Do you:")
    print("1) Go searching for the lab")
    print("2) Go to a survivor camp")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        lab_entrance()
    elif choice == "2":
        camp()
    else:
        print("\nInvalid choice. Game over.")
        quit()


def alone_path():
    print("\nYou leave by yourself,", player_name, ".")
    print("A zombie grabs you from behind — you didn't stand a chance.")
    print("ENDING: You die and become a zombie!")
    quit()


#camp
def camp():
    print("\nYou arrive at a camp full of survivors,", player_name, ".")
    print("People whisper about a scientist named Dr. Poly controlling the infection; you remember seeing that name on the lab.")
    print("Do you:")
    print("1) Stay safe at the camp")
    print("2) Sneak out at night to find the lab")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        print("\nYou live safely,", player_name, ", but never know what really happened.")
        print("ENDING: Peaceful Survival")
    elif choice == "2":
        lab_entrance()
    else:
        print("\nInvalid choice. Game over.")
        quit()


#lab
def lab_entrance():
    print("\nYou reach the lab with guards and high fences and see the name 'POLYLAB' on the side.")
    print("Do you:")
    print("1) Sneak in through a vent")
    print("2) Attack the guards directly")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        lab_core()
    elif choice == "2":
        fight_guards()
    else:
        print("\nInvalid choice. Game over.")
        quit()


def fight_guards():
    print("\nYou charge at the guards... risky decision,", player_name, ".")
    print("You are shot before you get through the gate.")
    print("ENDING: Your attack fails and you die.")
    quit()


def lab_core():
    print("\nInside the lab,", player_name, ", you discover the truth. scientists CREATED the zombies!!!!")
    print("The scientist behind it all is Dr. Poly. She planned to control the world using the virus.")
    print("Do you:")
    print("1) Destroy the lab and end the infection")
    print("2) Join Dr. Poly's evil mission to rule what's left of the world")

    choice = input("Pick 1 or 2: ")
    if choice == "1":
        print("\nYou blow up the generators and the cure is released to the world,", player_name, "!")
        print("All of the zombies start to die and the world is saved! YOU BEAT THE ZOMBIES!")
    elif choice == "2":
        print("\nYou join Dr. Poly,", player_name, ", and rule the world!")
        print("ENDING: You join the dark side!")
    else:
        print("\nInvalid choice. Game over.")
        quit()


def rooftop_escape():
    print("\nYou climb through the hatch and escape back into daylight,", player_name, ".")
    print("You're alive, but never uncover the truth behind the virus.")
    print("ENDING: You survive, but with no answers.")
    quit()


# Start the game
start()
