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

# Pseudocode
```
FUNCTION get_hair_cut(customer_id):
    PRINT("Customer %d: Getting my hair haircut.",customer_id)
    sleep(0.1 s)
ENDFUNCTION


FUNCTION cut_hair():
    PRINT("Barber: Cutting hair.")
    sleep(0.1 s)
ENDFUNCTION


FUNCTION balk(customer_id):
    PRINT("Customer %d: The barber shop is full,
          I will come next time.",customer_id)
    sleep(0.2 to 0.3 s)
ENDFUNCTION


FUNCTION groving_hair(customer_id):
    PRINT("Customer %d: waiting for my hair to grow.",customer_id)
    sleep(0.3 to 0.5 s)
ENDFUNCTION


FUNCTION customer(customer_id):
    WHILE True:
        mutex.lock()
        IF customers is equal N
            mutex.unlock()
            balk(customer_id)
        ELSE
            customers += 1
            PRINT("Customer %d: Waiting for haircutting.",customer_id)
            mutex.unlock()

            customer.signal()
            barber.wait()

            get_hair_cut(customer_id)
            customer_done.signal()
            barber_done.wait()

            mutex.lock()
            customers -= 1
            mutex.unlock()
            groving_hair(customer_id)
    ENDWHILE


FUNCTION barber():
    WHILE True:
        customer.wait()
        barber.signal()

        cut_hair()

        customer_done.wait()
        barber_done.signal()
    ENDWHILE
ENDFUNCTION


FUNCTION main():
    customers = 3
    threads = []
    FOR customer_id=0 in customers-1:
        threads.append(Thread(customer, customer_id))
    ENDFOR
    threads.append(Thread(barber,))
    FOR t=0 to threads.length-1:
        t.join()
    ENDFOR
ENDFUNCTION


```