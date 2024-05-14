def solution(n):
    for i in range((len(n) + 1) // 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True

while(1):
    n = input()
    if n == '0' : break
    print("yes" if solution(n) else "no")