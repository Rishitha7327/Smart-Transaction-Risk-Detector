# Smart Transaction Risk Detector – README

## Algorithm Explanation
The code accepts transaction values as input from the user and determines the type of each transaction as either Normal, Large, High Risk, or Invalid by using a for loop with if-else conditions implemented as a dictionary. It uses list comprehension to eliminate Invalid values before calculating the total manually by using a for loop. The three patterns used are Frequent, Large Spending, and Suspicious to determine the level of risk.

## Test Cases

**Test 1 – High Risk**
Input values – 200, 1500, 3000, 450, 2500, 100, 3500
Output – High Risk
Explanation – High Risk as three values are High Risk, total > 5000, and count > 5.

**Test 2 – Low Risk**
Input values – 50, 120, 300, 480
Output – Low Risk
Explanation – Low Risk as all values are Normal with no patterns.

## Logic Decisions
- Invalid values (≤ 0) are ignored while calculating the total to avoid incorrect results.
- The Suspicious pattern by itself will result in High Risk as repeated High Risk values are the strongest indicators of fraud.

## Programming Elements Used
- List, For Loop, If-Else, List Comprehension, Dictionary, Tuple
*Name: [Your Name] | Roll No: [XXXX]*
