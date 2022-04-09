# PPDS 06
Seventh assignment from the PPDS course.

# Description
In this assignment, we implemented a scheduler.

# Implementation
At the beginning, we created a simple Task class that contains its ID and the coroutine that will be executed. It contains one method that
executes that coroutine. We then created a Scheduler class whose role is to schedule coroutines. The Scheduler class contains a list of tasks that
contains the Task objects. The Scheduler class has 2 methods - add_task and schedule. 
The add_task is used to create a new Task object and then to add
the created object to the list of tasks. 
The schedule method is used for coroutine scheduling. It first sorts the Tasks by their ID from smallest to largest. This ensures that
coroutines will be executed with priority, i.e., based on ID, they will be executed in order from smallest to largest. We will then traverse the list of tasks in the while loop,
until it's empty. The loop will first remove the first Task in the list - that is, the Task with the smallest ID and try to execute it. The coroutine of the selected Task will run if it has not finished its iteration
and then adds the Task to the end of the list and continues in this way until the list contains no Task. Finally, we created 3 simple functions - coroutines,
which wrote a message in the for loop and then executed yield.


