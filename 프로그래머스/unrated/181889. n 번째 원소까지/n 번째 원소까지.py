def solution(num_list, n):
    if n==1:
        return [num_list[n-1]]
    else:
        for i in range(0,n-1):
            return num_list[i:n]
        
            
    