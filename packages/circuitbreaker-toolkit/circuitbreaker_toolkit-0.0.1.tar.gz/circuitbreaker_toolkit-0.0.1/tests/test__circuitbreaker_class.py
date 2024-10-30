
import pytest

from circuitbreaker_toolkit.breaker import (
    breaker_factory,
    State,
    CircuitBreaker,
)



def test__default():
    breaker = breaker_factory()


