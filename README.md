# PPDS 08
Eighth assignment from the PPDS course.

# Description
The program is used to ping the specified URL addresses, if the specified link cannot be pinged - i.e. the host was not found, the program 
prints "wasn't found" otherwise it prints "was found" + prints the ping message.

# Measurements

| Websites   | Async | Sync  |
|-----|-------|-------|
| 4   | 3,11  | 12,30  |
| 6  | 3,13  | 18,49  |
| 8  | 3,11 | 24,66 |
| 10  | 3,13 | 30,84  |
| 20  | 3,11 | 61,71  |

In the table above you can see the 5 measurements where the number of pinged URLs varied for each one and you can also see the execution time, in seconds, of the asynchronous program and the synchronous program
for a given number of URLs.
The tests were performed on addresses that could be pinged, so their host was found.

As you can see the asynchronous implementation is faster than the synchronous one, also the asynchronous implementation has almost the same speed, with only a few deviations.
If we ran the asynchronous implementation multiple times and averaged the values, we would get the same time in each of the measurements. With the synchronous implementation, the time increases linearly.
This is due to the fact that in the synchronous implementation the specified pages are pinged in succession. In the asynchronous implementation, the ping functions are executed concurrently.

