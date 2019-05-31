# number-partition-algorithms
A set of algorithms for the [number partition problem](https://en.wikipedia.org/wiki/Partition_problem) (a.k.a. set partition problem) where a list of numbers is divided into equal-sum groups.

The number partition problem is known to be NP-complete. Generally, there're two variants of the problem: Two-way partition problem (i.e. divide the data into two groups), and multi-way partition problem (i.e. divide data into more than two groups).

This project presents a set of heuristics and efficient approximation algorithms to solve the above problems. These algorithms are implemented in Python language.

# Usage
Executing these algorithms is easy:
> python partition.py datafile num_groups
Here `datafile` is a plain text file containing the list of data to be divided, `num_groups` is the number of groups and its minimum value is 2.

This command will run all the algorithms sequentially on the same data set. Specifically, there're following algorithms:
## Greedy Partition
This algorithm uses a simple strategy. Specifically, it greedily assigns the largest unassigned number to the group with smallest sum.

## KK(Karmarkar-Karp)
This algorithm consists of two phases. The first phase takes the two largest numbers from the input and replaces them by their difference; this is repeated until only one number remains. The replacement represents the decision to put the two numbers in different sets, without immediately deciding which one is in which set. At the end of phase one, the single remaining number is the difference of the two subset sums. The second phase reconstructs the actual solution. 

We provided a new implementation for this algorithm. We use Python's [heapq](https://docs.python.org/2/library/heapq.html) library to efficiently select largest number from a list, and Python's [LifoQueue](https://docs.python.org/2/library/queue.html) library to save mediate results and reconstruct the actual partition solution.

## DP(Dynamic Programming)
This is an optimal algorithm, suitable for small scale scenarios. The description of this algorithm can be found [here](https://en.wikipedia.org/wiki/Partition_problem).

# Support
This project is developed and maintained by [slxiao](https://github.com/slxiao). Refer to [gitlab issues](https://github.com/slxiao/number-partition-algorithms/issues) if you meet any bugs or need feature enhancements.
