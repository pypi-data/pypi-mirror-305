**NAME**

::

    OBX - write your own commands.


**SYNOPSIS**

::

    >>> from obx.object import Object, loads, dumps
    >>> o = Object()
    >>> o.a = 'b'
    >>> print(loads(dumps(o)))
    {'a': 'b'}


**DESCRIPTION**

::

    OBX has all the python3 code to program a unix cli program, such as
    disk perisistence for configuration files, event handler to
    handle the client/server connection, deferred exception handling to not
    crash on an error, a parser to parse commandline options and values, etc.

    OBX uses object programming (OP) that allows for easy json save//load
    to/from disk of objects. It provides an "clean namespace" Object class
    that only has dunder methods, so the namespace is not cluttered with
    method names. This makes storing and reading to/from json possible.

    OBX is Public Domain.


**INSTALL**

::

    $ pipx install obx
    $ pipx ensurepath


**SOURCE**

::

    source is at https://bitbucket.org/objx/obz


**AUTHOR**

::

    Bart Thate <bthate@dds.nl>


**COPYRIGHT**

::

    OBX is Public Domain.
