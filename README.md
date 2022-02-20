# PPDS 01
First assignment from the PPDS course.

##Description
In this project, we address the problem using 2 threads, 
that have a shared field and a shared field index. The index is incrementally increased, 
until it exceeds the length of the field. Finally, it is counted how many elements of the field have the given value.

In this case, however, there may be a problem where both threads simultaneously increment
the index value and there is a problem that at least 1 thread can execute both instructions in the while
cycle at the same time. Thus add 1 to the array at the given index and increment the index value at the same time.
To fix this problem, we used Mutex lock. 

We used python with version 3.8.0 to perform the implementation.





