from time import clock

UNITS = {'s': 1, 'ms': 1000, 'm': 1/60, 'h': 1/3600}


class Timer:
    """
    # code-timer
        A class to measure time elapsed and count number of passes through code segments
        using time.clock()
        Useful for benchmarking and code improvement.

            >>> t = Timer()  # starts the timer object
            ...
            >>> t.stop()  # stops the timer object
            >>> t.total  # then contains total time between creation and stop() in seconds.
            >>> repr(t)  # returns time with units as string, so print(t) can be used.

            >>> t = Timer(wait=True)  # creates timer but doesn't start measuring. t can be passed to functions to measure time
        Wait is False by default. See previous case.

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
    """
    default_unit = 'ms'

    def __init__(self, **kwargs):
        try:
            self.unit = kwargs['unit']
        except KeyError:
            self.unit = self.default_unit
        self.count = 0
        self.total = 0
        self.__start = 0
        self.is_running = False
        try:
            if not kwargs['wait']:
                self.start()
        except KeyError:
            self.start()

    def start(self):
        if not self.is_running:
            self.count += 1
            self.is_running = True
            self.__start = clock()

    def stop(self):
        if self.is_running:
            self.total += clock() - self.__start
            self.is_running = False

    def reset(self):
        self.is_running = False
        self.count = 0
        self.total = 0
        self.__start = 0

    def __repr__(self):
        return str(round(self.total*UNITS[self.unit], 4)) + ' ' + self.unit


class FunctionTimer(object):
    """
        Use as a decorator to measure accumulated time of a function's execution.
        Invoke the .timer member to get the total time and count

        eg:
            @FunctionTimer
            def afunction(args):
                # do some thing

            for i in range(1000):
                afunction(args)

            t = afunction.timer
            print(t.total, t.count))
    """
    def __init__(self, f):
        self.timer = Timer(wait=True)
        self.f = f

    def __call__(self, *args, **kwargs):
        self.timer.start()
        returns = self.f(*args, **kwargs)
        self.timer.stop()
        return returns

