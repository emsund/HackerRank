n = input()
d = input().strip().split(" ")
d = [int(i) for i in d]
d.sort()

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
    

split_ret_middle(d, q)
q[0],q[1] = q[1],q[0]
for i in q:
    print(int(i))
