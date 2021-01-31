import statistics
num_of_vals = int(input())
vals = list(map(int,input().split()))
freqs = list(map(int,input().split()))

arr = []
for i in range(num_of_vals):
    arr += [vals[i]] * freqs[i]

sorted_arr = sorted(arr)
median = statistics.median(sorted_arr)
arr_L = [val for val in sorted_arr if val < median]
arr_H = [val for val in sorted_arr if val > median]

median_L = statistics.median(arr_L)
median_H = statistics.median(arr_H)

print (round(float(median_H-median_L), 1))
