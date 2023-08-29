def solution(num):
    n=0
    while num != 1 & n<=500:
        if num ==1:
            break
        elif num % 2==0:
             num/=2
        else:
            num=num*3+1
        n+=1
    if n >=500:
        return -1
    else:
        return n