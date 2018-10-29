## Flipkart

- Designation
    + Data Scientist
        * CTC: 30,49,000 LPA
        * Basic: 22,00,000 LPA
    + SDE 1
        * CTC: 23,84,200 LPA
        * Basic: 16,00,000 LPA
- Place of Posting: Bangalore

---

### Coding Test

- Platform: [HackerRank](https://www.hackerrank.com/)
- Duration: 90 Minutes
- 3 Coding Questions

#### [**1. Minimum steps to reach the target by a knight**](https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/)

Given a square chessboard of N x N size, the position of Knight and position of a target is given. We need to find out minimum steps a Knight will take to reach the target position.

**My Approach**  

- A simple bfs from starting node.
- Coded this in the last 12 minutes.
- All test cases passed :smile:
- Even though I knew how to do it, should have started a bit earlier than last 12 minutes. :joy:

#### **2. Time Conversion**

Given date in format 22nd July 1995 convert into format 1995-07-22.

**My Approach**

- Plain string manipulation
- Python **zindabad**. :v:
- Did it in the first 10 minutes.
- All test cases passed.

#### **3. Maximal nodes product in Maximal Group**

__Essence of the question__

- Given 3 lists of size n.   
    - friendsfrom
    - frinedsto
    - candies
- friendsfrom[i] and friendsto[i] like the candy[i]. This relation is transitive.
- Liking a candy -> creates multiple group of friends.
- Return the product of two maximum nodes in the largest group.
- A single nodes/friend can be in multiple groups. 

**My Approach**

- Disjoint Set Union Find for each candy.
- Return the maximal product across all groups across all candies.
    + 8 Test cases passed.
- Found the bug.
    + Need to find the largest group first across all candies.
    + Among the largest group find the largest product.
        * Should read the question more thoroughly. :expressionless:
    + 14/15 test cases passed.
- Debugged for almost an hour couldn't find the stupid bug.