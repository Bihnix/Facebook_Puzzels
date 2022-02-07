

# All Wrong

There's a multiple-choice test with N questions, numbered from 1 to N. Each question has 2 answer options, labelled A and B. You know that the correct answer for the ith question is the ith character in the string C, which is either "A" or "B", but you want to get a score of 0 on this test by answering every question incorrectly.
Your task is to implement the function getWrongAnswers(N, C) which returns a string with N characters, the ith of which is the answer you should give for question i in order to get it wrong (either "A" or "B").

![image](https://user-images.githubusercontent.com/48855903/152843513-ef709c29-0f19-4a19-8187-e2c3c6629b8c.png)

# Sample Explanation
In the first case the correct answers to the 33 questions are A, B, and A, in that order. Therefore, in order to get them all wrong, the 33 answers you should give are B, A, and B, in that order.
In the second case the correct answers are all B, so you should answer each question with A.
