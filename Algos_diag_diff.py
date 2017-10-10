#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diag_1 = 0
diag_2 = 0

for i in range(n):
    diag_1 += a[i][i]
    diag_2 += a[i][n-i-1]
    
abs_diff_of_sums = abs(diag_1 - diag_2)
print(abs_diff_of_sums)
