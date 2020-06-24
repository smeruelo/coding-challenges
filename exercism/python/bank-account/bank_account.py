# https://exercism.io/my/solutions/0b7f208dbb324407a5174197321878b1

from threading import Lock


class BankAccount:
    def __init__(self):
        self._balance = 0
        self._is_opened = False
        self._lock = Lock()

    def is_opened(f):
        def wrapped(self, *args):
            if not self._is_opened:
                raise ValueError("Account is not opened.")
            return f(self, *args)
        return wrapped

    def mutex(f):
        def wrapped(self, *args):
            with self._lock:
                return f(self, *args)
        return wrapped

    @is_opened
    @mutex
    def get_balance(self) -> int:
        return self._balance

    @mutex
    def open(self) -> None:
        if self._is_opened:
            raise ValueError("Account is already opened.")
        self._balance = 0
        self._is_opened = True

    @is_opened
    @mutex
    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        self._balance += amount

    @is_opened
    @mutex
    def withdraw(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        if amount > self._balance:
            raise ValueError("There is not enough money in account.")
        self._balance -= amount

    @is_opened
    @mutex
    def close(self) -> None:
        self._is_opened = False
