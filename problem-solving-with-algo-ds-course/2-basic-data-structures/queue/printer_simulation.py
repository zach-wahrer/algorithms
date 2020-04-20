from models.queue import Queue  # As previously defined
from models.printer import Printer  # As previously defined
from models.task import Task  # As previously defined
import random


def simulation(num_seconds, pages_per_minute, students_in_lab, tasks_per_student):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task(students_in_lab, tasks_per_student):
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def new_print_task(students_in_lab, tasks_per_student):
    chance_of_print_task_per_second = (3600 / (students_in_lab * tasks_per_student))
    num = random.randrange(1, chance_of_print_task_per_second + 1)
    if num == chance_of_print_task_per_second:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5, 20, 2)
