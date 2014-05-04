# coding: utf-8

from __future__ import unicode_literals

# This is an end-to-end example of the flaky package in action. Consider it
# a live tutorial, showing the various features in action.

from flaky import flaky
from flaky.utils import TestCase, expectedFailure, skip


class ExampleTests(TestCase):
    _threshold = -1

    def test_non_flaky_thing(self):
        """Flaky will not interact with this test"""
        pass

    @expectedFailure
    def test_non_flaky_failing_thing(self):
        """Flaky will also not interact with this test"""
        self.assertFalse(True)

    @flaky(3, 2)
    def test_flaky_thing_that_fails_then_succeeds(self):
        """
        Flaky will run this test 3 times.
        It will fail once and then succeed twice.
        """
        self._threshold += 1
        if self._threshold < 1:
            raise Exception("Threshold is not high enough.")

    @flaky(3, 2)
    def test_flaky_thing_that_succeeds_then_fails_then_succeeds(self):
        """
        Flaky will run this test 3 times.
        It will succeed once, fail once, and then succeed one more time.
        """
        self._threshold += 1
        if self._threshold == 1:
            self.assertFalse(True)

    @flaky(2, 2)
    def test_flaky_thing_that_always_passes(self):
        """Flaky will run this test twice.  Both will succeed."""
        pass

    @skip("This really fails! Remove this decorator to see the test failure.")
    @flaky()
    def test_flaky_thing_that_always_fails(self):
        """Flaky will run this test twice.  Both will fail."""
        self.assertFalse(True)


@flaky
class ExampleFlakyTests(TestCase):
    _threshold = -1

    def test_flaky_thing_that_fails_then_succeeds(self):
        """
        Flaky will run this test twice.
        It will fail once and then succeed.
        """
        self._threshold += 1
        if self._threshold < 1:
            raise Exception("Threshold is not high enough.")
