from threading import Lock, Thread


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_lock = Lock()
        self.buzz_lock = Lock()
        self.fizzbuzz_lock = Lock()
        self.number_lock = Lock()
        self.fizz_lock.acquire()
        self.buzz_lock.acquire()
        self.fizzbuzz_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(0, self.n // 3 - self.n//15):
            self.fizz_lock.acquire()
            printFizz()
            self.number_lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(0, self.n // 5 - self.n//15):
            self.buzz_lock.acquire()
            printBuzz()
            self.number_lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(0, self.n//15):
            self.fizzbuzz_lock.acquire()
            printFizzBuzz()
            self.number_lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(0, self.n):
            self.number_lock.acquire()
            num = i + 1
            if num % 3 == 0 and num % 5 == 0:
                self.fizzbuzz_lock.release()
            elif num % 3 == 0:
                self.fizz_lock.release()
            elif num % 5 == 0:
                self.buzz_lock.release()
            else:
                printNumber(i + 1)
                self.number_lock.release()


if __name__ == '__main__':
    fb = FizzBuzz(16)
    targets = [
        (fb.fizz, lambda: print('fizz')),
        (fb.buzz, lambda: print('buzz')),
        (fb.fizzbuzz, lambda: print('fizzbuzz')),
        (fb.number, lambda x: print(x))
    ]
    for (target, print_fn) in targets:
        t = Thread(target=target, args=(print_fn,))
        t.start()