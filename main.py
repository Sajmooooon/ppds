class Task:
    def __init__(self, task, task_id):
        self.id = task_id
        self.task = task

    def run(self):
        return self.task.send(None)


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, task_id):
        new_task = Task(task, task_id)
        self.tasks.append(new_task)

    def schedule(self):
        self.tasks.sort(key=sort_id)
        while self.tasks:
            task = self.tasks.pop(0)
            try:
                task.run()
            except StopIteration:
                continue
            self.tasks.append(task)


def sort_id(task):
    return task.id


def program1():
    for i in range(3):
        print(f'1. program - {i}')
        yield


def program2():
    for i in range(2):
        print(f'2. program - {i}')
        yield


def program3():
    for i in range(4):
        print(f'3. program - {i}')
        yield


scheduler = Scheduler()
scheduler.add_task(program2(), 2)
scheduler.add_task(program1(), 1)
scheduler.add_task(program3(), 3)

scheduler.schedule()
