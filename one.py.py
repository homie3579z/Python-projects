"""
Dice Rolling Game
PS No: 54
Description: A program that rolls a die a number of times chosen by the user,
             shows the frequency of each face, the total, the average,
             and the most frequent face.
Language: Python 3
Concepts: Random, Loops, Functions, Statistics
"""

import random


def get_number_of_rolls():
    """
    Prompt the user to enter the number of rolls.
    Validates that the input is a whole number between 1 and 1000 (inclusive).
    Keeps asking until valid input is provided.
    """
    while True:
        user_input = input("Number of rolls: ")
        try:
            num = int(user_input)
            if 1 <= num <= 1000:
                return num
            else:
                print("Invalid input. Enter a whole number from 1 to 1000.")
        except ValueError:
            print("Invalid input. Enter a whole number from 1 to 1000.")


def roll_dice(num_rolls):
    """
    Roll the die 'num_rolls' times using the random module.
    Each roll produces a random integer between 1 and 6.
    Returns a list of all roll results.
    """
    rolls = []
    for i in range(num_rolls):
        roll = random.randint(1, 6)
        rolls.append(roll)
        if num_rolls == 1:
            print(f"Roll: {roll}")
        else:
            print(f"Roll {i + 1}: {roll}")
    return rolls


def calculate_frequency(rolls):
    """
    Calculate the frequency of each die face (1 to 6).
    Stores the frequency in a dictionary.
    Returns the frequency dictionary.
    """
    frequency = {face: 0 for face in range(1, 7)}
    for roll in rolls:
        frequency[roll] += 1
    return frequency


def calculate_statistics(rolls):
    """
    Calculate the total and average of all rolls.
    Returns a tuple of (total, average).
    """
    total = sum(rolls)
    average = total / len(rolls)
    return total, average


def find_most_frequent(frequency):
    """
    Find the most frequent face(s) from the frequency dictionary.
    Handles ties (multiple faces with the same highest frequency).
    Returns a tuple of (list_of_faces, max_count).
    """
    max_count = max(frequency.values())
    most_frequent_faces = [face for face, count in frequency.items() if count == max_count]
    return most_frequent_faces, max_count


def display_results(frequency, total, average, most_frequent_faces, max_count):
    """
    Display the frequency, total, average, and most frequent face(s)
    in the required format.
    """
    # Display frequency
    freq_parts = [f"{face}:{count}" for face, count in frequency.items()]
    freq_str = " | ".join(freq_parts)
    print(f"Frequency: {freq_str}")

    # Display total and average
    print(f"Total: {total} | Average: {average:.2f}")

    # Display most frequent face(s)
    if len(most_frequent_faces) == 1:
        face = most_frequent_faces[0]
        if max_count == 1:
            print(f"Most frequent: {face} ({max_count} time)")
        else:
            print(f"Most frequent: {face} ({max_count} times)")
    else:
        faces_str = " and ".join(str(f) for f in most_frequent_faces)
        print(f"Most frequent: {faces_str} ({max_count} times each)")


def play_game():
    """
    Main game function that orchestrates one round of the Dice Rolling Game.
    Gets the number of rolls, rolls the dice, calculates statistics,
    and displays the results.
    """
    # Step 1: Get number of rolls from user
    num_rolls = get_number_of_rolls()

    # Step 2: Roll the dice
    rolls = roll_dice(num_rolls)

    # Step 3: Calculate frequency
    frequency = calculate_frequency(rolls)

    # Step 4: Calculate total and average
    total, average = calculate_statistics(rolls)

    # Step 5: Find most frequent face(s)
    most_frequent_faces, max_count = find_most_frequent(frequency)

    # Step 6: Display results
    display_results(frequency, total, average, most_frequent_faces, max_count)


def main():
    """
    Entry point of the program.
    Runs the game in a loop, asking the user if they want to play again.
    """
    print("=" * 50)
    print("       WELCOME TO THE DICE ROLLING GAME")
    print("=" * 50)
    print()

    while True:
        play_game()
        print()
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
