"""Example a fork call in Unix."""

from os import fork, getpid, _exit


def child():
    print("Я дочерний поток %i" % getpid())
    _exit(0)


def parent():
    """Forks new child process, enter 'q' to exit."""
    while True:
        pid = fork()
        if pid == 0:
            child()
        else:
            print('Я родительский процесс %i' % getpid())
        if input() == 'q':
            break
