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


### Implementation 1

In the first implementation, we used a lock in the ``do_count(shared)`` function, 
where we locked the entire while loop and then unlocked it. Thus, it was only done on 1 thread because the other thread waited for the first one to finish and when it finished
the shared counter value already had the same value as the length of the field and thus the second thread
was terminated on the condition in the loop.


### Implementation 2

In the second implementation, we placed the lock inside the while loop, with the execution
threads alternated. The first thread locked the inside of the while loop, while the second thread 
waited, the first one checked the condition, and if it was not met, it executed the next instructions and 
finally unlocked.Then in the second thread it was the same and this was repeated with the threads, 
until the condition was met and then the unlock would occur to avoid deadlock and end the loop.




