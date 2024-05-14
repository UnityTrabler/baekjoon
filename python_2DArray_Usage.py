N = 4

x_arr = [[0] * 2 for i in range(N)]
y_arr = [[0 for j in range(4)] for i in range(4)]

x_arr[0][1] = 33
y_arr[0][1] = 33

print(x_arr)
print(y_arr)