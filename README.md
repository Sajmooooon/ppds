# PPDS 01

First assignment from the PPDS course.


## Description

In this project, we address the problem using 2 threads, 
that have a shared field and a shared field index. The index is incrementally increased, 
until it exceeds the length of the field. Finally, it is counted how many elements of the field have the given value.

In this case, however, there may be a problem where both threads simultaneously increment
the index value and there is a problem that at least 1 thread can execute both instructions in the while
cycle at the same time. Thus add 1 to the array at the given index and increment the index value at the same time.
To fix this problem, we used Mutex lock. 

We used python with version 3.8.0 to perform the implementation.


## Implementation

We made 2 implementations, where each time We placed a lock in a different part of the code. 
The implementations are numbered from 1-2 and are in separate folders. 
Implementation 1 is located in the var1 folder and implementation 2 in var2 folder.

We tested both implementations with array sizes of 1000 to 1000000. Implementation 1 worked without problems,
but in implementation 2 we had a problem, as we had a condition defined in the while at the beginning and not in the loop body.
Thus, even when the while loop's interior was locked in one thread, the second thread passed the condition and then, 
when one thread incremented the counter value and that value was already the same as the size of the array, then 
after unlocking, the waiting thread was able to execute the inside of the loop. Therefore, we modified the code to make the inside
while loop to check the condition first, and thus we avoided this problem.


### Implementation 1

In the first implementation, we used a lock in the ``do_count(shared)`` function, 
where we locked the entire while loop and then unlocked it. 
Thus, it is only executed on 1 thread, because the second one waits for the first one to finish and when it finishes
the shared counter value already has the same value as the length of the array and thus the second thread
is terminated on the condition in the loop.


### Implementation 2

In the second implementation, we placed the lock inside the while loop, with the execution
threads alternated. The first thread locks the inside of the while loop, while the second thread 
waits, the first one checks the condition, and if it is not met, it executes the next instructions and 
finally unlocks. Then in the second thread it does the same and repeats this with the threads,
until the condition is met and then the unlock would occur to avoid deadlock and end the loop.




