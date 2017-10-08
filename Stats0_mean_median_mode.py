def find_mean(numbers):
    ''' Accepts a list of integers, and returns the mean (average)'''
    mean = sum(numbers)/len(numbers)
    return mean


def find_median(numbers):
    ''' Accepts a list of integers, and returns the median'''
    numbers = sorted(numbers)
    n = len(numbers)
    i = int(n/2)
    
    if n % 2 != 0:
        # odd number of elements; just use middle one
        median = numbers[i]
    else:
        # even number of elements; average middle one
        a = numbers[i - 1]
        b = numbers[i]
        median = find_mean([a,b])
       
    return median


def find_mode(numbers):
    ''' Accepts a list of integers, and returns the smallest mode.'''
    freqs = {}
    for x in numbers:
        if x in freqs.keys():
            freqs[x] += 1
        else:
            freqs[x] = 1

    max_occur = max(freqs.values())
    
    modes = []

    for num, occ in freqs.items():
        if occ == max_occur:
            modes.append(num)

    return min(modes)
            
    
input_n = int(input().strip())
input_list = input().strip().split(" ")
input_list = [int(i) for i in input_list]

print(find_mean(input_list))
print(find_median(input_list))
print(find_mode(input_list))
