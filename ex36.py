from sys import exit

inventory = []

def start():
    print("""You wake up next to a rather nice looking house on a deserted island.
You notice the front door is slightly ajar.""")
    print("What do you do?")

    enter = input("---> ")

    if "door" in enter:
        entryway()
    elif "swim" in enter:
        print("You swim as hard as you can until you tire and pass out from exhaustion...")
        start()
    elif "boat" in enter:
        print("Your boat runs out of gas and while stranded out at sea you get thrown off the boat and lose consciousness.")
        start()
    else:
        die("Do you always give up this early?")

def die(failure):
    print(failure, "Try again!")
    exit(0)

def win():
    print("Congratulations! On to the next adventure!")
    exit(0)

def entryway():
    print("The door leads to a small room with a locked door leading into the house.")
    print("There is a shelf on your right.")
    print("Lots of choices for what to do here...")

    get_key = input("---> ")

    if "shelf" in get_key:
        print("You find a rusty key laying on the shelf and pick it up.")
        inventory.append("rusty key")
        print("You now have a", inventory[0], "in your inventory.")

        use_key = input("---> ")

        if "open door" or "use key" in use_key:
            living_room()
        else:
            die("Keys are normally good at opening doors...")
    else:
        print("You get bored and wander back outside to find the tide has risen and sweeps you out to sea.")
        start()

def helipad():
    print("You stumble onto the roof of the building and find a helipad.")
    print("There is a helicopter on the pad and a pilot is filling it with gas.")
    print("He flies you back to civilization.")
    win()

def tree_room():
    print("You burst through the door and find that the floor is covered with grass and the ceiling is gone.")
    print("A tree is growing in the middle of the room.")
    print("There are quite a few skeletons lying around and an axe lying by the tree.\nYou can tell that others have tried cutting down the tree before.")

    lumberjack = input("---> ")

    if "tree" and "use axe" or "hack" or "cut" or "chop" in lumberjack:
        print("You get very tired right as you get half-way through hacking at the tree and are tempted to take a nap to rest.")

        nap_time = input("---> ")

        if nap_time == "take a nap":
            die("You fall asleep and never wake up, joining those that came before you...")
        else:
            print("You power through with the determination of Paul Bunyan and finish chopping that tree down.")
            print("You spit on the tree to show that you don't respect its \"magical powers\" garbage.")
            print("You find a small hollow in the tree trunk with a small carved helicopter.")
            print("That's literally the only reason for this room...")
            print("It is a pretty sweet carving though.")
            print("You head back to the living room")
            inventory.append("carved helicopter")
            living_room()
    else:
        print("You need to unleash your inner Paul Bunyan.")
        tree_room()

def living_room():
    if "carved helicopter" in inventory:
        print("Maybe this stupid carving can fly me out of here...lol")

        helicopter = input("---> ")

        if "fly" or "helicopter" in helicopter:
            print("I guess you don't know if you don't try...but no, this carving isn't flying")
            print("Give it another go.")
            living_room()
        elif "last door" in helicopter:
            print("You walk over to the last door and notice that instead of a key hole there is a helicopter carving sized hole... strange...")

            finale = input("---> ")

            if "open door" or "use helicopter carving" or "use carving" in finale:
                helipad()
            else:
                print("The door! Open the door! What could go wrong?")
                living_room()
    else:
        print("You enter the living room.")
        print("You see two doors with signs above them labeling them \"first\" and \"last.\"")
        print("Which door will you choose?")

        which_door = input("---> ")

        if which_door == "first":
            print("Being a deductive genius you choose the first door, which swings wide open.")
            tree_room()
        elif which_door == "last":
            print("Locked, and no handy shelf is nearby where one might find a key.")
            print("Disgusted with yourself for not trying the \"first\" door first, you look around to see if anyone was watching you embarrass yourself.")
            print("You decide that the \"last\" door is going to get broken down because nobody makes you look foolish.")
            print("You back up to the far wall for a running start and ram your shoulder into the unlocked door...")
            tree_room()

start()
