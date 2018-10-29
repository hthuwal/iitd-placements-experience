## Amazon Development Centre India Private Limited

- Designation: Software Development Engineer
- Place of Posting: Bangalore, Hyderabad, Chennai, Delhi
- CTC: 2875000 INR Per Annum
- Base Salary: 13,00,000 INR Per Annum

### Online Test

- Platform: [HackerEarth](https://www.hackerearth.com/)
- Duration: 1 hour 30 minutes
- 20 MCQ covering OOPS, DS, Algorithms, OS, Networks etc.
- 2 Coding Questions

Screenshots of Questions are present [here.](coding-exam.pdf)

**1. Walls**

- There code for reading input in  C++14 was wrong. Glad that I found this out quickly and threw all of their code.
- Started by writing a simple brute force solution. For each pair of walls calculate the volume of water they can hold. Return the maximum volume.
    ```cpp
    int ans = INT_MIN;
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            int volume = min(wall[i], wall[j]) * (j-i);
            if(volume > ans)
                ans = volume;
        }
    }
    return ans;
    ```
    - Passed 4 cases. Rest TLE
- **A simple optimization.**
    - Since its best for the `jth` wall to be as far as possible start the inner loop from end towards the `ith` wall.
    - Also since the height of water column is `min(wall[i], wall[j])` we don't need to search any more for `ith` wall if we find a `j` s.t `wall[j] >= wall[i]`.
    ```cpp
    int ans = INT_MIN;
    for(int i=0;i<n;i++)
    {
        for(int j=n-1;j>=i+1;j--)
        {
            int volume = min(wall[i], wall[j]) * (j-i);
            if(volume > ans)
                ans = volume;
            if(wall[j] >= wall[i])
                break;
        }
    }
    return ans;
    ```
    - All test cases passed. :yum:

**2. Ladders**

- Looked like a dp problem. Solved it using O(n^2) dp.
    ```cpp
    int dp[n+1]; // All initialized to INT_MAX
    dp[0] = 0; // no ladders to reach level 0
    for(int i=1; i<n; i++)
        for(int j=1;j<=ladder[i]; j++)
            dp[i+j] = min(dp[i+j], dp[i] + 1);
    return dp[n];
    ```
    - Passed all but 1 Test Case (TLE).
- Wrote a BFS code too. Same results though.
- Apparently a simple optimization to the dp problem would have solved the TLE case. 
    + No need to update the floors that were reachable from the previous floor.
    ```cpp
    int dp[n+1]; // All initialized to INT_MAX
    dp[0] = 0; // no ladders to reach level 0
    for(int i=1; i<n; i++)
        for(int j=(ladder[i-1]-1);j<=ladder[i]; j++)
            dp[i+j] = min(dp[i+j], dp[i] + 1);
    return dp[n];
    ```

#### Note: Sometimes the little stuff makes a big difference. :smile: