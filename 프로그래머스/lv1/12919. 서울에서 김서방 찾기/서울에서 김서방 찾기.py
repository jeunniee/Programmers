def solution(seoul):
    a = [i for i in range(len(seoul)) if seoul[i]=="Kim"]
    return f"김서방은 {a[0]}에 있다"
       
        