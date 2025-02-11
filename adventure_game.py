import random
import time  # Import time module for delay

def character_selection():
    print("Choose your character:")
    time.sleep(1)
    characters = {
        "1": {"name": "Frodo", "hp": 100, "strength": 30, "wisdom": 80},
        "2": {"name": "Aragorn", "hp": 120, "strength": 90, "wisdom": 70},
        "3": {"name": "Gandalf", "hp": 110, "strength": 50, "wisdom": 100},
        "4": {"name": "Gollum", "hp": 80, "strength": 40, "wisdom": 30}
    }
    for key, value in characters.items():
        print(f"{key}: {value['name']} (HP: {value['hp']}, Strength: {value['strength']}, Wisdom: {value['wisdom']})")
        time.sleep(1)  # Delay between character display
    choice = input("Enter the number of your character: ")
    return characters.get(choice, characters["1"])  # Default to Frodo

def adventure(character):
    corruption = 0  # Tracks good vs. evil choices
    print(f"You are {character['name']} on a quest in Middle-earth.")
    time.sleep(1)

    print("You find the One Ring. What do you do?")
    time.sleep(1)
    print("1: Resist its power and continue your quest (Good)")
    time.sleep(1)
    print("2: Keep it for yourself, tempted by its strength (Evil)")
    time.sleep(1)
    choice = input("Enter choice: ")
    if choice == "2":
        corruption += 1
        print("You feel the Ring's dark influence growing inside you...")
    else:
        print("You remain steadfast in your mission.")
    time.sleep(1)

    print("A Nazgûl approaches! What do you do?")
    time.sleep(1)
    print("1: Fight bravely with sword or magic (Good)")
    time.sleep(1)
    print("2: Try to negotiate, offering secret information (Neutral)")
    time.sleep(1)
    print("3: Betray your allies and join Sauron (Evil)")
    time.sleep(1)
    choice = input("Enter choice: ")
    if choice == "3":
        corruption += 2
        print("You bow to the Dark Lord... your path shifts towards darkness.")
    elif choice == "1":
        print("You fight valiantly and defeat the Nazgûl!")
    else:
        print("You attempt diplomacy. The Nazgûl leaves, but you sense unease.")
    time.sleep(1)

    print("You reach Rivendell. Elrond offers wisdom. Do you:")
    time.sleep(1)
    print("1: Listen and seek guidance for your journey (Good)")
    time.sleep(1)
    print("2: Ignore him and trust only in yourself (Neutral)")
    time.sleep(1)
    print("3: Steal Elrond’s knowledge to serve your own power (Evil)")
    time.sleep(1)
    choice = input("Enter choice: ")
    if choice == "3":
        corruption += 2
        print("You take forbidden knowledge and your soul darkens.")
    elif choice == "1":
        print("Elrond's wisdom strengthens your resolve!")
    time.sleep(1)

    print("You stand at the gates of Mordor. Final choice:")
    time.sleep(1)
    print("1: Destroy the Ring, fulfilling your quest (Good Ending)")
    time.sleep(1)
    print("2: Claim the Ring’s power for yourself (Evil Ending)")
    time.sleep(1)
    print("3: Offer the Ring to Sauron and rule beside him (Dark Lord Ending)")
    time.sleep(1)
    choice = input("Enter choice: ")

    if choice == "1":
        if corruption > 2:
            print("The Ring's corruption was too strong... You fail to throw it in, and darkness wins.")
        else:
            print("With great willpower, you cast the Ring into Mount Doom! Middle-earth is saved!")
    elif choice == "2":
        if corruption < 4:
            print("The Ring's power floods through you... but you resist its darkness. Middle-earth is saved!")
        else:
            print("You take the Ring and power floods through you... but your soul is lost to the darkness.")
    else:
        print("You kneel before Sauron. The world falls into shadow. The Dark Lord has returned.")
    time.sleep(1)

    print("Your journey has ended. Thanks for playing!")

player = character_selection()
adventure(player)
