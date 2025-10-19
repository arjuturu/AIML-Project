"""adventure_game.py

A small text-based adventure game for practicing Python functions,
conditionals, loops and user input. The player explores a forest or a cave
and makes choices to try to find a legendary treasure.

This file is part of a course-end project that used GitHub Copilot to assist
in writing and optimizing code. See REPORT.md for details.
"""

print("Welcome to the Adventure Game!")


def input_choice(prompt, options):
    """Prompt until the user enters one of the allowed options.

    Returns the chosen option (lowercased). The user may type 'quit' to exit.
    """
    options_lower = [o.lower() for o in options]
    while True:
        choice = input(prompt).strip().lower()
        if choice == "quit":
            return "quit"
        if choice in options_lower:
            return choice
        print(f"Please enter one of: {', '.join(options)} (or type 'quit' to exit)")


def start_game():
    """Introduce the game, ask for the player's name and present the first choice.

    Returns: 'win', 'lose' or 'quit' depending on the path outcome.
    """
    print("\n--- New Adventure ---\n")
    # Accept any name input; allow the player to type 'quit' to exit
    name = input("Enter your name: ").strip()
    if name.lower() == "quit":
        return "quit"
    # If user didn't type anything useful, use a default
    if not name:
        name = "Explorer"
    print(f"\nHello, {name}! Your quest is to find the legendary treasure.")

    choice = input_choice("Choose your path (forest or cave): ", ["forest", "cave"])
    if choice == "quit":
        return "quit"

    if choice == "forest":
        return forest_path(name)
    elif choice == "cave":
        return cave_path(name)


def forest_path(player_name):
    """Handle the forest scenario with further choices.

    The player can follow a river or climb a tree. Outcomes vary.
    Returns 'win' or 'lose'.
    """
    print("\nYou step into a dense, misty forest. The air is cool and the trees tower above.")
    print("You can follow a nearby river that glitters in the dim light, or try to climb a tall tree to scout the area.")

    choice = input_choice("Do you follow the river or climb the tree? (river/tree): ", ["river", "tree"])
    if choice == "quit":
        return "quit"

    if choice == "river":
        print("\nYou follow the river downstream. The sound of water calms you.")
        print("After a while you find a small boat and a map tucked under a rock.")
        second = input_choice("Do you take the boat or keep walking? (boat/walk): ", ["boat", "walk"])
        if second == "quit":
            return "quit"
        if second == "boat":
            print("\nThe boat carries you across a hidden lake to a ruined island.")
            print("On the island you discover a stone chest — inside, the legendary treasure!")
            return "win"
        else:
            print("\nYou keep walking but the path becomes confusing and you get lost.")
            return "lose"

    else:  # climb tree
        print("\nYou climb the tree carefully. From the top you see smoke rising to the north.")
        approach = input_choice("Do you head toward the smoke or go back down? (smoke/down): ", ["smoke", "down"])
        if approach == "quit":
            return "quit"
        if approach == "smoke":
            print("\nFollowing the smoke you meet a friendly wanderer who shares a clue about the treasure location.")
            print("Using the clue, you find the treasure hidden in a hollow tree. Congratulations!")
            return "win"
        else:
            print("\nYou go back down and lose your bearings in the forest. Night falls and you are forced to turn back.")
            return "lose"


def cave_path(player_name):
    """Handle the cave scenario. The player can light a torch or proceed in the dark.

    Returns 'win' or 'lose'.
    """
    print("\nYou enter a yawning cave. The walls glisten with mineral veins.")
    print("It is pitch dark deeper inside. You can light a torch if you have one, or proceed carefully in the dark.")

    choice = input_choice("Light a torch or proceed in the dark? (torch/dark): ", ["torch", "dark"])
    if choice == "quit":
        return "quit"

    if choice == "torch":
        print("\nYou light the torch and the cave illuminates, revealing ancient carvings.")
        print("Reading the carvings reveals a riddle that points to a hidden chamber.")
        answer = input_choice("Riddle: 'I speak without a mouth and hear without ears. What am I?' (echo/silence): ", ["echo", "silence"])
        if answer == "quit":
            return "quit"
        if answer == "echo":
            print("\nThe rock face slides open to reveal a small chamber filled with gold and jewels — you found the treasure!")
            return "win"
        else:
            print("\nYou answer incorrectly. A trapdoor opens and you fall into a deep pit. Game over.")
            return "lose"

    else:  # dark
        print("\nYou advance in the dark and trip over a hidden ravine. You fall and the adventure ends.")
        return "lose"


def main_loop():
    """Run the game loop until the player quits or chooses not to replay."""
    while True:
        result = start_game()
        if result == "quit":
            print("\nThanks for visiting the Adventure Game. Goodbye!")
            break

        if result == "win":
            print("\nYou won the adventure — the treasure is yours!")
        elif result == "lose":
            print("\nYou lost this attempt. Better luck next time.")
        else:
            print("\nThe adventure ended unexpectedly.")

        again = input_choice("Would you like to play again? (yes/no): ", ["yes", "no"])
        if again == "quit" or again == "no":
            print("\nThank you for playing. Farewell!")
            break


if __name__ == "__main__":
    main_loop()
