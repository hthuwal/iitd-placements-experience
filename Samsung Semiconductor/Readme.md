## Samsung Semiconductor India R&D Center

- Designation: Senior Engineer – Software
- Place of Posting: Bangalore
- CTC: 2200000 INR Per Annum (B.Tech), 2300000 INR Per Annum (M.Tech)
- Basic: 1500000 INT Per Annum

---

## Online Test

- Platform: Their same old shitty software.
- 1 Question
- 3 Hours.

### Question: Mr. Kim and his refrigerators.

Mr. Kim has to deliver refrigerators to N customers. From the office, he is going to visit all the customers and then return to his home. Each location of the office, his home, and the customers is given in the form of integer coordinates (x,y) (0≤x≤100, 0≤y≤100) . The distance between two arbitrary locations (x1, y1) and (x2, y2) is computed by |x1-x2| + |y1-y2|, where |x| denotes the absolute value of x; for instance, |3|=|-3|=3. The locations of the office, his home, and the customers are all distinct. You should plan an optimal way to visit all the N customers and return to his home among all the possibilities.

You are given the locations of the office, Mr. Kim’s home, and the customers; the number of the customers is in the range of 5 to 10. Write a program that, starting at the office, finds a (the) shortest path visiting all the customers and returning to his home. Your program only have to report the distance of a (the) shortest path.

**Constraints**

5≤N≤10.   
Each location (x,y) is in a bounded grid, 0≤x≤100, 0≤y≤100, and x, y are integers.

**Input:**

You are given 10 test cases. Each test case consists of two lines; the first line has N, the number of the customers, and the following line enumerates the locations of the office, Mr. Kim’s home, and the customers in sequence. Each location consists of the coordinates (x,y), which is represented by ‘x y’.

**Output:**

Output the 10 answers in 10 lines. Each line outputs the distance of a (the) shortest path. Each line looks like ‘#x answer’ where x is the index of a test case. ‘#x’ and ‘answer’ are separated by a space.

**I/O Example**

Input (20 lines in total. In the first test case, the locations of the office and the home are (0, 0) and (100, 100) respectively, and the locations of the customers are (70, 40), (30, 10), (10, 5), (90, 70), (50, 20).)

5   
0 0 100 100 70 40 30 10 10 5 90 70 50 20   
6   
88 81 85 80 19 22 31 15 27 29 30 10 20 26 5 14   
10   
39 9 97 61 35 93 62 64 96 39 36 36 9 59 59 96 61 7 64 43 43 58 1 36   

**Output (10 lines in total)**

Case #1: 200   
Case #2: 304   
Case #3: 366  

### Experience

- Had already discussed this question with [Shadab](https://github.com/dufferzafar).
- The Question clearly stated that the goal was not find an efficient solution.
- If one is able to enumerate all possible paths then all test cases would pass.
- Write a simple recursive function to print all possible permutations of intermediate nodes. [Similar to this.](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/)
- Calculate the cost corresponding to each permutation.
- Return the minimum cost.
- All test cases passed. :smile: