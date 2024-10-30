
import pytest

from circuitbreaker_toolkit.breaker import (
    breaker_factory,
    State,
    CircuitBreaker,
)

from circuitbreaker_toolkit.defaults import Defaults

from circuitbreaker_toolkit.exceptions import (
    FooException,
    CircuitBreakerOpen,
    CircuitBreakerSequenceError,
)


#┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
# Basic Tests - laying the groundwork for later tests                          #
#┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
def test__default():
    '''verify default factory works'''
    breaker = breaker_factory()


#╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
def test__basic__no_exc():
    '''verify basic flow works'''
    breaker = breaker_factory()
    breaker.start()
    breaker.no_exception()
    breaker.end()


#╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
def test__basic__generic_exc():
    '''verify basic flow with generic exception works'''
    breaker = breaker_factory()
    breaker.start()
    breaker.generic_exception(None)
    breaker.end()


#╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌#
def test__basic__listed_exc():
    '''verify basic flow with defaults and non-generic exception errors'''
    breaker = breaker_factory()
    breaker.start()
    with pytest.raises(AssertionError):
        breaker.listed_exception(None)

    # since `listed_exception` raised, end is now out of sequence
    with pytest.raises(CircuitBreakerSequenceError):
        breaker.end()



#┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
# Bad Sequences - verify casese that should throw sequence errors              #
#┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
def test__bad_sequence__start():
    breaker = breaker_factory()
    breaker.start()
    with pytest.raises(CircuitBreakerSequenceError):
        breaker.start()


def test__bad_sequence__listed_exc():
    '''sequence error - did not start, but marked exception'''
    breaker = breaker_factory()
    with pytest.raises(CircuitBreakerSequenceError):
        breaker.listed_exception(None)


def test__bad_sequence__generic_exc():
    '''sequence error - did not start, but marked exception'''
    breaker = breaker_factory()
    with pytest.raises(CircuitBreakerSequenceError):
        breaker.generic_exception(None)


def test__bad_sequence__no_exc():
    '''sequence error - did not start, but marked (no)exception'''
    breaker = breaker_factory()
    with pytest.raises(CircuitBreakerSequenceError):
        breaker.no_exception()


def test__bad_sequence__end():
    '''sequence error - did not start, but marked end'''
    breaker = breaker_factory()
    with pytest.raises(CircuitBreakerSequenceError):
        breaker.end()


def test__bad_sequence__start_end():
    '''sequence error - start then stop - no result'''
    breaker = breaker_factory()
    breaker.start()
    with pytest.raises(CircuitBreakerSequenceError):
        breaker.end()


#┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
# Sequencing - verify circuit breaker core logic                               #
#┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈#
def test__sequence():
    _fake_t = 0.0
    def fake_time_f():
        nonlocal _fake_t
        _fake_t += 0.1
        return _fake_t

    save_time_f = Defaults.TIME_FUNC
    Defaults.TIME_FUNC = fake_time_f

    try:
        breaker = breaker_factory()

        def _success_run():
            breaker.start()
            breaker.no_exception()
            breaker.end()

        # all good runs should not throw CircuitBreakerOpen
        for _ in range(20):
            _success_run()

    finally:
        Defaults.TIME_FUNC = save_time_f


def test__sequence__failure():
    _fake_t = 0.0
    def fake_time_f():
        nonlocal _fake_t
        _fake_t += 0.1
        return _fake_t

    save_time_f = Defaults.TIME_FUNC
    Defaults.TIME_FUNC = fake_time_f

    try:
        breaker = breaker_factory()

        def _failure_run():
            breaker.start()
            breaker.generic_exception(None)
            breaker.end()

        i = 0
        # all good runs should not throw CircuitBreakerOpen
        with pytest.raises(CircuitBreakerOpen):
            for i in range(20):
                _failure_run()

        # it should take exactly 'threshold + +1' loops to get failure
        assert float(i) == Defaults.BREAKER_OPEN_THRESHOLD + 1.0

    finally:
        Defaults.TIME_FUNC = save_time_f


def test__sequence__open():
    _fake_t = 0.0
    def fake_time_f():
        nonlocal _fake_t
        _fake_t += 0.1
        return _fake_t

    save_time_f = Defaults.TIME_FUNC
    Defaults.TIME_FUNC = fake_time_f

    try:
        breaker = breaker_factory()

        def _success_run():
            breaker.start()
            breaker.no_exception()
            breaker.end()

        def _failure_run():
            breaker.start()
            breaker.generic_exception(None)
            breaker.end()

        i = 0
        # all good runs should not throw CircuitBreakerOpen
        with pytest.raises(CircuitBreakerOpen):
            for i in range(20):
                _failure_run()

        # it should take exactly 'threshold + +1' loops to get failure
        assert float(i) == Defaults.BREAKER_OPEN_THRESHOLD + 1.0
        assert breaker._state == State.OPEN

        # pretend enough time has passed... verify HALF_CLOSED
        _fake_t += Defaults.BREAKER_OPEN_TIME
        breaker.start()
        assert breaker._state == State.HALF_CLOSED

        # but nooo, another error? back to open...
        breaker.generic_exception(None)
        breaker.end()
        assert breaker._state == State.OPEN

        # now we're open again
        with pytest.raises(CircuitBreakerOpen):
            _success_run()

        # (fake) wait some more....
        _fake_t += Defaults.BREAKER_OPEN_TIME
        breaker.start()
        assert breaker._state == State.HALF_CLOSED
        breaker.no_exception()
        breaker.end()

        # finally, back to closed
        assert breaker._state == State.CLOSED

    finally:
        Defaults.TIME_FUNC = save_time_f





