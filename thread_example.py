"""
An example of working with multiple threads in the _thread module.
"""

import time
import _thread


def counter(id, count, stoutmutex, exitmutexes):
    """Prints counter in stdout and simulates job."""

    for item in range(count):
        time.sleep(1 / (id + 1)) # job simulation
        with stoutmutex:
            print(f'Thread {id} printing {item}')
    exitmutexes[id].acquire()


def count_with_threads(count, threads):
    """Starts printing counter with counter call with multiple threads."""   
    exitmutexes = [_thread.allocate_lock() for i in range(threads)]
    stdoutmutex = _thread.allocate_lock()

    for item in range(threads):
        _thread.start_new_thread(counter, (item, count, stdoutmutex, exitmutexes))

    while not all(mutex.locked() for mutex in exitmutexes):
        time.sleep(0.20)
    print('Main thread exiting.')


if __name__ == '__main__':
    count_with_threads(count=2, threads=5)
