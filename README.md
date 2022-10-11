# puzzles
generalized formularization for puzzles




Problem 1: 100 people in a circle with a sword puzzle  

100 people standing in a circle in an order 1 to 100. No. 1 has a sword. He kills the next person (i.e. No. 2) and gives the sword to the next (i.e. No. 3). All people do the same until only 1 survives. Which number survives at the last? 

Solution: The solution is pure logic based and I found this in some internet but I improvised it and made the formula for all the general cases. So, lets start with the logic I found on internet. My way of approach towards the problem is different I analyze and I understand the missing parts, find solution and improvise for the general case. Same I have done here.
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





Problem 2: Monkeys with keys of doors 

There are 100 doors, all closed. In a nearby cage are 100 monkeys. The first monkey is let out, and runs along the doors opening every one. The second monkey is then let out, and runs along the doors closing the 2nd, 4th, 6th,… — all the even-numbered doors. The third monkey is let out. He attends only to the 3rd, 6th, 9th,… doors (every third door, in other words), closing any that is open and opening any that is closed, and so on. After all 100 monkeys have done their work in this way, what state are the doors in after the last pass? Answer with the number of open doors. Answer is a integer. Just put the number without any decimal places if its an integer. If the answer is Infinity, output Infinity.

Solution: The solution is pretty simple. Consider a number between the range. Let's say in our case it is 100 doors and 100 monkeys, So pick a number between 1-100. I considered number 56 where we find all the divisors of 56. Why divisors, lets understand if we take the divisors of 48 it is 1&48, 2&24, 3&16, 4&12, 6&8. Monkeys will visit all the divisor doors of 56 where on pass 1 they open the door and on 2nd they close, on 3th they open again and on 4th they close, 6th they open and 8th they close, 12th open, 16 they close, 24th they open and finally 48th its close which gives a conclusion that consider any number and you find at last it comes under the initial state, but in consider of any perfect square number say 16, the divisor are 1&16, 2&8, 4&4, here the 4 repeats and in similar cases every perfect square have a number repeated in divisor as they called perfect square numbers. Now on pass 1 they open, on 2nd they close, 4 they open, 8th they close but in 16 at end they open which is opposite of initial state. This shows the perfect squares doors will be in the opposite position of initial state and others are in initial state always. So the number of perfect squares in range of 1 to 100 is 10. So the answer is 10 and to get the number of perfect squares in any range here is my code.






Problem3: 100 cows and milk distribution among 10 equally

A milkman has 100 cows number from 1 to 100. Every cow gives milk according to their numbers i.e i'th cow gives i litre milk. Milkman has 10 sons and he wants to divide his cows among his 10 sons so that every son should get an equal amount of milk, the task is to help him to know about the division of these cows among the sons. 

Solution: The solution is pure logic based and I found this in some internet but I improvised it and made the formula for all the general cases. So, lets start with the logic I found on internet (in this case it is geeksforgeeks.org). My way of approach towards the problem is different I analyze and I understand the missing parts, find solution and improvise for the general case. Same I have done here.
keywords: pairing, arithmetic progression
As we know that the i'th cow gives i litres milk. So first let us count the total litre of milk which is obtained from these cows. This can be solved by using arithmetic progression sum.
We know that sum of n numbers starting from 1 is always, sum = n*(n+1)/2 .
So the total quantity of milk obtained if from 100 cows is total milk = 100(100+1)/2=5050 litres.
As the problem says that the division of the cows should be done in a manner that every son get equal amount of milk. So every son should get 5050/10 = 505 litres of milk.
Now our main problem is to divide 1 to 100 numbers in such a way that every sons should get 10 cows who’s number sum up to 505. Here, I tried to analyze and make a generalized method of division so that the number is distributed equally at any situation. So the formula is same as above its n*(n+1)/2m where n is total number of cows and m is number of division to be made. Its not about calculating the and analyzing the amount to be shared it is how to make the division. In our case we need to analyze the distribution that every one gets the milk of 505 litres at the end of division. Which mean the sum to be 505. In my way I tried to make a division by pairs lets say n = 10 and m = 5 then the pair distribution should be as follows say the m = 5 people as {a, b, c, d, e} the distribution must be like a-(1,10), b-(2,9), c-(3,8), d-(4,7), e-(5,6). So that the numbers add up to be same in every person. Similarly in the above case the 1 st person gets (1,100), (11,90), (21,80), (31,70),(41,60) and similar till 10th person where you get (10,91),(20,81),(30,71),(40,61),(50,51). We need to consider that if the total is not divided perfectly in pairs to the number of people then the solve we made need few addition they are lets understand with an example say n = 17 and m = 5. We make the distribution in round wise say in round we distributed each pair to each in m. a-(1,17), b-(2,16), c-(3,15), d-(4,14), e-(5,13). In round two the distribution cannot be done equally in pairs as we left over with (6,12), (7,11), (8,10), 9. So in order to distribute it equally we add up everything and we divide them by m. In cows case if they are 17 cows we cannot divide the cows equally so we add up the litres of milk and divide the milk among the m = 5. The left over sum up to 63 which is divide among 5 is 12.6 so the number of litres shared to each is 12.6+1+17 = 30.6.
I even tried different possibilities with different numbers and many other options if you find any mistakes or can be able improvise the formula. Please let me know.  And I need to update the code to try for higher n values. If you are trying to code use (i+1, n-i) for i in range(n) so that you can pair as I said above.  I'll try to  make update as soon as I get free. Thank you. 
