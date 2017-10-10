n = input()
x = [int(i) for i in (input().strip().split(" "))]
w = [int(i) for i in (input().strip().split(" "))]

print(round((sum([x[i]*w[i] for i in range(len(x))])/sum(w)), 1))
