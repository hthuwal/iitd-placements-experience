## Sprinklr

- Designation: 
    + Platform Software Engineer
        * CTC: 35 LPA
    + Product Engineer
        * CTC: 25 LPA
- Place of Posting: Gurgaon
- CTC breakup not known.

---

### Online Round

- Platform: HackerEarth
- Druation: 2 Hours
- Multiple MCQs 
- 4 Coding Questions


#### Coding Questions

##### 1. Shortest path to exit a grid.

Given a matrix where 0- blank, 1-plant, 2-source. Find the shortest distance from source to any of the boundary edges. You can traverse through 0 in any of the four directions(left, right, up, down).

- Simple BFS Worked.
- Passed all test cases. :smile:

##### 2. Node from which maximum elements can be reached.

There are N nodes. Each node has exactly 1 directed edge. You have to return the node from which maximum elements can be traversed.

For eg : `N=3 and A[]={3,3,1}`

So there is a directed edge from node 1 to node 3, from node 2 to node 3 and from node 3 to node 1;

So if we start from node 2 we can traverse all the elements.

Output : Return 2

- Simple DFS from every node count number of nodes that are reachable.
- Passed all test cases. :smile:

##### 3. Count submatrices

Find the count of all the submatrices of a matrix of size `m x n`, such that the sum of the elements of the submatrices is divisible by given number P.

- Wrote a O(n^3) space and time DP. 
- Was exceeding memory limit. Few test cases passed.
- Didn't know about [matrix prefix sum.](https://www.geeksforgeeks.org/prefix-sum-2d-array/) :disappointed:

##### 4. Min Cost

Given 3 fruit f1, f2 and f3. Energy per unit of these three fruits is 2, 3 and 5 respectively. Given cnt1, cnt2, cnt3 amount of these fruits and cost per unit of fruits f1, f2 and f3 is cost1, cost2 and cost3. Find the minimum cost such that the total energy gained after buying these fruits is S.

Example: count:[2, 2, 1], cost [5, 5, 20]  & S = 10   
Ans: 20 if you buy 2 f1 and 2 f2.

- Tried converting the problem into a bounded knapsack. Couldn't do it memory issues. :disappointed:
- Got to know a trick was involved after the exam:
    + 2a + 3b + 5c = S
    + Find all possible values of a, b and c O(n<sub>2</sub>).
        * Assume a and b and then calculate c.
    + return the set of values that give minimum cost.