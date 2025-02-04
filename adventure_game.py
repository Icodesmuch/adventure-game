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
                "items": ["torch", "key", "monster", "rare relic", ],
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



        elif command.startswith("use"):
            item = command.split(" ", 1)[1]
            if item in player["inventory"]:
                print("Using", item)
            else:
                print("You don't have that item.")
        elif command == "fight":
            print("Fighting...")
        elif command == "flee":
            print("Fleeing...")
        elif command == "quit":
            print("Quitting...")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")
        print("")
    


if __name__ == "__main__":
    game()