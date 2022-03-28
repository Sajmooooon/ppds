# PPDS 06
Sixth assignment from the PPDS course.

# Description
In this assignment, we implemented a simple problem of a barber shop that has multiple customers coming in, but 
has only one barber, at the same time the barber shop has a limited number of places, so when the capacity is full, the customers
have to come back later.

# Implementation
We have created 2 main functions barber and customer. In the barber function, at the beginning there is an infinite loop, first the barber waits for the customer (signal
from the customer) - he sleeps, he gets it when the customer arrives, then he sends a signal to the customer to sit in the chair and start cutting his hair,
this is simulated by the cut_hair function. After the cut, he waits for a signal from the customer and when it arrives he also sends a signal to the customer that he has finished cutting.

In the customer function we first created an infinite loop, then a lock occurs and checks if the barber shop is full, if so
then the mutex is unlocked, and the leave is simulated using sleep in the balk function. If the barbershop is not full, the number of customers is increased and
which customer is waiting for a haircut. If the barber is not busy, the client sends a signal to the barber to "wake up" and waits for a signal from the barber
so that he can sit in the chair where he will cut his hair. The client is then cut and this is simulated using the get_hair_cut function. After the haircut
the customer sends a signal that he is cut and waits for a signal from the barber. When he receives the signal, the customer leaves, thus the number of customers is decremented in the locked mutex
and waits for the hair to grow back, which is simulated by sleep in the groving_hair function. After the hair grows back, he comes to the barbershop again.

