# PPDS 02
Second assignment from the PPDS course.


## Description
In this assignment, we were concerned with solving 3 problems using a semaphore and an event.
In the first problem we created a simple barrier.
In the second problem we solved a reusable barrier and in the third problem we solved a fibonacci.
The implementation of the simple barrier is located at [simple barrier](https://github.com/Sajmooooon/ppds/tree/02/simpleBarrier) with the reusable barrier located at [reusable barrier](https://github.com/Sajmooooon/ppds/tree/02/barrier)
folder and the fibonacci implementation is located in the fibonacci folder.


## ADT Simple Barrier
In this task, we created a simple barrier using a semaphore, where the ids of the threads before and after the barrier were printed out.
The barrier is provided by the ``wait()`` function in the ``SimpleBarrier``  class. In this function, the
thread is locked, then the counter is incremented, which is then
checks that its value is the same as the thread count. If so, the counter is reset. Next 
all threads are released, the thread is unlocked, and finally the thread is waited for to catch up if the condition has been met,
then all waiting threads are released.


## Reusable Barrier
In this task we dealt with a reusable barrier. At the beginning we implemented the SimpleBarrier class and 
in it we defined the wait function.
In the first example in the ``semaphore.py`` script, we used the same function as in the ``Simple Barrier`` section.
Unlike the Simple Barrier implementation, here we have used 2 barriers that alternate 
in an infinite loop.

In the second example in the ``event.py`` script, we used Event instead of Semaphore. In this example in the function 
``wait()``
we first used ``event.clear()`` which makes sure that the event is cleared so that it can be used again. 
In the initial implementation, we placed ``event.clear()`` at the end of the ``wait()`` function, which caused
if we added ``sleep()`` between ``mutex.unlock()`` and ``event.wait()``, the last thread, 
that met the condition would come later on ``event.wait()`` 
and those threads that were waiting on ``event.wait()``
would have executed ``event.clear()`` and the last thread would thus be stuck on ``event.wait()``.
Further, as in the previous example, if the condition that the counter has the same value as the number of threads is met, 
then all pending threads will be released,
but in this case using ``event.set()`` and resetting the counter. 
Next, as in the previous example, the thread is unlocked and waits for the other threads to catch up if the condition has been met,
then all waiting threads are released.

