
### 1.1.1. A first recursive attempt
# fib1 is not functional due to the recursive error.
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

### 1.1.2. Utilizing base cases
# fib2 is not efficient. There are 15 calls required to compute element 5, 177 calls to
# compute element 10, and 21,891 calls to compute element 20.
def fib2(n: int) -> int:
# I remember having something like this in the joplin python module I was writing.
# This would have helped my understanding.
  if n < 2:
    return n
  return fib2(n-1) + fib2(n-2)


### 1.1.3. Memoization to the rescue
# Todo (Rasul): add to anki
# Memoization is a technique in which you store the results of computational tasks when they
# are completed so that when you need them again, you can look them up instead of needing to
# compute them a second (or millionth) time
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1} # our base cases

def fib3(n: int) -> int:
  if n not in memo:
    memo[n] = fib3(n-1) + fib3(n-2)
  return memo[n]

### 1.1.4. Automatic memoization
# Python has a built-in decorator for memoizing any function automagically.
# The decorator @functools.lru_cache()
from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # same definition as fib2()
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case


### 1.1.5. Keep it simple, Fibonacci
# Remember, any problem that can be solved recursively can also be solved iteratively.
def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

### 1.1.6. Generating Fibonacci numbers with a generator

from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
  yield 0
  if n > 0 : yield 1

  last: int = 0
  next: int = 1  # initially
  for _ in range(1, n):
    last, next = next, last + next
    yield next

if __name__ == "__main__":
    for i in fib6(50):
        print(i)