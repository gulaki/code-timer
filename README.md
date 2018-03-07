Timer() is a class to measure time elapsed and count number of passes through code segments using time.clock()
Useful for benchmarking, testing different implementaions for performance.

Run demo_timer.py to see usage and performance characteristics for various implementations of calculating the factorial of a number.

    >>> t = Timer()  # starts the timer object
    ...
    >>> t.stop()  # stops the timer object
    >>> t.total  # then contains total time between creation and stop() in seconds.
    >>> repr(t)  # returns time with units as string, so print(t) can be used.

A timer can be started and instructed to wait till start() method is called.

    >>> t = Timer(wait=True)  # creates timer but doesn't start measuring. wait is False by default. See previous case.

    >>> t.start()  # begins measuring.
    ...
    >>> t.stop()  # stops measuring.
    ...
    >>> t.start() # starts measuring again
    ...
    >>> t.stop()  # stops measuring
    >>> t.total  # now has total time recorded between starts and stops in seconds
    >>> t.count  # contains number of times the timer was triggered.

This can be used in a loop to measure time per loop or count number of times a function was called.

    >>> t = Timer(unit='s')  # to define what units to print the time in.

Options are 's' (second), 'ms' (millisecond), 'm' (minute) and 'h' (hour).

By default the unit is 'ms' but in a project the default units can be set before all usages by

    >>> Timer.default_unit = 's'  # or any unit

Class FunctionTimer can be used as a decorator to measure accumulated time of a function's execution.
Invoke the .timer member to get the total time and count

    @FunctionTimer
    def afunction(args):
        # some process

    for i in range(1000):
        afunction(args)

    t = afunction.timer
    print(t.total, t.count))
    print('Time per loop =', t.total/t.count)

    afunction.timer.reset()  # resets the timer to zero.



