# puzzles
generalized formularization for puzzles




Problem 1:
100 people standing in a circle in an order 1 to 100. No. 1 has a sword. He kills the next person (i.e. No. 2) and gives the sword to the next (i.e. No. 3). All people do the same until only 1 survives. Which number survives at the last? 
Solution: 
The solution is pure logic based and I found this in some internet but I improvised it and made the formula for all the general cases. So, lets start with the logic I found on internet. My way of approach towards the problem is different I analyze and I understand the missing parts, find solution and improvise for the general case. Same I have done here.
Keywords: circle in an order 1 to 100, No. 1 starts the game, kills the next person to him and pass on, who survives.
missing parts: we don't the position of the person who survives. 
solution: This is logical one I got it from internet. So, I will try to put it short and simple though understandable. Lets say if the total number of people in circle is equal to the power of 2. (Power of 2 is multiples of 2. ex: 25 = 2x2x2x2x2). Then the person who initiated the game will be alive. To understand this, take a small example: say 8 which is 23 , So 8 people are in circle and if we start with 1st person and in round 1: 2,4,6,8 is killed, round 2: 3,5,7 is killed, 1 is the one left who initiated the game. Take any example you will find this if total number of people is equal to 2x .
Case 2 : If the total number is not equal to 2x , which is in above question where total is 100.  As 100 is not equal to 2x . We find the nearest possible of 2x  less than the total which is 26 =64. Now we split the total by 100 - 64 = 36. i.e 36 people need to die when 64 people be alive. So the 36th person got killed by twice of him which is 72th person and then after he passes the sword to the next person 73rd and he kills the 72nd. So 73rd will survive till last. Here after we will generalize it for all the cases with different numerical inputs.  
My formula is i = 2 (n-l) + K where i ≤ n, if i > n then we need to difference the n from i because as it is a loop or circle there exists the continuity after n from beginning.  
where n = total number of people in a circle, l = nearest power of 2 to the total, K = The position or person who initiated the game.  
To prove this we can use trial and error method or induction method. 
I'll give small example with two scenarios: 
Lets say n = 10 which is total number of people in circle and K = 1 which is No 1 has the sword to kill next to him.
Sol: if n=10 then the nearest power of 2 is 8 = 23 as 24 = 16 which exceed the n. So l = 8, by using over formula we say i = 2 (10-8) + 1 = 5 th person will survive. Lets do it manually as No 1. holds the sword he kills 2 and passes to 3 and so on. In first round : 2,4,6,8,10 get killed, in second round: 3,7,1 get killed, last round: 9 get killed and 5 remains.

Lets take a different example where we change the position of initiating and also try using the n value to be some odd number instead of even number which we did in above cases. Lets say n = 43 and K = 36. 
Sol: By above information we say l = 32 which is 25 . And using above formula we get i = 58 and as i >n we subtract n from i. So the final result is 15th person survives. Lets do it manually. In first round: 37,39,41,43,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36. In second round: 40,1,5,9,13,17,21,25,29,33,38. In third round: 3,11,19,27,35,7. In fourth round:23,42,31. Finally 15 remains and survives the game. 
I even tried different possibilities with prime numbers and many other options if you find any mistakes or can be able improvise the formula. Please let me know.  And also here is the code to try for higher n values. 
