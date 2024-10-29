import datetime
import unittest
import signal
import sys
from time import perf_counter, time_ns

from clock_time import sleep, time_s

class ClockTimeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.SECS = (0.2, 1, 1.5)
        cls.SIGNAL_SEC = 2
        cls.SIGNAL_ALARM = 1
        print('(please wait %.2f seconds)' % \
              (sum(cls.SECS) + cls.SIGNAL_SEC))

    def test_sleep_arg_type(self):
        with self.assertRaises(TypeError):
            sleep()
        with self.assertRaises(TypeError):
            sleep(1, 2)
        with self.assertRaises(ValueError):
            sleep('a')
        with self.assertRaises(ValueError):
            sleep(b'a')
        with self.assertRaises(ValueError):
            sleep(('a',))
        with self.assertRaises(ValueError):
            sleep(['a',])

    def test_sleep_arg_range(self):
        # int
        with self.assertRaises(ValueError):
            sleep(-1)
        with self.assertRaises(ValueError):
            sleep(2**63)
        # float
        with self.assertRaises(ValueError):
            sleep(-1.1)
        with self.assertRaises(ValueError):
            sleep(-1e-9)
        with self.assertRaises(ValueError):
            sleep(float('nan'))
        with self.assertRaises(ValueError):
            sleep(sys.float_info.max)
        with self.assertRaises(ValueError):
            sleep(9.3e+9)

    def test_sleep_0(self):
        sleep(0)
        sleep(-0)
        sleep(0.0)
        sleep(-0.0)

        # not 0, but very small.
        sleep(0.000_000_000_001)
        sleep(0.000_000_000_01)
        sleep(0.000_000_000_1)
        sleep(0.000_000_001)
        sleep(0.000_001)
        sleep(0.001)

    def _check_time_s(self):
        s1 = time_s()
        s2 = time_ns() // 1_000_000_000

        # after year 2262 April 11th, s2 will overflow
        # in CPython v3.14.0a1 implementation.
        if datetime.datetime.now().year < 2262:
            self.assertLessEqual(abs(s1-s2), 1)

    def _check_proximal(self, a, b):
        if a > b:
            big, small = a, b
        else:
            big, small = b, a
        ratio = big / small
        self.assertLessEqual(
                ratio, 1.2,
                ('There is a significant difference between '
                 'sleep time and measured time, may be '
                 'due to unstable testing environment.'))

    def test_sleep(self):
        self._check_time_s()

        for sec in self.SECS:
            t1 = perf_counter()
            sleep(sec)
            delta = perf_counter() - t1

            self._check_proximal(sec, delta)
            self._check_time_s()

    def test_signal(self):
        # doc: If the sleep is interrupted by a signal and
        # no exception is raised by the signal handler,
        # the sleep is restarted with a recomputed timeout.
        def handle_alarm(signal, frame):
            pass
        signal.signal(signal.SIGALRM, handle_alarm)

        signal.alarm(self.SIGNAL_ALARM)
        t1 = perf_counter()
        sleep(self.SIGNAL_SEC)
        delta = perf_counter() - t1

        self._check_proximal(self.SIGNAL_SEC, delta)
        self._check_time_s()

    def test_time_s(self):
        with self.assertRaises(TypeError):
            time_s(1)
        with self.assertRaises(TypeError):
            time_s(1, 2)
        self.assertEqual(type(time_s()), int)

if __name__ == "__main__":
    unittest.main()
