## Harness

- Designation: Software Engineer
- Place of Posting: Bangalore
- CTC: 2710000 INR Per Annum
- Gross: 2310000 INR Per Annum

---

### Online Exam (60 Minutes)

- 10 MCQs: Basic Algorithm, Data Structure, Oops, C program outputs, Java etc.
- 2 Coding Question
- Platform: HackerRank

##### 1. Mobile Numpad

|1 (space)|2 (abc)|3 (def)|
|-------|-------|-------|
|**4 (ghi)**|**5 (jkl)**|**6 (mnop)**|
|**7 (qrs)**|**8 (tuv)**|**9 (wxyz)**|   

- Given a Numpad.  
- And a string `sentence` say **"har x"**  
- Find the number of different decoding possible for the keypress sequence of the `sentence`.
- Keypress for **"harf fb"** is **44277199**
- Possible decodes of **44277199** are
    + **ggaqq ww, ggaqq x, ggar ww, ggar x, haqq ww, haqq x, har ww, har x**
    + `return 8`

- Easy DP question. Still wasn't able to do it. :disappointed:
- Didn't had enough time left to be able to code it.

##### 2. Distinct Substrings

Count the number of distinct substring of a string. Length of string was O(10<sup>5</sup>)

- Coded Brute Force.
- Took way more time than what brute force should have taken.
- Couldn't remember the syntax of `string.substr`. Wasted a lot of time just to figure out its syntax. :disappointed:
- 5/10 test cases.
- Implemented Rolling Hash. 6/10 test cases passed. :unamused:
- **Should Have realized that O(n<sup>2</sup>) 10<sup>10</sup> won't work. No point in doing rolling hash.**