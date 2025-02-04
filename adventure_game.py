import random
player = { "name": "player",
                "health": 100,
                "damage": 20,
                "inventory": ["health potion", "dagger"],
                "gold": 0,
                "keys": 0
            }

room = { "name": "room",
                "description": "You are in a dark room.",
                "exits": ["north", "south", "east", "west"],
                "items": ["torch", "key", "monster"],
                "findables" : ["rare relic", "damage boost", "extra health"],
                "locked": True
            }   
def game():  
    print("Welcome to Dungeon of Shadows!")
    print("You are in a dark dungeon. Try to find the exit before you run out of health.")
    print("Type 'help' for a list of commands.")
    print("")

    while True:
        print(room["description"])
        print("Exits:", room["exits"])
        print("Items:", room["items"])
        print("")

        command = input("Enter your command: ").strip().lower()

        if command == "help":
            print("Commands:")
            print("  - move [direction]")
            print("  - search")
            print("  - use [item]")
            print("  - fight")
            print("  - quit")
            print("")
        elif command.startswith("move"):
            direction = command.split(" ", 1)[1]
            if direction in room["exits"]:
                print("Moving", direction)
            else:
                print("You can't move in that direction.")
        elif command == "search":
            print("Searching...")
            searchController()
            
        elif command.startswith("use"):
            item = command.split(" ", 1)[1]
            if item in player["inventory"]:
                print("Using", item)

            else:
                print("You don't have that item.")
        elif command == "fight":
            print("Fighting...")
            outcome = fightController(room,player)
            if outcome == "gameover":
                break
        elif command == "quit":
            print("Quitting...")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")
        print("")

def searchController():
    randomInt = random.randint(0,(len(room["findables"]) - 1))
    item = room["findables"][randomInt]
    if item == "rare relic":
        print("You found a rare relic.")
    elif item == "damage boost": 
        print("You found a 2x damage boost.")
        damage = player["damage"] * 2
        print("Your damage is now " + str(damage))
    elif item == "extra health":
        print("You found a extra health")
        if player["health"] == 100: 
            print("Health already full.")
            return
        elif player["health"] <= 80:
            player["health"] = player["health"] + 20 
            print("Health Replenished.")
            print("Health: " + player["health"])
             
    player["inventory"].append(item)



def fightController(room, player):
    for item in room["items"]:
        if item == "monster":

            player["health"] = player["health"] - 40
            room["items"].remove("monster")
            print("You defeated the monster.")

            if player["health"] <= 0:
                print("You were killed by the monster.")
                return "gameover"
            break
    else:
        print("There are no monsters in this room.")

    
if __name__ == "__main__":
    game()