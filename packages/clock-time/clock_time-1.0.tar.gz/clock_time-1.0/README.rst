Introduction
------------

Provide ``sleep(secs)`` / ``time_s()`` functions. Fix overflow bugs in CPython implementation so far (v3.14.0a1).


``sleep(secs)``
---------------

Use ``clock_nanosleep()`` with ``CLOCK_MONOTONIC`` to sleep. So that the sleep is not affected by system date/time jumps.

On CPython 3.11+, `time.sleep() <https://docs.python.org/3/library/time.html#time.sleep>`_ function already use this method.


``time_s()``
------------

Return time as an integer number of seconds since the `epoch <https://docs.python.org/3/library/time.html#epoch>`_.


Usage
-----

Only provide source code distribution, user need to install the build toolchain. It can't be compiled on platforms without ``clock_nanosleep()``.

.. sourcecode:: python

    try:
        from clock_time import sleep, time_s
    except ImportError:
        from time import sleep, time_ns
        def time_s():
            return time_ns() // 1_000_000_000

    sleep(secs)
    t = time_s()
