# Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

```
a^2 + b^2 = c^2
```

For example, `3^2 + 4^2 = 9 + 16 = 25 = 5^2`.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


## Answer

Reduce equations

```
a^2 + b^2 = c^2
3^2 + 4^2 = 9 + 16 = 25 = 5^2
```

to 

```
1000^2 - 2000a - 2000b + 2ab = 0
```

which further leads to 


```
a = (500000 - 1000b) / (1000 -b)
```

And the goal is to solve the above equations with conditions

* a, b are both positive integers
* a, b are both smaller than 1000

The rest is to scan b from 1 to 999 and find the match with a simple script. 

See 'overview' pdf doc for another approach to this problem (parametrization of Pythagorean triplet). 