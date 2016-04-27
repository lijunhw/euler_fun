# Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,

and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

## Answer

Note that factors of 2\*5 don't contribute to the sum of digits. Take care of the rest with num list multiplication trick as described previous (e.g., Problem 16). This makes no assumption of the length of factorial number thus the program can take in a large number.

The implementation in `main.py` is a little clumsy, but shows the full thinking process. Alternatively, one can simply use the built-in factorial function like math.factorial(). Some concise solution utilizing the power of Python is like 

```
import math
print reduce(lambda acc,x: acc + int(x), str(math.factorial(100)), 0)
```
