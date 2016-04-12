"""
Still pretty straightward. I use a Python generator for a twist. 
"""

# Create a Python generator to produce Fibonacci series
def fib_gen(n_max):
    fib1 = 0
    fib2 = 1
    while 1:
        fib_next = fib1 + fib2
        if fib_next > n_max:
            # Terminate generator
            break
        else:
            yield fib_next
            fib1 = fib2
            fib2 = fib_next
    # Generator is terminated when this function ends


if __name__ == "__main__":
    s = 0
    for i in fib_gen(4000000):
        if i % 2 == 0:
            s += i
    print s

