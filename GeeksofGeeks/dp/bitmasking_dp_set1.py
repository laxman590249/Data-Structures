"""
There are 100 different types of caps each having a unique id from 1 to 100. Also, there are ‘n’ persons each having a
collection of a variable number of caps. One day all of these persons decide to go in a party wearing a cap but to look
unique they decided that none of them will wear the same type of cap. So, count the total number of arrangements or ways
 such that none of them is wearing the same type of cap.

Constraints: 1 <= n <= 10 Example:

The first line contains the value of n, next n lines contain collections
of all the n persons.
Input:
3
5 100 1     // Collection of the first person.
2           // Collection of the second person.
5 100       // Collection of the third person.

Output:
4
Explanation: All valid possible ways are (5, 2, 100),  (100, 2, 5),
            (1, 2, 5) and  (1, 2, 100)
"""

persons = 3
collections = ['5 100 1', '2', '5 100']
unique_cap = set()

for collection in collections:
    cap = collection.split(' ')
    for u in cap:
        unique_cap.add(u)

unique_caps_count = len(unique_cap)
print(unique_caps_count)

total_ways = pow(2, unique_caps_count)
print(total_ways)



