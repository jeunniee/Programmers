def solution(numbers):
    n=sorted(numbers, reverse=True)
    if n[0]*n[1]>n[len(n)-1]*n[len(n)-2]:
        return n[0]*n[1]
    else:
        return n[len(n)-1]*n[len(n)-2]
    
        