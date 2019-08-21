jobs = [[0, 3], [1, 9], [2, 6]]

a = sorted(jobs, key=lambda x : x[1] - x[0])
print(a)