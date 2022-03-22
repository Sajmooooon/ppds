# PPDS 05
Fifth assignment from the PPDS course.

# Description
In this assignment we solved 2 problems. One task deals with the problem of smokers, where our task was to solve
agent not to wait for the resource allocation signaling. 
In the second task we solved the problem of savages, where we had to make all the savages start eating together at the beginning,
and if the pot was empty, one of them would wake up the cook, who would cook the food and the cook would put the portions in the pot. Then
the implementation of multiple cooks had to be resolved. When the savage finds that the pot is empty he wakes up all the cooks who together
cook. After it is cooked, just 1 cook tells the waiting savage that it is cooked.

# Implementation smokers
In the task of smokers, we have modified the code so that the agent does not wait for signal and the dealers keep supplying raw materials and the number of raw materials increases.
By implementing this assignment in this way, the problem is that the raw materials are constantly being delivered to the table and all 3 raw materials are on the table.
Then there is the problem of which smoker will continue, or it may happen that one smoker goes around and does not get to the next one as you can see in code below.
To avoid favouring one smoker over another, we would need to randomly select which of the available smokers would go. This will therefore prevent favouritism.

```
def pusher_match(shared):
    while True:
        shared.match.wait()
        shared.mutex.lock()
        if shared.isTobacco:
            shared.isTobacco -= 1
            shared.pusherPaper.signal()
        elif shared.isPaper:
            shared.isPaper -= 1
            shared.pusherTobacco.signal()
        else:
            shared.isMatch += 1
        shared.mutex.unlock()
```


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

# Pseudocode
```
FUNCTION init(servings):
    servings = servings
    count = 0
    mutex = Mutex()
    cmutext = Mutex()
    empty_pot = Semaphore(0)
    full_pot = Semaphore(0)

    b1 = SimpleBarrier(number_savages)
    b2 = SimpleBarrier(number_savages)
    c1 = SimpleBarrier(number_cooks)
    c2 = SimpleBarrier(number_cooks)
ENDFUNCTION


FUNCTION eat(savage_id):
    PRINT('savage %2d: eating',savage_id)
    sleep(0.5 to 2 s)
ENDFUNCTION


FUNCTION savage(savage_id):
    sleep(0.01 to 1 s)
    WHILE True:
        b1.wait()
        b2.wait('savage %2d: before dinner',
                'savage %2d: we are all',savage_id)
        mutex.lock()
        PRINT('savage %2d: number of remaining portions %2d',savage_id,servings)
        IF servings is equal 0:
            PRINT('savage %2d: wake the cook',savage_id)
            empty_pot.signal(number_cooks)
            full_pot.wait()
        ENDIF
        PRINT('savage %2d: taking from pot',savage_id)
        servings = servings - 1
        mutex.unlock()
        eat(savage_id)
    ENDWHILE
ENDFUNCTION


FUNCTION cook(cook_id):
    WHILE True:
        empty_pot.wait()
        c1.wait()
        c2.wait()
        cmutext.lock()
        count = shared.coks + 1
        PRINT('cook %2d: cooking',cook_id)
        sleep(0.5 to 2 s)
        IF count is equal cooks:
            count = 0
            PRINT('cook %2d: servings -> pot',cook_id)
            servings = servings + number_servings
            full_pot.signal()
        ENDIF
        cmutext.unlock()
    ENDWHILE
ENDFUNCTION


FUNCTION main():
    shared = Shared(0)
    threads = []
    FOR savage_id=0 to number_savages-1:
        savages.append(Thread(savage, savage_id, shared))
    ENDFOR

    FOR cook_id=0 to number_cooks-1:
        savages.append(Thread(cook, cook_id, shared))
    ENDFOR

    FOR t=0 to threads.length-1:
        t.join()
    ENDFOR
ENDFUNCTION
```
