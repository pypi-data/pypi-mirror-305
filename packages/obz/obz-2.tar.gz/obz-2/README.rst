**NAME**

::

    obz - OBZ.


**SYNOPSIS**

::

    python3 -m obz <cmd> [key=val] [key==val]
    python3 -m obz.console
    python3 -m obz.daemon
    python3 -m obz.service


**DESCRIPTION**

::

    OBZ is a demo bot, it can connect to IRC, fetch and display RSS
    feeds, take todo notes, keep a shopping list and log text. You can
    also copy/paste the service file and run it under systemd for 24/7
    presence in a IRC channel.

    OBX has all the python3 code to program a unix cli program, such as
    disk perisistence for configuration files, event handler to
    handle the client/server connection, deferred exception handling to not
    crash on an error, a parser to parse commandline options and values, etc.

    OBX uses object programming (OP) that allows for easy json save//load
    to/from disk of objects. It provides an "clean namespace" Object class
    that only has dunder methods, so the namespace is not cluttered with
    method names. This makes storing and reading to/from json possible.

    OBX/OBZ is Public Domain.


**INSTALL**

::

    $ pipx install obz
    $ pipx ensurepath


**CONFIGURATION**


irc

::

    $ obz cfg server=<server>
    $ obz cfg channel=<channel>
    $ obz cfg nick=<nick>

sasl

::

    $ obz pwd <nsvnick> <nspass>
    $ obz cfg password=<frompwd>

rss

::

    $ obz rss <url>
    $ obz dpl <url> <item1,item2>
    $ obz rem <url>
    $ obz nme <url> <name>

opml

::

    $ obz exp
    $ obz imp <filename>


**SYSTEMD**

::

    $ obz srv > obz.service
    $ sudo mv obz.service /etc/systemd/system/
    $ sudo systemctl enable obz --now

    joins #obz on localhost


**USAGE**


without any argument the bot does nothing

::

    $ python3 -m obz
    $

see list of commands

::

    $ python3 -m obz cmd
    cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,
    pwd,rem,req,res,rss,srv,syn,tdo,thr,upt


start a console

::

    $ python3 -m obz.console
    >


use -v to enable verbose

::

    $ python3 -m obz.console -v
    OBX since Tue Sep 17 04:10:08 2024
    > 


use -i to init modules

::

    $ python3 -m obz.console -i
    >



start daemon

::

    $ python3 -m obz.daemon
    $


start service

::

   $ python3 -m obz.service
   <runs until ctrl-c>


**COMMANDS**

::

    here is a list of available commands

    cfg - irc configuration
    cmd - commands
    dpl - sets display items
    err - show errors
    exp - export opml (stdout)
    imp - import opml
    log - log text
    mre - display cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    res - restore deleted feeds
    rss - add a feed
    srv - create service file
    syn - sync rss feeds
    tdo - add todo item
    thr - show running threads


**SOURCE**

::

    source is at https://bitbucket.org/objx/obz


**FILES**

::

    ~/.obz
    ~/.local/pipx/venvs/obz/*


**AUTHOR**

::

    Bart Thate <bthate@dds.nl>


**COPYRIGHT**

::

    OBZ is Public Domain.
