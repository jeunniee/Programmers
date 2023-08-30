import re
def solution(my_string):
    answer=re.sub(r'[^0-9]', '', my_string)
    return sum(list(map(int,answer)))