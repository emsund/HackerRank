n = int(input().strip())
x = [int(i) for i in input().strip().split(" ")]
f = [int(i) for i in input().strip().split(" ")]
s = []

for i in range(n):
    s += ([x[i]]*f[i])

s.sort()
q = []

def split_ret_middle(data, quartile, remaining_splits=2):
    ''' split a given list into two, find and return middle. recurse'''
    if remaining_splits == 0:
        return 1
    else:
        n = len(data)
        h1 = data[0:int(n/2)]
        h2 = data[int(n/2):n]

        if n%2 != 0:
            # if odd, remove middle element and return it
            middle_value = h2.pop(0)
        else:
            # if even, take mean of two middle elements
            middle_value = (h1[-1]+h2[0])/2

        q.append(middle_value)
        split_ret_middle(h1, quartile, remaining_splits - 1)
        split_ret_middle(h2, quartile, remaining_splits - 1)
        return 0
    

split_ret_middle(s, q)
q[0],q[1] = q[1],q[0]
iqr = round(float(q[2]-q[0]), 1)
print(iqr)
