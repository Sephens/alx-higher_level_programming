#!/usr/bin/python3
for n in range(0, 8):
    for k in range(n + 1, 10):
        print("{:d}{:d}".format(n, k), end=', ')
print("{:d}{:d}".format(n + 1, k))
