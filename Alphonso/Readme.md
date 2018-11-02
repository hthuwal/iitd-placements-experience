## Alphonso

- Designation: Technologist
- Place of Posting: Bangalore
- CTC: 3000000 INR Per Annum
- Gross: 3000000 INR Per Annum 

---

### Online Test

- Platform: HackerRank
- 25-26 MCQs: OS, DBMS, Python, Unix, etc..
- 1 Coding Question
- 2 Pseudo Codes

#### Coding Question

+ Given a set of jobs
+ Time taken by each job.
+ Profit associated with each job.
+ Total time that you have.
+ Maximize the profit.
 
Spend a lot of time trying to figure out what to do.

- Two 2D DP's.
- 1D DP.
- Greedy
- Nothing worked. :cry:

Didn't realize it was simply a 0/1 knapsack problem. :angry:

#### Pseudo Code problems

##### 1. TCP Sender Receiver

- Files are being sent over 5 parallel TCP connections from sender to receiver.
- Files are splitted into 512 Bytes segments.
- Chunks from multiple files can be sent paralley.
- Assume no packet loss, no connection break.
- The sender receives the segments and merges them to create the file.

Write the pseudo code for the sender.

Was frustrated after not being able to do the coding question. Did something. Wrote a few python function. Probably incorrect. :expressionless:

##### 2. Pattern Lock


:large_blue_circle::large_blue_circle::large_blue_circle:  

:large_blue_circle::large_blue_circle::large_blue_circle:  

:large_blue_circle::large_blue_circle::large_blue_circle:  

Write pseudo code for two functions:

- Store Pattern Lock.
    + My Approach
        + Store a pattern as a sequence of integers 0, 1, 2, 4, 5, 6, 7, 8, 9
        + conversion of dot(x, y) -> 3*x + y
- Validate Pattern Lock
    + My Apprach
        * if dotA is pressed after dotB check:
            - dotA has not been touched already (use a map/dict/set).
            - dotA is reachable from dotB. That is it is in its immediate vicinity.

