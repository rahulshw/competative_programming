# Problem: https://leetcode.com/problems/print-zero-even-odd/

from threading import Condition, Lock, Thread
import math

printNumber = lambda x: print(x)


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.odd_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock.acquire()
        self.even_lock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for j in range(0, self.n):
            self.zero_lock.acquire()
            printNumber(0)
            if j % 2 == 0:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for j in range(0, math.floor(self.n / 2)):
            self.even_lock.acquire()
            printNumber((j + 1) * 2)
            self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for j in range(0, math.ceil(self.n / 2)):
            self.odd_lock.acquire()
            printNumber((j + 1) * 2 - 1)
            self.zero_lock.release()


if __name__ == '__main__':
    zeo = ZeroEvenOdd(n=10)
    zth = Thread(name='print_zero', target=zeo.zero)
    eth = Thread(name='print_even', target=zeo.even)
    oth = Thread(name='print_odd', target=zeo.odd)
    zth.start()
    eth.start()
    oth.start()

