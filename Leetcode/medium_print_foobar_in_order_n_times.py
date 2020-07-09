# problem: https://leetcode.com/problems/print-foobar-alternately/

from threading import Lock, Thread, Event


def printFoo(): print('foo', end='')
def printBar(): print('bar', end='')


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self) -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()

    def bar(self) -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()


if __name__ == '__main__':
    fb = FooBar(10)
    tFoo = Thread(name='tFoo', target=fb.foo,)
    tBar = Thread(name='tBar', target=fb.bar,)
    tFoo.start()
    tBar.start()