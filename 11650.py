
N = int(input())
x_arr = [[0] * 2 for i in range(N)]

# for i in range(N):
#     x_arr[i][0], x_arr[i][1] =  map(int, input().split())
#     print("x = ",x_arr[i][0], "y =",x_arr[i][1])
#     print("i = ", i)
x_arr[0][1] = 33
y_arr[0][1] = 33

# for i in range(N):   
#     for j in range(i+1, N):        
#         if cmp(x_arr[i], x_arr[j]) == 1:             
#             x_arr[i], x_arr[j] = x_arr[j], x_arr[i]
#             y_arr[i], y_arr[j] = y_arr[j], y_arr[i]            
#         elif cmp(x_arr[i], x_arr[j]) == 0:
#             if cmp(y_arr[i], y_arr[j]) == 1:
#                 x_arr[i], x_arr[j] = x_arr[j], x_arr[i]
#                 y_arr[i], y_arr[j] = y_arr[j], y_arr[i]
#             else : continue
#         else : continue
print(x_arr)
print(y_arr)

# for i in range(N):
#     print(x_arr[i][0], x_arr[i][1])