# Dungeon of Shadows

Welcome to **Dungeon of Shadows**, a text-based adventure game where you must navigate a dark dungeon, battle monsters, and uncover hidden treasures to survive!

## 📜 Game Overview
You find yourself in a mysterious dungeon with dangers lurking around every corner. Your goal is to explore, gather items, fight monsters, and find the exit before your health runs out.

## 🎮 How to Play
Run the script to start the game and enter commands to control your character.

### 🕹️ Commands:
- `help` → Displays a list of available commands.
- `move [direction]` → Moves the player in the specified direction (north, south, east, west).
- `search` → Searches the room for hidden items or dangers.
- `use [item]` → Uses an item from the inventory.
- `fight` → Engages in battle with a monster (if present).
- `quit` → Exits the game.

## 🏹 Game Mechanics
- **Health**: Starts at 100. Decreases when fighting monsters.
- **Damage**: Default is 20. Can be boosted by certain items.
- **Inventory**: Stores items found during gameplay.
- **Rooms**: Each room has a description, exits, and items.
- **Locked Doors**: Some rooms may be locked, requiring keys to enter.

## 🏆 Items & Power-ups
- **Health Potion** → Restores health.
- **Dagger** → Basic weapon.
- **Torch** → Helps illuminate the dungeon.
- **Key** → Unlocks doors.
- **Rare Relic** → A valuable collectible.
- **Damage Boost** → Doubles attack damage.
- **Extra Health** → Adds health (if not already full).

## 🦇 Fighting Monsters
When encountering a monster:
- Your health decreases by 40 upon attack.
- If health drops to 0, the game is over.
- If you defeat the monster, it is removed from the room.

## 🔧 Installation & Running the Game
1. Ensure you have Python installed (version 3.x recommended).
2. Download or clone the project.
3. Run the script:
   ```sh
   python dungeon_game.py
   ```
4. Follow the on-screen instructions to play.

## 👨‍💻 Future Enhancements
- Implement a storyline with multiple endings.
- Add more enemy types and combat mechanics.
- Introduce NPCs for interactions.
- Expand the dungeon with more rooms and puzzles.

Enjoy your adventure in the **Dungeon of Shadows**! 🏰🔥

