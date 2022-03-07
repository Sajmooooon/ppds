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


