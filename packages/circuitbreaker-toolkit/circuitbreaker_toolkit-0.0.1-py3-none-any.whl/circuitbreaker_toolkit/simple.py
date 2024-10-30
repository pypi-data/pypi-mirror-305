# SPDX-FileCopyrightText: © 2024 David E. James
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE

from functools import wraps
from enum import Enum

from .defaults import Defaults

# @todo: fix this - I was having circular import issues between breaker and
#        defaults when trying to set the default there.
from .breaker import breaker_factory
if Defaults.BREAKER_FACTORY is None:
    Defaults.BREAKER_FACTORY = breaker.breaker_factory


def circuitbreaker(
    open_threshold = None,
    open_timeout   = None,
    forgiveness    = None,
    exceptions     = None,
    time_func      = None,
    **kwargs
    ):

    def _circuitbreaker_decorator(func):
        _cb_factory = kwargs.get('breaker_factory', Defaults.BREAKER_FACTORY)

        # pass everything as kwargs so position is no longer important
        _breaker = _cb_factory(open_timeout   = open_timeout,
                               open_threshold = open_threshold,
                               forgiveness    = forgiveness,
                               exceptions     = exceptions,
                               time_func      = time_func,
                               **kwargs)

        @wraps(func)
        def _circuitbreaker_wrapper(*_args, **_kwargs):
            _breaker.start()
            _exceptions = _breaker.get_exceptions()

            try:
                return_val = func(*_args, **_kwargs)

            except _exceptions as e:
                _breaker.listed_exception(e)
                raise

            except Exception as e:
                _breaker.generic_exception(e)
                raise

            else:
                _breaker.no_exception()

            finally:
                _breaker.end()

            return return_val

        return _circuitbreaker_wrapper
    return _circuitbreaker_decorator

