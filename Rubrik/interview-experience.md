## Rubrik

Day 1: Slot 1

### Round 1

- Coding Round
- The interviewer spent a few minutes explaining what the company actually does and its technological stack.

#### Problem: Find the integer root of a number.

- Asked what language do I prefer to code in. I said C++.
- The interviewer sat beside me and asked me to write the code for the problem in C++ on his laptop (probably notepad).
- I started writing the code using binary search. Find a candidate s.t. `(candidate)`<sup>`2`</sup> `< n` 
- **Question: He pointed out that I was using floating point numbers and asked do I really need to use floating point numbers.**
    + I answered that since the question is to find the integer root we do not need to use floating point numbers.
    + Started modifying the code to use only integers.
-  **Question: Is it possible to find floating point root and then using it give the integer root**
    +  I answered Yes! We can simply return the floor of the decimal square root.
    +  **He said this might not be stable as there is always some precision loss in the way decimal numbers are stored.**
    +  **For e.g floating number 2 can be stored as 1.999999999999 and floor of which would give 1 as the integer square root of 4.**
- He gave a bunch of test cases and my code failed on one of them.
- I then modified my code to mimic `std::upper_bound`.
    ```cpp
    int sqrt(int n)
    {
        int l = 0;
        int h = n;
        while(l<=h)
        {
            long cand = l + (h-l)/2;
            if(cand * cand <= n)
                l = mid + 1;
            else
                h = mid - 1;
        }
        return l-1;
    }
    ```
- This was giving right answer for all the test cases he came up with. He didn't look convinced though. :confused: 

#### Problem: Find square root of a number upto epsilon precision.

- Started modifying the code. 
    + changed the condition to
    ```cpp
        if(abs((cand * cand) - n) <= eps)
    ```
    + **He pointed out that this condition is not what he asked for**
    + What I was doing: `abs(your_answer`<sup>`2`</sup>` - actual_answer`<sup>`2`</sup>`) < eps`.
    + What the Question demands: `abs(your_answer - actual_anser) < eps`
    + I then said that we can achieve the desired result by squaring what question asks and using that as the stopping condition.
- Took too much time in thinking about the while condition.
- The code:
    ```cpp
    double sqrt(double n, double eps)
    {
        double l = 0;
        double h = n;
        while(abs(l-h) <= eps)
        {
            double mid = l + (h-l)/2;
            if(abs(mid*mid - n) < eps)
                return mid;
            else if(mid*mid < n)
                l = mid;
            else
                r = mid;
        }
        return l;
    } 
    ```
- **At this point he pointed out that this code fails for the cases when n = 0.25 and asked can I explain why?**.
    + I then realized the assumption that there is an implicit assumption in the code that *square root of a number is smaller than the number itself.*.
    + This is why the code fails because this assumption is not true in the range [0, 1].
- **He then asked me to make a quick change that solves this problem**
    + All the changes that I proposed required me to introduce `if else` inside the binary search logic.
    + Couldn't figure out the quick change. :disappointed: 
- The quick change is to set `h = 1` whenever `n < 1`.


### Wasn't called for any subsequent rounds. 
