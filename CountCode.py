'''
10)


 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1

'''

Answer:

l1=int(input())
l2=int(input())
l3=int(input())
h=int(input())
count=0
if(h<l1):
    count=count+1
if(h<l2):
    count=count+1
if(h<l3):
    count=count+1
print(count)

Output::
30
40
20
25
2
