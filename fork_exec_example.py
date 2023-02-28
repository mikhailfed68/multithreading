"""
Example of a fork/exec technique in Unix whereby
an executing process spawns a new program.
"""

from os import fork, execlp


def exec_program():
    """Forks new child process and executes new programm inside one."""

    pid = fork()
    if pid == 0:
        execlp('ls', 'ls', '-al')
        assert False, 'Error'
    else:
        print("Child is %i" % pid)


if __name__ == '__main__':
    exec_program()
