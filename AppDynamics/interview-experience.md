## AppDynamics

Day1: Slot 2

### Round 1

- Coding Round
- Introduce Yourself and your work.
    + Gave a brief overview of my resume.

#### Problem: Write a program to read a string and print its reverse.

- Used STL.
    ```cpp
    #include<bits/stdc++.h>
    using namespace std;
    int main()
    {
        string str;
        cin>>str;
        cout<<string(rbegin(str), rend(str));
    }
    ```
- **Don't use STL**
    ```cpp
    #include<bits/stdc++.h>
    using namespace std;
    int main()
    {
        string str;
        cin>>str;
        for(int i=str.length()-1;i>=0;i--)
            cout<<str[i];
    }
    ```
    + **What is the maximum length of the string this code will work on?**
        * I gave an estimate of how long string can be stored (based on my experience).
        * The interviewer pointed out that since an integer is being used to index each element. The maximum length of the string on which this code will work is of O(INT_MAX).
- **Where is the string stored?**
    + My first answer was on stack.
    + But later I realized that since we don't know what the size of the string. It cannot be stored on stack.
    + So the string must be allocated memory dynamically on the heap.
- **What happens when you do `cin>>str`. or if you had to implement the string class on which the above code works. How would you do it?**
    + `char * ptr`: 
        * stored on stack.
        * will point to the actual memory on heap. 
    + Will have to create a function corresponding to `operator>>` that takes an input stream.
        * This function will keep reading character by character from this stream and update the string. Untill the delimeter is reached.
    + **What is the delimeter?**
        * cin>>str (where str is of class string) will read untill we encounter a space. So space must be the delimeter.
        * He didn't look convinced.
        * So I explained that I've faced this issue and if I want to read a string (that might contain spaces) upto new line character, I had to use getline function.
        * For e.g. if the input is `App Dynamics`
            ```cpp
            cin>>str; // str = "App";
            getline(cin, str); // str = "App Dynamics"
            ```

#### Problem: Implement Dijsktra's Algorithm

- I Started with basic assuemptions for Dijsktra's Algorithm. Like no negative edge weights.
- Briefly Explained the algorithm.
- Explained that I can use both c++ set and priority_queue to implement the heap required in the algorithm.
    + Priority Queue: Internally implemented as heap.
    + Set: BST
- Continued to explain the code as I was writing it down.

### Problem: Linked List

- Write code for
    - Union of LL
    - Intersection of LL

### Random Problem I dont remember

- Wrote a recursive code.
- Then a DP code (O(n^2)).
- The interviewer suggested that O(nlog(n)) is also possible but I couldn't figure it out.