# Circle Game Solver 🤺

# 🗡️ Welcome to the Circle Game Solver repository! 🔄

## Introduction 🎮

Have you ever wondered which person survives in the classic circle game scenario, where 100 people stand in a circle, and one person with a sword initiates the game by killing the next person and passing on the sword? Look no further! This repository provides a logical and efficient solution for such scenarios. 💻

## The Challenge 🕹️

The challenge involves 100 people standing in a circle, numbered from 1 to 100. The game starts with person No. 1 holding a sword, and each person kills the next in line, passing on the sword until only one person survives. The task is to determine which number survives at the last round.

## The Solution 📈

The solution is based on a logical formula derived from an internet source but further improved and generalized for various cases. The key is to understand the pattern based on the total number of people in the circle.

## Formula 🧮:
   i = 2 * (n - l) + K
- n: Total number of people in the circle.
- l: Nearest power of 2 to the total.
- K: The position or person who initiated the game.
- If i is greater than n, subtract n from i due to the circular nature of the game.

## Examples 🎲:

Given for n is an even number: Say n = 10 and K = 1:
- Nearest power of 2 (l) is 8.
- Using the formula: i = 2 * (10 - 8) + 1 = 5
- Result: 5th person survives.

Given for n is an Odd number: Say n = 43 and K = 36:
- Nearest power of 2 (l) is 32.
- Using the formula: i = 2 * (43 - 32) + 36 = 58
- As i > n, subtract n from i: 58 - 43 = 15
- Result: 15th person survives.

## Usage 🚀

Feel free to use the provided formula in your own applications. The repository also includes sample code for higher n values.

## Contribution 🤝

If you find any mistakes or have suggestions for improvement, please don't hesitate to contribute. Your feedback is highly appreciated!

Happy coding! 🚀✨
