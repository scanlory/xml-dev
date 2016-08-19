#!usr/bin/env python
# (c) R. D. Scanlon 2016

r"""
*Program Title*

*Program Description*
"""


# Imports:
import time
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

# Program Main function:
def main():
    r"""
    Program entry point.
    :return:
    """

    # Add code here.
    while True:
        program_state = input("Please enter a program state, 'q' to quit: ")
        if program_state == 'sched':
           sched = start_scheduler()
        elif program_state == 'add':
            sched.add_job(job_function_1, 'interval', minutes=0.05)
        elif program_state == 'remove':
            sched.remove_job(job_function_1)
        elif program_state == 'q':
            stop_scheduler(sched)
            break


# Functions/Classes/etc.:
def start_scheduler():
    """
    start_scheduler fires off the background scheduler and returns.

    :return: sched: the apscheduler object.
    """
    sched = BackgroundScheduler(timezone=utc)

    sched.add_job(job_function, 'interval', minutes=0.01, max_instances=5)
    sched.start()

    print('Scheduler is running.')
    return sched


def stop_scheduler(sched):
    sched.shutdown()
    print('Scheduler has stopped.')


def job_function():
    print(time.clock())


def job_function_1():
    print('Hello, world!')


# Program state handling:
if __name__ == '__main__':
    main()
