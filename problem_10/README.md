# Summation of primes


The sum of the primes below 10 is

```
2 + 3 + 5 + 7 = 17.
```

Find the sum of all the primes below two million.

## Answer

It is natural to borrow the solution from Problem 7 ("10001st prime") for the purpose of finding prime numbers below an upper bound. But the upper bound of 2 million makes the program run slow. See `main.py` for the implementation. 

However, "overview" pdf doc gives a faster (and ancient) algorithm "[sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)" to find the prime numbers below a limit. The idea is to incrementally identify prime numbers starting from 2 by eliminating multiples of the already discovered prime numbers from the bag, given the fact that the next composite number can be written in form of the multiples of products of a subset of previously discovered prime numbers. The space complexity of this algorithm is O(N), but takes less time to compute. 

Follow-up question: compare the time and space complexities of those two approaches. 