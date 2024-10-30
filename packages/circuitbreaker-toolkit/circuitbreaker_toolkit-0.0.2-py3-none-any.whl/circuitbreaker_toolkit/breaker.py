# SPDX-FileCopyrightText: © 2024 David E. James
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from enum import Enum

from .defaults import Defaults
from .exceptions import (
    FooException,
    CircuitBreakerOpen,
    CircuitBreakerSequenceError,
)


#──────────────────────────────────────────────────────────────────────────────#
# Factory                                                             §factory #
#──────────────────────────────────────────────────────────────────────────────#

def breaker_factory(*args, **kwargs):
    return CircuitBreaker(*args, **kwargs)


#──────────────────────────────────────────────────────────────────────────────#
# State Definitions                                                     §state #
#──────────────────────────────────────────────────────────────────────────────#

class State(Enum):
    CLOSED      = 1
    OPEN        = 2
    HALF_CLOSED = 3


#──────────────────────────────────────────────────────────────────────────────#
# Breaker Class                                                       §breaker #
#──────────────────────────────────────────────────────────────────────────────#

class CircuitBreaker:
    #┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
    # Init and Configuration                                     §breaker.init #
    #┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
    def __init__(self,
                 open_timeout   = None,
                 open_threshold = None,
                 forgiveness    = None,
                 exceptions     = None,
                 time_func      = None,
                 **kwargs
                 ):
        self._open_timeout_f = \
            _ensure_callable(open_timeout, Defaults.BREAKER_OPEN_TIME)

        self._open_threshold_f = \
            _ensure_callable(open_threshold, Defaults.BREAKER_OPEN_THRESHOLD)

        self._configure_exceptions(exceptions)
        self._configure_forgiveness(forgiveness)

        if time_func is not None and not callable(time_func):
            raise ValueError(f'time_func must be callable or NoneType')

        self._time_f = time_func or Defaults.TIME_FUNC

        # internal state vars
        self._in_process    = False
        self._result_marked = False
        self._state         = State.CLOSED
        self._opened_time   = None
        self._failures      = 0.0

        self._failure_update_time = self._time_f()

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def _configure_exceptions(self, exceptions):
        if exceptions is None:
            self._exception_f = lambda: FooException
            self._fail_on_generic = True

        elif callable(exceptions) and not inspect.isclass(exceptions):
            self._exception_f = exceptions
            self._fail_on_generic = False

        else:
            self._exception_f = lambda: exceptions
            self._fail_on_generic = False

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def _configure_forgiveness(self, forgiveness):
        if callable(forgiveness):
            self._forgive_f = forgiveness
            return

        _forgiveness = forgiveness or Defaults.FORGIVENESS

        try:
            forgive_rate = float(_forgiveness)
        except ValueError:
            raise ValueError(f'forgiveness must be callable or float')

        def forgiveness_f(elapsed):
            return elapsed * forgive_rate

        self._forgive_f = forgiveness

    #┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
    # Public Interfaces                                        §breaker:public #
    #┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
    def start(self):
        if self._in_process:
            raise CircuitBreakerSequenceError()

        self._in_process = True
        self._result_marked = False

        if self._state != State.OPEN:
            return

        timestamp = self._time_f()
        elapsed   = timestamp - self._opened_time

        if elapsed >= self._open_timeout_f():
            self._state = State.HALF_CLOSED

        if self._state == State.OPEN:
            self._in_process = False
            raise CircuitBreakerOpen()

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def get_exceptions(self):
        return self._exception_f()

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def listed_exception(self, exception):
        if not self._in_process:
            raise CircuitBreakerSequenceError()

        # if user didn't specify exceptions, then the only exception that
        # gets here is a 'fake' unused exception
        assert self._fail_on_generic == False

        timestamp = self._time_f()
        self._mark_failure(timestamp)

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def generic_exception(self, exception):
        if not self._in_process:
            raise CircuitBreakerSequenceError()

        timestamp = self._time_f()

        if self._fail_on_generic:
            self._mark_failure(timestamp)

        else:
            self._mark_success(timestamp)

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def no_exception(self):
        if not self._in_process:
            raise CircuitBreakerSequenceError()

        timestamp = self._time_f()
        self._mark_success(timestamp)

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def end(self):
        if not self._in_process or not self._result_marked:
            raise CircuitBreakerSequenceError()

        self._in_process = False

    #┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
    # Internal Actions                                        §breaker.private #
    #┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
    def _mark_success(self, timestamp):
        if self._state == State.HALF_CLOSED:
            self._state    = State.CLOSED
            self._failures = 0
        self._result_marked = True

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def _mark_failure(self, timestamp):
        self._failures += 1.0
        if self._state == State.HALF_CLOSED or \
           self._failures > self._open_threshold_f():
            self._state      = State.OPEN
            self._opened_time = timestamp
        self._result_marked = True

    #╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
    def _forgive(self, timestamp):
        elapsed        = timestamp - self._failure_update_time
        forgive_amt    = self._forgive_f(elapsed)
        self._failures = max(0, self._failures - forgive_amt)

        self._failure_update_time = timestamp


#──────────────────────────────────────────────────────────────────────────────#
# Private Utilities                                                   §private #
#──────────────────────────────────────────────────────────────────────────────#

def _ensure_callable(var, default):
    if callable(var):
        return var

    if var is not None:
        return lambda *args, **kwargs: var

    if callable(default) and not inspect.isclass(default):
        return default

    return lambda *args, **kwargs: default

