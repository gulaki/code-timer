from time import clock, time
import sys

if sys.platform == 'win32':
    timer_func = clock
else:
    timer_func = time

UNITS = {'s': 1, 'ms': 1000, 'm': 1/60, 'h': 1/3600}
STATES = {'simple': False, 'stats': True}


class Timer(object):
    """
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
    """
    default_unit = 'ms'

    def __init__(self, **kwargs):
        self._start = 0
        self.is_running = False
        self.unit = kwargs['unit'] if 'unit' in kwargs else self.__class__.default_unit
        self.count = 0
        self.total = 0
        try:
            if not kwargs['wait']:
                self.start()
        except KeyError:
            self.start()

    def start(self):
        if not self.is_running:
            self.count += 1
            self.is_running = True
            self._start = timer_func()
        else:
            raise RuntimeWarning('Timer already running.')

    def stop(self):
        if self.is_running:
            self.total += timer_func() - self._start
            self.is_running = False
        else:
            raise RuntimeWarning('Check code. Timer is already stopped.')

    def reset(self):
        self.is_running = False
        self.count = 0
        self.total = 0
        self._start = 0

    def __repr__(self):
        fact = UNITS[self.unit]
        return str(round(self.total*fact, 4)) + ' ' + self.unit


class TimerStats(Timer):
    """
    TimerStats() extends Timer() by enabling simple statistical analysis on collected time data.

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

    A call to TimerStats.stop() also returns the lap time. So if required it can be saved as lap data if required.
    """
    default_unit = 'ms'

    def __init__(self):
        self.total2 = 0
        self.min = 0
        self.max = 0
        self.mean = 0
        self.std = 0
        Timer.__init__(self, wait=True)

    def start(self):
        if not self.is_running:
            self.count += 1
            self.is_running = True
            self._start = timer_func()
        else:
            raise RuntimeWarning('Timer already running.')

    def stop(self):
        if self.is_running:
            lap = timer_func() - self._start
            self.total += lap
            self.total2 += lap ** 2
            self.is_running = False
            if self.count == 1:
                self.min = self.max = lap
            else:
                if lap < self.min:
                    self.min = lap
                if lap > self.max:
                    self.max = lap
        else:
            raise RuntimeError('Check code. Timer is already stopped.')
        return lap

    def final_stats(self):
        self.mean = self.total / self.count
        self.std = (self.total2 / (self.count-1) - self.mean ** 2) ** 0.5
        self.min = self.min
        self.max = self.max

    def reset(self):
        self.is_running = False
        self.count = 0
        self.total = 0
        self._start = 0

    def __repr__(self):
        return str(round(self.total*UNITS[self.unit], 4)) + ' ' + self.unit

    def __str__(self):
        n = 4
        fact = UNITS[self.unit]
        tot = str(round(self.total*fact, n))
        min = str(round(self.min*fact, n))
        max = str(round(self.max*fact, n))
        mean = str(round(self.mean*fact, n))
        std = str(round(self.std*fact, n))
        stat_str = 'iters={cnt}: total={total} {unit}, min={min} {unit}, max={max} {unit}, ' \
                   'mean={mean} {unit}, std={std} {unit}.'
        return stat_str.format(unit=self.unit, total=tot, min=min, max=max, mean=mean, std=std, cnt=self.count)


class FunctionTimer(object):
    """
        Use FunctionTimer as a decorator to measure accumulated time of a function's execution.
        Invoke the .timer member to get the total time and count

        eg:
            @FunctionTimer
            def afunction(args):
                # do some thing

            for i in range(1000):
                afunction(args)

            t = afunction.timer
            print(t.total, t.count)
    """
    def __init__(self, f):
        self.timer = Timer(wait=True)
        self.f = f

    def __call__(self, *args, **kwargs):
        self.timer.start()
        returns = self.f(*args, **kwargs)
        self.timer.stop()
        return returns


class FunctionTimerStats(object):
    """
        FunctionTimerStats is similar to FunctionTimer decorator but enables statistical analysis on the timing data using TimerStats()

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
    """
    def __init__(self, f):
        self.timer = TimerStats()
        self.f = f
        self.lap = 0

    def __call__(self, *args, **kwargs):
        self.timer.start()
        returns = self.f(*args, **kwargs)
        self.lap = self.timer.stop()
        return returns
