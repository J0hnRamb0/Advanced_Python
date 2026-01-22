



def sum_number(n):
    if n == 0:          
        return 0

    return n + sum_number(n - 1)   
n = 5
print(sum_number(n))