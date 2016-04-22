# README

This is my take on [Project Euler](https://projecteuler.net).

I just do it for fun, and don't claim the copyright for questions and so on. There are some amazing solutions on Project Euler's forums. 

To update `README_all.md`, do:

```
cd scripts
python readme_aggregator.py
```

## Some general thoughts

* If a recursive solution is too slow or too memory hungry, add a caching mechanism among recursive calls, such a hash table, list, etc.. 

* Think about using Python generators when dealing with large-scale problem that don't need to track a global history. 
