# This file is placed in the Public Domain.
# pylint: disable=C,W0212


"daemon"


import os
import sys


from .command import NAME, scanner
from .modules import face
from .persist import Workdir, pidfile, pidname
from .runtime import forever, privileges, errors, wrap


Workdir.wdr = os.path.expanduser(f"~/.{NAME}")


def daemon(verbose=False):
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    os.nice(10)


def main():
    daemon("-v" in sys.argv)
    privileges()
    pidfile(pidname(NAME))
    scanner(face, init=True)
    forever()


def wrapped():
    wrap(main)
    if "-v" in sys.argv:
        for line in errors():
            print(line)


if __name__ == "__main__":
    wrapped()
