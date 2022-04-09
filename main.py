"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.
Implementation of the Scheduler.
"""


class Task:
    """The Task class."""

    def __init__(self, task, task_id):
        """
        The constructor for Task class.

        Parameters:
        task: The coroutine to be executed.
        task_id: The ID of task.
        """

        self.id = task_id
        self.task = task

    def run(self):
        return self.task.send(None)


class Scheduler:
    """The Scheduler class."""

    def __init__(self):
        """The constructor for Scheduler class."""

        self.tasks = []

    def add_task(self, task, task_id):
        """
        The function to create new Task object and add to list.

        Parameter:
        task: The coroutine to be executed.
        task_id: The ID of task.
        """

        new_task = Task(task, task_id)
        self.tasks.append(new_task)

    def schedule(self):
        """The function to schedule tasks in list sorted by ID."""

        self.tasks.sort(key=sort_id)
        while self.tasks:
            task = self.tasks.pop(0)
            try:
                task.run()
            except StopIteration:
                continue
            self.tasks.append(task)


def sort_id(task):
    """
    The simple function to return id of Task.

    Parameter:
    task: The Task object.
    """

    return task.id


def program1():
    """The simple function to print message in for loop."""

    for i in range(3):
        print(f'1. program - {i}')
        yield


def program2():
    """The simple function to print message in for loop."""

    for i in range(2):
        print(f'2. program - {i}')
        yield


def program3():
    """The simple function to print message in for loop."""

    for i in range(4):
        print(f'3. program - {i}')
        yield


scheduler = Scheduler()
scheduler.add_task(program2(), 2)
scheduler.add_task(program1(), 1)
scheduler.add_task(program3(), 3)

scheduler.schedule()
