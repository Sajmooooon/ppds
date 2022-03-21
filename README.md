# PPDS 05
Fifth assignment from the PPDS course.

# Description
In this assignment we solved 2 problems. One task deals with the problem of smokers, where our task was to solve
agent not to wait for the resource allocation signaling. 
In the second task we solved the problem of savages, where we had to make all the savages start eating together at the beginning,
and if the pot was empty, one of them would wake up the cook, who would cook the food and the cook would put the portions in the pot. Then
the implementation of multiple cooks had to be resolved. When the savage finds that the pot is empty he wakes up all the cooks who together
cook. After it is cooked, just 1 cook tells the waiting savage that it is cooked.

# Implementation savages
This task is an extension of the Producers and Consumers problem of tracking stock status. In the first part it was necessary to
all the savages to wait for each other before dinner and go to eat at once, we solved this problem using 2 simple barriers.
In the second problem, it was necessary to solve that all the cooks cooked together and only one of them announced the finished dinner to the waiting
to the savage. We solved this second problem similarly to the first problem, where we used 2 simple barriers at the beginning to make all the cooks
to wait for each other and then start cooking. After cooking only 1 of them announced that it was cooked.

When solving for the savages, we simulated sleep using sleep() then in an infinite loop at the beginning they all waited for each other
savages, and then we used a lock to sequentially list how many servings were left, or if the number of servings was currently 0,
then the given savage signals all cooks using Semaphore to wake up, and then we simulated waiting for servings using Semaphore wait.
When the cooks are finished, the savages scoop their food and the number of servings from the shared space is taken and the lock is unlocked. Eventually they will eat which is simulated by sleep().

The cooks' solution runs in an infinite while cycle, then waits using Semaphore wait() to signal, from
savage when the pot is empty. Then when they get the signal they wait for each other, we provided this using
2 simple barriers as with the savages, and then they each cook some part of the meal, which is simulated by sleep(). When everyone has finished cooking,
the number of portions is incremented and the last cook, then signals savage with the Semaphore that it's done.
