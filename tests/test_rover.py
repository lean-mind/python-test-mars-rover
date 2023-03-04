from unittest import TestCase

from assertpy import assert_that

from src.rover import Rover


class TestRover(TestCase):
    def test_should_be_instantiated(
        self,
    ):
        rover = Rover()
        assert_that(rover).is_not_none()
