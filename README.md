A class to measure time elapsed and count number of passes through code segments
using time.clock()
Useful for benchmarking and code improvement.

Run demo_timer.py to see usage and performance characteristics for various implementations of calculating factorial of a number.

>>> t = Timer()  # starts the timer object
...
>>> t.stop()  # stops the timer object
>>> t.total  # then contains total time between creation and stop() in seconds.
>>> repr(t)  # returns time with units as string, so print(t) can be used.

>>> t = Timer(wait=True)  # creates timer but doesn't start measuring. t can be passed to functions to measure time
wait is False by default. See previous case.

>>> t.start()  # begins measuring.
...
>>> t.stop()  # stops measuring.
...
>>> t.start() # starts measuring again
...
>>> t.stop()  # stops measuring
>>> t.total  # now has total time recorded between starts and stops in seconds
>>> t.count  # contains number of times the timer was triggered

This can be used in a loop to measure time per loop or count number of times a function was called.

>>> t = Timer(unit='s')  # to define what units to print the time in.

Options are 's' (second), 'ms' (millisecond), 'm' (minute) and 'h' (hour).

By default the unit is 'ms' but in a project the default units can be set before all usages by

>>> Timer.default_unit = 's'  # or any unit

