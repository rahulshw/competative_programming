# problem: https://leetcode.com/problems/print-foobar-alternately/

from greenlet import greenlet


def printFoo(): print('foo', end='')
def printBar(): print('bar', end='')


class FooBar:
    def __init__(self, n):
        self.n = n

    def foo(self) -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            gBar.switch()

    def bar(self) -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            gFoo.switch()


if __name__ == '__main__':
    fb = FooBar(10)
    gFoo = greenlet(fb.foo)
    gBar = greenlet(fb.bar)
    gFoo.switch()