from threading import Lock


class BankAccount:
    def __init__(self):
        self._balance = 0
        self._is_opened = False
        self._lock = Lock()

    def get_balance(self) -> int:
        with self._lock:
            if not self._is_opened:
                raise ValueError("Account is not opened.")
            return self._balance

    def open(self) -> None:
        with self._lock:
            if self._is_opened:
                raise ValueError("Account is already opened.")
            self._balance = 0
            self._is_opened = True

    def deposit(self, amount: int) -> None:
        with self._lock:
            if not self._is_opened:
                raise ValueError("Account is not opened.")
            if amount < 0:
                raise ValueError("Amount must be a positive number.")
            self._balance += amount

    def withdraw(self, amount: int) -> None:
        with self._lock:
            if not self._is_opened:
                raise ValueError("Account is not opened.")
            if amount < 0:
                raise ValueError("Amount must be a positive number.")
            if amount > self._balance:
                raise ValueError("There is not enough money in account.")
            self._balance -= amount

    def close(self) -> None:
        with self._lock:
            if not self._is_opened:
                raise ValueError("Account is already closed.")
            self._is_opened = False
