"""
1. Due to limited time, here the program is hard-coded;
2. It work as described in the specification;
3. Design:
		a. calculate the union of include_list and exclude_list:
			a1. sort the list, first sort by the first element, then by the second element;
			a2. use every list in the big list to compare with the other lists, 
				if these two has intersection, calculate the union of these two and mark this one as completed;
				if there is no intersection, break
			a3. loop until every list is marked as completed;
		b. calculate the difference of include and exclude:
			b1. function: given A:[a,b] and B:[c,d], calculate the A-B
			b2: use every list in exclude union, calculate the diff between each list in include union, 
				after iterating all list in include union, a new include union is created. 
				Then use the next list in exclude union to calculate;
4. Code:
		Easy to read.
5. Time Complexity:
		In step a: 
			Worst: O(n^2)
			Best: O(n)
		In step b:
			Average: O(n^2)
"""

from union import get_union
from diff import get_diff

include_list = [
    [10, 15],
    [1, 10],
    [20, 30],
    [10,25],
    [1,10],
    [30,58],
    [],
    [11,15],
    [60,70],
    [75,80],
    [179,200],
    [75,100],
    [200,200],
    [300,300]
]
exclude_list = [
    [95, 205],
    [65, 65],
    [],
    [50,57],
    [250,300]
]

union_of_include = get_union(include_list)
union_of_exclude = get_union(exclude_list)
result = get_diff(union_of_include, union_of_exclude)
print "the result is \n" , result 
