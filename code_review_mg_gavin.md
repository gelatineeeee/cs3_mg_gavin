### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: 9-Magnesium 	                                                      Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name: \#21- Gavin, \#22- Isagunde                                      Date:**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

Implementation 2 (Binary Search) is faster when the list is very large because it cuts the search space in half with every iteration. It makes it more efficient than checking the elements one by one.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list?~~ | ~~How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list?~~ |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

Implementation 1 is easier to understand at first glance because it has very simple logic, uses concise code, and follows a straightforward step-by-step search process without extra variables.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process?~~ | ~~How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process?~~ |

### 

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

Implementation 1 would be easier to update because its simple loop structure makes it less prone to logical errors or breaking when changing what happens when a target is found.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating?~~ | Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?

Implementation 1 is easier to test because it has fewer conditions to check and a very straightforward path to verify across different inputs.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear?~~ | ~~Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear?~~ |

### 

### 

### 

### 

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from user?

The algorithm should check if the list is empty, verify that inputs are valid data types, handle unusual or missing values safely, and ensure the list is properly sorted before running Binary Search.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search? | Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search? |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and 

I would choose Implementation 2 (Binary Search) for this problem because the input list is large and already sorted, providing superior efficiency. Implementation 1 (Linear Search) would be more suitable if the list were unsorted, very small, or continuously changing where sorting overhead is not worth it. 