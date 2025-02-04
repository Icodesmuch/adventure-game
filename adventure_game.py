### **3. Text-Based Adventure Game**

# - **Concepts:** Loops, conditionals, dictionaries.
# - **Key Features:** User choices affect the outcome.
# - **What You’ll Learn:**
#     - Nested conditionals (`if-elif-else`)
#     - Using dictionaries for game logic
#     - Structuring a simple game loop


# Game Idea: "Dungeon of Shadows"
# A text-based adventure game where the player explores a dark dungeon, fights monsters, collects treasures, and tries to escape alive.

# Game Features:
# Rooms & Exploration: The player moves between different dungeon rooms, encountering random events.
# Combat System: The player can fight or flee when encountering monsters.
# Inventory System: Collect potions, weapons, and keys to unlock doors.
# Random Events: Traps, treasure chests, or secret passages.
# Win/Lose Condition: Escape the dungeon to win; die from monsters or traps to lose.
# Basic Gameplay Flow:
# Player starts in a dark dungeon with minimal supplies.
# Moves through rooms using commands like "north", "south", "east", "west".
# Encounters random events (monsters, loot, locked doors).
# Chooses to fight, flee, or use items in battles.
# Tries to find the exit before running out of health.
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
            print("  - flee")
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

            # Allow the player to encounter a rare relic, monster, health and damage multiplier
            # random.seed()
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
        elif command == "flee":
            print("Fleeing...")
        elif command == "quit":
            print("Quitting...")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")
        print("")

def searchController():
    randomInt = random.randint(0,len(room["findables"]))
    item = room["findables"][randomInt]
    if item == "rare relic":
        print("You found a rare relic.")
    elif item == "damage boost": 
        print("You found a 2x damage boost.")
        damage = player["damage"] * 2
        print("Your damage is now " + damage)
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
    if room["item"] == "monster":
        player["health"] = player["health"] - 40
        print("You defeated the monster.")
        if player["health"] == 0:
            print("You were killed by the monster.")
            return "gameover"
    else:
        print("There are no monsters in this room.")

    
if __name__ == "__main__":
    game()