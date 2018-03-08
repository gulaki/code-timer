## codetimer 

This is a module to measure time elapsed and count number of passes through code segments and functions.

Useful for benchmarking, testing different implementaions for performance, statistical time analysis of code, etc.

Run *demo_timer.py* to see usage and performance characteristics for various implementations of calculating the factorial of a number.

- *Timer()* is a simple timer that simply measures total time and number of passes through code. *Use like tick() and tock() of Matlab.*

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

- *FunctionTimer()* can be used as a decorator to measure accumulated time of a function's execution.
Invoke the *.timer* member to get the total time and count

    @FunctionTimer
    def afunction(args):
        # some process

    for i in range(1000):
        afunction(args)

    t = afunction.timer
    print(t.total, t.count))
    print('Time per loop =', t.total/t.count)

    afunction.timer.reset()  # resets the timer to zero.

- *TimerStats()* extends Timer() by enabling simple statistical analysis on collected time data.

      >>> t = TimerStats()  # initializes the timer and always waits by default. Units can be specified and default can be set like Timer().
      ...
      >>> for i in range(10000):
      ...     t.start()
      ...     ...
      ...     t.stop()
      >>> t.final_stats()  # call this after measurement is done to calculate mean and standard deviation
      >>> t.min  # minimum lap time (s)
      >>> t.max  # maximum lap time (s)
      >>> t.total  # total time (s)
      >>> t.count  # no. of laps
      >>> t.mean  # average lap time (s)
      >>> t.std  # standard deviation (s)
      >>> repr(t)  # returns total time with units as string
      >>> str(t)  # 'total=9604.3762 ms, min=90.9867 ms, max=100.9108 ms, mean=96.0438 ms, std=10.0969 ms.'

A call to *TimerStats.stop()* also returns the lap time. So if required it can be saved as lap data.

- *FunctionTimerStats()* is similar to FunctionTimer decorator but enables statistical analysis on the timing data using TimerStats()

eg:
    
    @FunctionTimerStats
    def afunction(args):
        # do something
        return something

    for i in range(1000):
        retval = afunction(args)
        lap = afunction.lap  # Each lap time can be caught for further analysis

    t = afunction.final_stats()  # calculates mean and std and can be accessed from the members.
    print(t)  # Formatted output giving detailed information

Run *test_stats.py* to see statistical analysis of time data from running a function. Need Matplotlib to see the plots.

*Note: Feel free to suggest features/code or report bugs if any. I dont think I have tested it enough. I hope this can become a comprehensive module for developing fast computational projects.*