def cmp(a, b):
    if a > b : return 1
    if a == b : return 0
    return -1

N = int(input())
x_arr= [0] * N
y_arr= [0] * N
for i in range(N):
    x_arr[i], y_arr[i] =  map(int, input().split())

for i in range(N):   
    for j in range(i+1, N):        
        if cmp(x_arr[i], x_arr[j]) == 1:             
            x_arr[i], x_arr[j] = x_arr[j], x_arr[i]
            y_arr[i], y_arr[j] = y_arr[j], y_arr[i]            
        elif cmp(x_arr[i], x_arr[j]) == 0:
            if cmp(y_arr[i], y_arr[j]) == 1:
                x_arr[i], x_arr[j] = x_arr[j], x_arr[i]
                y_arr[i], y_arr[j] = y_arr[j], y_arr[i]
            else : continue
        else : continue

for i in range(N):
    print(x_arr[i], y_arr[i])
