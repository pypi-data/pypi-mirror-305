# This file is placed in the Public Domain.
# pylint: disable=C,W0105


"list of commands"


from obx.object  import keys


from ..command import Commands


def cmd(event):
    event.reply(",".join(sorted(keys(Commands.cmds))))
