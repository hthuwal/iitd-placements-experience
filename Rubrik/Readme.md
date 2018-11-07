## Rubrik

- Designation: Member Technical Staff
- Location: US/Bengaluru
- CTC: 3225000 INR Per Annum
- Basic Element: 2750000 INR Per Annum (Bachelors)
- Basic Element: 2850000 INR Per Annum (Masters)

---

### Coding Round

- Platform: HackerRank
- Duration: 2 Hours
- 3 Questions

##### 1. Infinite Modification

Given an Empty Array A[]. You perfrom infinite modification to it as follows

You add number `x` to the array if it there exist no subset of A with the sum of its elements = x.

You'll be given a number `n` as query. You are supposed to print the n'th element % M in the array. `1 <= n <= 10^5`. `M = 10^9 + 7`.

- Initially thought it might involve finding subset with `sum = x` using O(n<sup>2</sup>) DP atleast `n` times.
- But once you simulate the modification steps 2 to 3 times. The arrays simply turns to be an array of powers of 2.
- A = [ 1, 2, 4, 8, 16 .....]
- For Query `i` you just need to reutrn 2<sup>i</sup> % M.
- Implemented a modulo exponentiation function. 
- All test cases passed. :smile:

##### 2. Find the Lighter Coin

Given **N** identical coins but one of them weighs lesser than the all others. Given a physical balance which can weigh two sets of coins at a time. What is the minimum number of times one has to use the balance to find the lighter coin.

- Had done this question as puzzle during B.Tech Placements.
- Optimum strategy is to divid the coins in to three sets of size `n/3`, `n/3`, `n - 2n/3` (A, B, C)
- Weight any two say A and B. If they are equal lighter coin is in C.
- else if A is lighter than B, A contains the lighter coin.
- else B contains the lighter coin.
- Simple recursion works.
  ```cpp
  long long int recurse(long long int n)
  {
    if(n <= 1)
        return 0;
    else if(n == 2 || n==3)
        return 1;
    else
        return 1 + max(recurse(n/3), recurse( n - (2*(n/3) )));
  }
  ```
- `1 <= n <= 10^18`
- Didn't notice the huge input range. Was reading integers. Costed me 5-8 minutes of debugging.
- All test cases passed. :smile:

##### 3. Copy on Write (COW)

Implement a file system with followin commands.

- **CREATE** `<file_name>`: Create a empty file with name `<file_name>`.
- **READ** `<file_name>` `<starting_position>` `<end_position>`: Read the file from `<starting_position>` to `<end_position>`.
- **SIZE** `<file_name>`: Print the size of the file with name `<file_name>`.
- **EDIT** `<file_1>` `<file_2>` `<start>` `<end>` `<size>` `<list of numbers>`: Create `file1` with contents same as `file2` except the contents between `<start>` and `<end>` should be replaced with the `<list of numbers>`.
- **EXIT**

Implementation:
```cpp
unordered_map<string, vector<int> >;
// string -> file_name
// vector<int> -> file data
``` 

- Passed all test cases. :smile: