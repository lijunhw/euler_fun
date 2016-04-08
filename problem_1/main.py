

def multiple_35(n_max): 
    s = 0
    for i in range(n_max):  # doesn't include n_max itself
        if ((i % 3) == 0) or ((i % 5) ==0):
            s += i
    return s

if __name__ == "__main__":
    print multiple_35(1000)

