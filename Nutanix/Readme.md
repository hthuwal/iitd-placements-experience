## Nutanix

- Designation: Member of Technical Staff
- Place of Posting: Bangalore
- CTC: 39LPA, Gross: 20LPA (B.Tech), 21LPA (M.Tech)

---

### Coding Round

- Platform: HackerRank
- Duration: 1 hour 30 minutes
- Number of Questions: 2

Screenshots of Questions are present in the [coding-exam.pdf](coding-exam.pdf)

#### How I approached it?
Read the questions from the pdf before reading ahead.

- Question *1* seemed tough as compared to the *2*nd One.
- Second one seemed straight forward, build the tree from inorder and post order traversal and then check for conditions. So started doing it.
- Estimated it would take *1* hour max to do this, will still have at least *30* minutes to attempt the 1st question.

#### What went wrong?

- Started writing code without thinking of other approaches. After writing *30%* code to build the tree, realized there exist some pattern in the inorder and post order traversals. So don't need to create the tree.
- Tried finding the pattern for some cases. Panicked that I have wasted some time. Found wrong patterns. More Panick !!. Took more than *1* hour *10* minutes to what could have been done in *30-40* minutes.
- After that all test cases went wrong. Was unable to find the bug untill only 3 minutes were remaining.

#### What went right?

- The fact that I chose to do the pattern approach **using python instead of C++**.
- Found bug replaced string of indics "145123" to [1, 45, 12, 3]. Everything worked because of the uniform api of python. Everything that was intended for strings worked on lists as well. 
- This allowed one swift change from `string` to `string.split()` to get correct answer on all the test cases.
- Wouldn't have been able to do this in the remainig 2-3 minutes if I had used C++.

#### Takeaway

- Give sometime into thinking the approach before starting coding.
- Choice of Language if available could be a game changer. Choose wisely based on what your algorithm is trying to do.
