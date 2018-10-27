## Indeed

- Designation: Software Engineer
- Place of Posting: Hyderabad
- CTC: 2300000 INR Per Annum
- Base Salary: 1800000 INR Per Annum

---

### Online Round

- Platform: HackerRank
- Time: 90 Minutes
- 3 Coding Questions
- Was able to do 2/3 Questions.

1. Given a **nxn** square matrix containing integer values. Find the value of largest k ( size of a smaller sub square) such that all subsquares of that size has **sum < R**.  

    - Had no idea how to solve it. Just skipped it after reading it.
    - Proposed Solution: 
        + Use [dp to store prefix sum](https://www.geeksforgeeks.org/prefix-sum-2d-array/) **(O(n<sup>2</sup>)).**
        + Then use binary search on K. **O(n<sup>2</sup> log(k))**

2. Given a array, you have to increment the values such that all the elements become unique. Find the smallest sum you can get by incrementing the numbers.  
Eg: arr [ ] = {1,2,2,3,4}. You can increment the value of 2 to 5, final arr is {1,2,3,4,5} and the output will be sum of the final array = 15    
    - Found it easy on the first read. Realized it is a **Greedy Problem**
    - Create a hash of size = 2*max value of the numbers in array. Initialize it with all zeros.  
       ```cpp
       int hash[2*MAX_ELEMENT] = {0};
       ```
    - Update the number of times each element occurs in the array.  
       ```cpp
       for(int i=0;i<n;i++) hash[arr[i]]++;
       ```
    - If a number occurs mor than once change its every instance except to the next number  
       ```cpp
       for(int i=0;i<MAX_SIZ;i++)
       {
           if(hash[i] > 1)
           {
                hash[i+1] = (hash[i]-1);
                hash[i] = 0
           }
       }
       ```
    - Then the minimum cost is the ths sum of all the i's if hash[i] = 1; 
    - All test cases passed. :smile:   

3. A magical sub-sequence of a string S is a sub-sequence of S that contains all five vowels in order. Find the length of largest magical sub-sequence of a string S.  
For example, if ``S = aeeiooua``, then aeiou and aeeioou are magical sub-sequences but aeio and aeeioua are not.
    - **Easy Dynamic Programming Problem.**
    - `dp[n][5]`. `dp[i][j]` denontes length of longest subsequence ending at `vowel[j]` in the `S[0:i]`
    - Initialize dp matrix with all zeroes
    ```cpp

        if(a[0] == 'a')
            dp[0][0] = 1;   

        for(int i=1;i<n;i++)
        {
            for(int j=0;j<5;j++)
            {
                if(j==0) // if ending vowel should be 'a'
                    if(a[i] == vowels[j]) //current letter is 'a'
                        dp[i][j] = dp[i-1][j] + 1; // take it
                    else
                        dp[i][j] = dp[i-1][j]; 
                else
                    if(a[i] == vowels[j])
                    {
                        dp[i][j] = dp[i-1][j];
                        if(dp[i-1][j-1] != 0)
                            dp[i][j] = max(dp[i][j], dp[i-1][j-1]);
                        dp[i][j] += 1;
                    }
                    else
                        dp[i][j] = dp[i-1][j];
            }
        }
        return dp[n-1][4];
    ```
    - All test cases passed :smile: