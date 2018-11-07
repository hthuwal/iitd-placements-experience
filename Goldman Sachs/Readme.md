## Goldman Sachs

- Designation: Analyst
- Place of Posting: Bengaluru
- CTC: 3150000 INR
- Gross: 21,00,000 INR

---

### Online Test

2 Sections CS and Quant & Analytics

- Platform HackerRank
- CS Section
    + 1 Programming Question
    + 4 CS MCQ
    + 2 Comprehensions with 2 MCQs each
        * Lambda Calculus
        * Hamiltonian Path
    + 60 Minutes
- Quant & Analytics
    + 6 MCQs
    + 2 Comprehensions  with 2 MCQs each
    + 60 Minutes
- Scoring +10/-2 for MCQ. +20 for coding Question.

##### Experience
- MCQ's were tough. Had done lambda calculus in the first semester but couldn't do the questions. :disappointed:
- Was able to do some CS MCQs. Quant & Analytics MCQ were tough.
- Liked the coding Question. Passed all test cases :smiley:
- [Screenshot of the coding Question.](coding-exam.pdf)
- Solution
  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  /*
   * Complete the 'minimum_steps' function below.
   *
   * The function is expected to return a LONG_INTEGER.
   * The function accepts LONG_INTEGER_ARRAY A as parameter.
   */

  long minimum_steps(vector<long> A) {
      int n = A.size();
      int hash[1000004]={0};

      // count how many times each element occurs
      for(int i=0;i<n;i++)
          hash[A[i]]++;


      // if an element i occurs x times
      // => 2^i occurs x times
      // => let k = log2(x), rem = x - 2^k
      // => 2^i occurs 2^k times and 2^i occurs rem times
      // => 2^(i+k) occurs 1 more time and 2^i occurs rem times
      // => hash[i+k] ++ and repeat
      for(int i=0;i<1000004; i++)
      {
          if(hash[i] != 0)
          {
              // increase 
              while(hash[i] > 1)
              {
                  int x = log2(hash[i]);
                  hash[i+x] ++;
                  hash[i] = hash[i] - pow(2, x);
              }
          }
      }
      int ans = 0;
      for(int i=0;i<1000004; i++)
          ans += hash[i];
      return ans;
  }

  ```

