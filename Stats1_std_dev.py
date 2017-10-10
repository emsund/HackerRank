n = int(input().strip())
ar = [int(x) for x in (input().strip().split(" "))]

mean = sum(ar)/n
var = sum([(x-mean)**2 for x in ar])/n
stddev = round(float(var**0.5), 1)

print(stddev)
