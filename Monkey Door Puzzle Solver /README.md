# Monkey Door Puzzle Solver 🐒🚪

Welcome to the Monkey Door Puzzle Solver repository! 🐵🔓

## Introduction 🤓

Have you ever wondered about the state of 100 doors after 100 monkeys have had their way with them? 🚪🔐 
In this classic puzzle, each monkey has a specific task regarding the doors, and our goal is to determine the number of doors left open after all 100 monkeys complete their work.

## The Challenge 🚀

There are 100 doors, initially all closed. Each monkey has a unique task:

- Monkey 1 opens every door.
- Monkey 2 closes the even-numbered doors.
- Monkey 3 toggles the doors at every third position.
- And so on...

After all 100 monkeys have completed their tasks, we want to find out how many doors are left open.

## Note: I request everyone to pause and try solving the problem for a minute. Don't think they are silly problems, they have been asked in FAANG company interviews. 

## The Solution 🎯

The solution to this puzzle involves understanding the pattern and behavior of the doors based on their divisors. A key insight is that the doors touched by monkeys will open and close in a predictable manner.

Solution Strategy:
- Choose a number within the given range (e.g., 56).
- Find all divisors of the chosen number.
- Observe the opening and closing pattern based on the divisors.
- Determine the state of each door after the last pass.

## Example:

For the range of 1 to 100:

- The number 56 has divisors 1&56, 2&28, 4&14, 7&8.
- Monkeys will open and close doors based on this pattern.
- After the last pass, the doors will return to their initial state.
- However, for perfect square numbers (e.g., 16), the pattern is different. They end up in the opposite state of the initial state.

## Usage 🚀

Feel free to use the provided code to solve similar puzzles for different ranges. Simply input the desired range into the code, and it will output the number of doors left open.

## Contribution 🤝

If you have any suggestions, improvements, or want to contribute to enhancing the code, feel free to do so! Your expertise is highly valued.

**Happy puzzling! 🐒🚪**
