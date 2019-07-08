# Dice rolling simulator.
# Made by Oliver Bevan in July 2019.
import random


def roll_die(number_of_sides):
    return random.randint(1, number_of_sides)


print("Welcome! How many dice would you like to roll?")
number_of_dice = int(input())  # TODO: Add type checking.
print("Okay, and how many sides would you like the dice to have?")
number_of_sides_on_die = int(input())

print(f"You roll {number_of_dice} dice. They read:")
sum_of_dice_values = 0
for i in range(0, number_of_dice):
    die_value = roll_die(number_of_sides_on_die)
    sum_of_dice_values += die_value
    print(die_value, end=" ")
print(f"\nThey sum to {sum_of_dice_values}.")
