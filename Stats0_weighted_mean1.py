def weighted_mean(values, weights):
    
    numer, denom = (0, 0)
    
    for i in range(len(values)):
        numer += values[i]*weights[i]
        denom += weights[i]
        
    return numer/denom
  
    
n = int(input().strip())
x = [int(i) for i in (input().strip().split(" "))]
w = [int(i) for i in (input().strip().split(" "))]

mean = weighted_mean(x, w)
mean = round(mean, 1)
print(mean)
