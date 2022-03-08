# PPDS 01
Third assignment from the PPDS course.

## Description
In this project, we created simple implementation of the Consumer-Producer problem, where producer produced items then added them to the warehouse and
the consumer retrieved and processed the products from the warehouse. In both examples the producer and consumer were executed in a loop.

In our project, we decided to simulate production in the ``producer()`` using ``sleep()`` with a selected time value, followed by
wait to see if there is free space in the warehouse via ``free.wait()`` and then check if the threads should finish, if so the loop is terminated. 
To simulate exclusive access to the warehouse we used ``lock()``, 
then we simulate storing the product in the warehouse using ``sleep()`` with the selected value, we further increased the total number of produced products that 
are stored in the variable ``counter``, then simulate the departure from the warehouse with ``unlock()`` and finally increase the number of products in the scalde
via ``items.signal()``.

For ``consumer()``, the number of items in the warehouse is first checked with ``items.wait()``, as in the previous example, it is checked to see if it should exit
and if it does, the loop is terminated. Access to the warehouse is then gained via 
``lock()`` as in the previous example. Next, the retrieval of the product from the warehouse is simulated, via ``sleep()`` with the selected time value. Then
is simulated leaving the warehouse via ``unlock()``, and ``free.signal()`` is used to simulate removing the product from the warehouse. Finally
``sleep()`` is used with the selected value to simulate the processing of the product.


## Experiment
In our experiments we changed 2 values, and we observed changes depending on the number of products per second.
We created simple grid search function which allows us to test multiple values, and then we displayed the results in graphs, 
which you can see below.

### Experiment 1
In the first experiment, we tracked the number of items produced in one second in dependence on 2 values that we adjusted. 
The first value was the production time and the second 
the number of consumers. We varied both values in intervals, for the number of consumers we varied the values
from 1-10 consumers and for production time we varied the values in the interval from 0-9/250. We also set the warehouse size to 100 items
and we set the value in the ``sleep()`` function waiting for the main thread to complete to 0.08.

In the experiment, we can observe that the most items were just created with the least amount of time and with the largest number of consumers
as this resulted in a fast release of stock. We can also see that with the smallest time and number of consumers gradually started to increase
the number of products per second, since with fewer consumers the stock was slowly released. We can also observe a sudden decrease in the number of
of products at 6 consumers with the lowest rate, which could be due to the use of random values from the intervals in the other ``sleep()`` 
functions other than production time.

<img src="https://i.imgur.com/tt1e0vV.png" width="350px">

### Experiment 2
In this experiment, we removed the sleep function that simulates storing the product in the warehouse inside the lock in the producer
and we also removed the sleep function, which simulates the retrieval of the product from the warehouse from inside the lock. Time to complete the main
threads was set to 0.05.
Then we set the warehouse size to 100, we set the production time in the internval to (produce_time+1) / 250 and the processing time
of the product to sleep(randint(1, 10) / 250). And in the cycle, we increased the number of consumers and produce_time from 0 to 10.
With this setup, we achieved an ideal graph, which you can se below.

<img src="https://i.imgur.com/BlcNKFW.png" width="350px">

### Experiment 3
In this experiment, we observed the dependence of the number of producers on the production time. As we can see in the graph below, we can see that the most
products were created with the largest number of producers and the smallest amount of time, and conversely the smallest number of producers
with the largest production time produced the smallest number of products per second. We had the same network setup as in the previous example.
Only instead of increasing the conzumets we gradually increased the producers, we also started with a production rate of 0 and gradually increased the
up to 9/250. We set the time to store and retrieve from stock to randint(1, 10) / 400. We set the scald size to 100.

<img src="https://i.imgur.com/jT7PvZD.png" width="350px">
