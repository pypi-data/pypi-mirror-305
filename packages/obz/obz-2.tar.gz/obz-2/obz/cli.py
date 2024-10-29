# This file is place in the Public Domain.
# pylint: disable=C


"cli"


import os
import sys


from obx.persist import Workdir
from obx.object  import Config
from obx.runtime import Client, Errors, Event, errors, wrap


from .command import NAME, scanner, command, parse
from .modules import face


Workdir.wdr = os.path.expanduser(f"~/.{NAME}")


cfg  = Config()


class CLI(Client):

    def __init__(self):
        Client.__init__(self)
        self.register("command", command)

    def raw(self, txt):
        print(txt)


def wrapped():
    wrap(main)
    for error in errors():
        print(line)


def main():
    parse(cfg, " ".join(sys.argv[1:]))
    scanner(face)
    evt = Event()
    evt.txt = cfg.txt
    csl = CLI()
    command(csl, evt)
    evt.wait()


if __name__ == "__main__":
    wrapped()
