## AppDynamics

- Designation: Software Engineer I
- Place of Posting: Bangalore
- CTC: 4626048 INR Per Annum
- Gross: 2993548 INR Per Annum
- Base Salary: 1749000 INR Per Annum :laughing:

___

### Online Round

- Platform: HackerRank
- Duration: 1.5 hours
- Number of Questions: 15
    + 12 MCQs Algorithm, Aptitude, DBMS etc
    + 3 Coding Questions

#### Coding Questions

**1. Vowels.** 
    
Given an input array of strings **A**. A valid string is a string that starts and ends at vowels. Given a series of queries where each query of two integers i and j. Find the number of valid strings in the array A[i:j].

**2. Maximize Profit**

Given an Array **A**. Here A[i] denotes the number of items the seller A[i] has. The cost at which a seller sells his items is equal to the number of items he currently has.

For e.g A shopkeeper with 5 items will sell each item at rates 5, 4, 3, 2, 1.

Given the Array **A** and the number of items **k** that a customer intents to buy. What is the maximum profit that the sellers can collectively obtain.

For e.g: A = [3, 5], k=6  
Max cost = 5 + 4 + 3 + 3 + 2 + 2 = 19

**3. Sum of longest common prefix of all suffixes with the original string.**

Let **Suf<sub>i</sub>** denotes a suffix of the a string **S**. Let **L<sub>i</sub>** be the length of the longest common prefix of **S** and **Suf<sub>i</sub>**.    
Find the sum of all **Li**'s.

___

#### Experience

**Question 1**

- [Link to solution](https://github.com/hthuwal/competitive-programming/blob/master/HackerRank/vowels.py)
- Started doing it with segment trees.
- After implementing `create` function of the segment tree realized that it doesn't involves updates and can be done using difference arrays.
- Used Python. Accepted. :smile:

**Question 2**

- Greedy Approach: At any given moment the item will be sold by the seller with highest number of items.
- Implemented in python using Counters. TLE in 4-5 test cases. :fearful:
- Implemented the same algorithm in C++. All test cases passed. :relaxed:

**Question 3**

- Given string size was in range 1 to 10<sup>5</sup>.
- Was sure brute force O(n<sup>2</sup>) would get TLE in some cases.
- 20 Minutes Remaining.
- Tried to come up with a better algorithm for about 8-9 minutes.
- With 10 minutes remaining implemented the brute force in python.
    + TLE in 4-5 cases. (Similar to Question 2 :astonished:)
- Seeing this Quickly Implemented the brute force in C++.
    + All Test Case Passed. :yum:

---

#### Takeaways

- **Selecting Language to do the code is a pain. If you choose C++ You might get stuck debugging difficult code that could have been done easily in python. But python at the same time could give you TLE even with an algo that works fine in C++.**
- So be agile and quick to realize the wrong choice of language/algo. 
