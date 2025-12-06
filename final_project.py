#zombie apocalypse: survive or fall

#ask player for their name (global variable)
print("WELCOME TO Z-DAY: SURVIVE OR FALL")
player_name = input("What is your name, survivor: ")
print("\nGood luck,", player_name, "(you will need it). Your journey starts now...\n")

#game functions

def start():
    print(player_name, ", you wake up in a abandonded house during a zombie apocalypse.")
    print("Your head really hurts and you barely remember how you got here")
    print("Do you:")
    print("A. Look outside the window")
    print("B. Search the house")

    choice = input("Choose A or B: ")
    if choice == "A":
        outside()
    elif choice == "B":
        house()
    else:
        start()


def outside():
    print("\nWatch out! There are zombies in the street,", player_name, "!")
    print("You see a car with keys inside in the distance, but it will make too much noise")
    print("You also see a sewer cover nearby")
    print("Do you:")
    print("A) Take the car and drive")
    print("B) Go down into the sewer")

    choice = input("A or B: ")
    if choice == "A":
        car_run()
    elif choice == "B":
        sewer()
    else:
        outside()


def house():
    print("\nYou search the house and find food and a pocket knife")
    print("Suddenly, another survivor appears, she says her name is Lucy")
    print("Do you:")
    print("A) Trust Lucy")
    print("B) Leave her alone")

    choice = input("A or B: ")
    if choice == "A":
        team_with_lucy()
    elif choice == "B":
        alone_path()
    else:
        house()


#car path
def car_run():
    print("\nYou start the car but look behind you", player_name, "zombies are chasing you but they're slow")
    print("Up ahead you see:")
    print("A) A survivor camp")
    print("B) A mysterious lab with guards and 'POLYLAB' written on the side")

    choice = input("A or B: ")
    if choice == "A":
        camp()
    elif choice == "B":
        lab_entrance()
    else:
        car_run()


#sewer path
def sewer():
    print("\nYou crawl into the sewer, it's dark and smells terrible")
    print("You notice lights and machinery deeper in the tunnel")
    print("Do you:")
    print("A) Explore further into the tunnel")
    print("B) Climb out through a hatch to the surface")

    choice = input("A or B: ")
    if choice == "A":
        lab_core()
    elif choice == "B":
        rooftop_escape()
    else:
        sewer()


#house options
def team_with_lucy():
    print("\nLucy cheers, she is happy you trusted her!")
    print("Lucy whispers to you: 'There's a rumor about a cure in a lab nearby'")
    print("Do you:")
    print("A) Go searching for the lab")
    print("B) Go to a survivor camp")

    choice = input("A or B: ")
    if choice == "A":
        lab_entrance()
    elif choice == "B":
        camp()
    else:
        team_with_lucy()


def alone_path():
    print("\nYou leave by yourself,")
    print("A zombie grabs you from behind, you are cooked ngl...")
    print("ENDING: You became a zombie.")
    quit()


#camp scene
def camp():
    print("\nYou arrive at a camp full of survivors,", player_name)
    print("People whisper about a scientist named Dr. Poly controlling the infection, you remember seeing that name on the lab")
    print("Do you:")
    print("A) Stay safe at the camp")
    print("B) Sneak out at night to find the lab")

    choice = input("A or B: ")
    if choice == "A":
        print("\nYou live safely,", player_name, " but never know what really happened.")
        print("ENDING: Peaceful Survival")
    elif choice == "B":
        lab_entrance()
    else:
        camp()


#lab paths
def lab_entrance():
    print("\nYou reach the lab with guards and high fences and she the name 'POLYLAB' on the side.")
    print("Do you:")
    print("A) Sneak in through a vent")
    print("B) Attack the guards directly")

    choice = input("A or B: ")
    if choice == "A":
        lab_core()
    elif choice == "B":
        fight_guards()
    else:
        lab_entrance()


def fight_guards():
    print("\nYou charge at the guards...risky decision,")
    print("You are shot before you get through the gate")
    print("ENDING: Failed Attack.")
    quit()


def lab_core():
    print("\nInside the lab you discover the truth, scientists CREATED the zombies!!!!")
    print("The scientist behind it all is Dr. Poly. She planned to control the world using the virus")
    print("Do you:")
    print("A) Destroy the lab and end the infection")
    print("B) Join Dr. Poly's evil mission to rule what's left of the world")

    choice = input("A or B: ")
    if choice == "A":
        print("\nYou blow up the generators,", player_name, ". The cure spreads into the air.")
        print("Zombies weaken, humanity has a little hope. HERO ENDING!")
    elif choice == "B":
        print("\nYou join Dr. Poly,", player_name, ", and gain power over the survivors.")
        print("ENDING: Villain of the New World")
    quit()


def rooftop_escape():
    print("\nYou climb through the hatch and escape back into daylight,", player_name, ".")
    print("You're alive, but never uncover the truth behind the virus.")
    print("ENDING: Survival Without Answers.")
    quit()


#start the game 
start()
