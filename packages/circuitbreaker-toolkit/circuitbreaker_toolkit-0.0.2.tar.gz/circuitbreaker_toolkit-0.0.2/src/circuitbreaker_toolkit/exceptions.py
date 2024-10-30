# SPDX-FileCopyrightText: © 2024 David E. James
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE
''' Exception Classes for CircuitBreaker use.
'''

class FooException(Exception):
    '''A dummy exception class.

    This is used when CircuitBreaker is setup to catch generic exceptions to
    keep except clause happy.
    '''
    pass


class CircuitBreakerOpen(Exception):
    '''Function call skipped due to open breaker.

    When trying to call a wrapped function, if the circuit breaker is in an
    open state, this execption will be thrown.
    May be expanded in the future to include meta data on the breaker.
    '''
    pass


class CircuitBreakerSequenceError(Exception):
    '''A sanity-check exception class.

    Should never happen if utilizing circuitbreaker decorator functionality.
    Indicates the API for the CircuitBreaker state class is being used
    out of order.

    As with all "should never happen" errors, this should be checked for at
    some level of code as an indication that "something is horribly wrong", or
    this should just be allowed to crash the program (so a new instance can be
    started in its place).
    '''
    pass


