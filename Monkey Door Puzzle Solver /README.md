# Monkey Door Puzzle Solver 🐒🚪

Welcome to the Monkey Door Puzzle Solver repository! 🐵🔓

## Introduction 🤓

Have you ever wondered about the state of 100 doors after 100 monkeys have had their way with them? 🚪🔐 
In this classic puzzle, each monkey has a specific task regarding the doors, and our goal is to determine the number of doors left open after all 100 monkeys complete their work.

## The Challenge 🚀

There are 100 doors and 100 monkeys, initially all doors are closed. Each monkey has a unique task:

- 🐒 Monkey 1 opens every door as every door initially closed
- 🐒 Monkey 2 attends the even-numbered doors say 2,4,6,8,..... and closes them as they all are open by Monkey 1
- 🐒 Monkey 3 attends the doors at every third position say 3,6,9,.... and if the door is open it closes, if not it opens. 
- And so on...

After all 100 monkeys have completed their tasks, we want to find out how many doors are left open.

## STOP 🛑 
I request you to pause and try solving the problem for a minute. Don't think they are silly problems, they have been asked in FAANG company interviews. 

## The Generalized Solution 📈

The solution to this puzzle involves understanding the pattern and behavior of the doors based on their divisors. A key insight is that the doors touched by monkeys will open and close in a predictable manner.

Solution Strategy:
- Choose a number within the given range (eg. 48).  
- Find all divisors of the chosen number.  
- Observe the opening and closing pattern based on the divisors. 
- Determine the state of each door after the last pass.

## Generalized Example 🌟

For now I took 48 monkeys and 48 doors as my example, 

- The number 48 has divisors (1,48), (2,24), (3,16), (4,12), (6,8) Which makes a list of (1,2,3,4,6,8,12,16,24,48)
- Why divisors ? Observe the pattern, In eg. 48, 1 attends the door and opens, now 2 attends and closes, 3 opens, 4 closes, 6 opens, 8 closes, 12 opens, 16 closes, 24 opens, 48 closes at last it comes under initial state where the door was closed before 1 attends. 
- Monkeys will open and close doors based on this pattern.
- After the last monkey pass, the doors will return to their initial state.

## Catch in solution 🎣

- However, for perfect square numbers (e.g., 16), the pattern is different. Did you observe that?
- They end up in the opposite state of the initial state.

## Result 🎯
- For the 100 monkey 100 doors the solution is 10. As 10 is perfect square of 100. So at the end 10 doors will be left open. 

## Usage 🚀

Feel free to use the provided code to solve similar puzzles for different ranges. Simply input the desired range into the code, and it will output the number of doors left open.

## Contribution 🤝

If you have any suggestions, improvements, or want to contribute to enhancing the code, feel free to do so! Your expertise is highly valued.

**Happy puzzling! 🐒🚪**
