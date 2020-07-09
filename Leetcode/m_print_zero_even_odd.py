# Problem: https://leetcode.com/problems/print-zero-even-odd/

from threading import Condition, Lock, Thread
import math

printNumber = lambda x: print(x)

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.lock = Lock()
        self.condition = Condition()

    def check_for_zero(self):
        return self.i % 2 == 0

    def check_for_even(self):
        #return self.i % 2 == 1
        return ((self.i - 1) / 2 % 2) == 1

    def check_for_odd(self):
        #return self.i % 2 == 1
        return ((self.i - 1) / 2 % 2) == 0

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self) -> None:
        for j in range(0, self.n):
            with self.condition:
                self.condition.wait_for(self.check_for_zero)
                self.i += 1
                printNumber(0)
                self.condition.notifyAll()

    def even(self) -> None:
        for j in range(0, math.floor(self.n / 2)):
            with self.condition:
                self.condition.wait_for(self.check_for_even)
                self.i += 1
                printNumber((j+1) * 2   )
                self.condition.notifyAll()

    def odd(self) -> None:
        for j in range(0, math.ceil(self.n / 2)):
            with self.condition:
                self.condition.wait_for(self.check_for_odd)
                self.i += 1
                printNumber((j+1) * 2 - 1)
                self.condition.notifyAll()



if __name__ == '__main__':
    zeo = ZeroEvenOdd(n=10)
    zth = Thread(name='print_zero', target=zeo.zero)
    eth = Thread(name='print_even', target=zeo.even)
    oth = Thread(name='print_odd', target=zeo.odd)
    zth.start()
    eth.start()
    oth.start()

