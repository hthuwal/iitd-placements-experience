## Uber

- Designation: Software Engineer
- Place of Posting: Bangalore or Hyderabad
- CTC: 3600139 INR Per Annum, Basic: Base 1800000

### Coding Round

- Platform: HackerRank
- Duration: 1 hour 30 minutes
- Number of Questions: 3

Screenshots of Questions are present in the [coding-exam.pdf](coding-exam.pdf)

--- 

### Experience

**1. Custom Sorted Array**

- Initially thought it was [this](https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/).
- Then realized it is much simpler.
- Basically count the number of even integers say **k**.
- Then minimum number of swaps is = number of odd integers in range [0:k]
- All test case passed.
- Took around 25 minutes.
 
**2. Game Problem**

- If game ended before tie. (A, B)
    + (25, Y): This implies Last round one by A. 
        * Find Number of ways to get to (24, Y)
    + (X, 25)
        * Find Number of ways to get to (X, 24)
    + `ways(i, j) = ways(i-1, j) + ways(i, j-1)`
- If game tied at 24:24 and after that ended at (X, X-2) or (Y-2, Y)
    + after 24:24 -> they must reach 25:25 and so on
    + only 2 ways to reach from i:i to j:j (branching of two at every level)
    + so number of ways to reach (X-2, X-2) from (24, 24) is the number of edges in binary tree of height X-2-24. 
        + ans1 = `2`<sup>`X-2-24+1`</sup>`- 2`
    + Answer: ways(24) + ans1   
- Debugged till the end.
- `12/15 Test Case Passed.` :disappointed:

**3. Uber Shuttle Problem**

- Didn't had any time left to attempt.
- On reading the question in the beginning, didn't know how to d it.
- The Question was similar to the one I left in Nutanix.

---

#### Takeaway

- Always find the solution/approach to the problems that you weren't able to solve during a test. 
- If I had learned how to solve the nutanix Question, I might have been able to atleast attempt the third Question. :disappointed: