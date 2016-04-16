# Smallest multiple


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Answer

Since 20 is a small number, scanning from 1~20 will be enough

```
2*3*5*7*2*2*3*11*13*2*17*19 = 232792560
```

To solve it programmatically, a generic algorithm is

```
product = 1

for i in 2 to N:
    is product divisible by i? 
        if yes -> continue
        if not -> product = least_common_multiple(i, product) 

return product
```

The "overview" pdf doc has another algorithm which is better than the one above. The idea is that every integer can be written as the product of prime number with certain power. The problem become to find the largest power of each prime number so that p^n <= 20. In this case, it becomes

```
2^4 * 3^2 * 5* 7 * 11 * 13* 17 *19
```

For this algorithm to work, the key is to find the series of prime numbers smaller than N (here N=20). 
