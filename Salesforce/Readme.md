## Salesforce

- Designation: Associate member of technical staff
- Place of Posting: Hyderabad
- CTC: 3200000 INR Per Annum
- Base: INR 15Lakhs

### Coding Test

- Platform: HackerRank
- Duration: 1 Hour
- 3 Coding Questions

[Screenshot of the first two problems](coding-exam.pdf)

##### 1. Snake Sequence

Given a 2D-grid of integers input, find and return the size of maximum Snake Sequence.

A snake sequence is made up of adjacent numbers in the grid such that for each 
number, the number on the right or the number below it is +1 or -1 its. Value.

Your starting position is always at the top left corner of the grid.

- Simple DP works (n x m grid)
    + Every node is itself a snake sequence of length 1
        ```cpp
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                dp[i][j] = 1;
        ```
    + For the first row you can reach the cell only from the left and for the first column you can reach the cell only from the above.
        ```cpp
        for(int i=1; i<m;i++)
            if(abs(grid[0][i] - grid[0][i-1]) == 1)
                dp[0][i] = 1 + dp[0][i-1];
        ```
        ```cpp
        for(int i=1; i<n;i++)
            if(abs(grid[i][0] - grid[i-1][0]) == 1)
                dp[i][0] = 1 + dp[i-1][0];
        ```
    + One can reach a cell i, j from either i-1, j or i, j-1
        ```cpp
        for(int i=1;i<n;i++)
        {
            for(int j=1;j<m;j++)
            {
                if(abs(grid[i][j]-grid[i-1][j]) == 1)
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + 1);
                
                if(abs(grid[i][j]-grid[i][j-1]) == 1)
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + 1);
            }
        }
        ```
    + Answer is the maximum entry in the entire dp table.
+ Made a stupid coding mistake of running both for loops upto `n` in the above code. Wasted 5-10 minutes to find this bug.
+ All 4 test cases passed :smile:

##### 2. Reduce to Zero

Given a number N.You can perform any of the two operations on N in each move:

1. If we take 2 integers a and b where , N = a*b (a != 1 and b != 1), then we can change N = max(a, b).
2. Decrease the value of  by .

Determine the minimum number of moves required to reduce the value of N to 0.


- Simple DP solution. Was Getting Wrong Answer for 2/4 test cases. Couldn't debug it till the end.
- [HackerRank: Down to zero](https://www.hackerrank.com/challenges/down-to-zero-ii/problem). Slightly advanced version with multiple queries instead of just 1.
- [Solution to Down to zero problem](https://github.com/hthuwal/competitive-programming/blob/master/HackerRank/down-to-zero-2.cpp) Apparently filling dp backwards gives TLE but filling it in forward manner works just fine. :confused:

##### [3. Count number of possible decodes of the string](https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/)

Let 1 represent 'A', 2 represent 'B', etc. Given a digit sequence count the number of possible decodings of the given digit sequence.

- Simple DP.
- Was getting wrong answer for 1/4 test cases.
- Took some time but figured out the bug. Didn't handle the case when current digit is 0 correctly.
- All test cases passed. :smile: