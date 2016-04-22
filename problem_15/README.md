# Lattice paths

Starting in the top left corner of a 2\*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

![lattice paths](http://i.imgur.com/PUl2FZc.gif)

How many such routes are there through a 20\*20 grid?


## Answer

Two solutions are provided in `main.py`: 

* A natural thinking will be using dynamic programming with the formula

```
path_num[i][j] = path_num[i-1][j] + path_num[i][j-1]
```

It works for small lattice, but quickly fails as lattice dimension goes larger if there is no cached value among recursive calls.

* An improved iterative solution is to use a matrix in which the value of an element is the number of paths going from the origin (0,0) to this point. After initializing the first row and first columns as 1's, the rest of matrix elements can be calculated quickly according to the formula above. The answer will be the value of the lower right corner element of the matrix. Size of 20 is done in a blink. 

* The "overview" pdf also gives three solutions with first two almost identical to those given above. The third is more of a mathematical approach using combinational math which only has O(N) time complexity. 
