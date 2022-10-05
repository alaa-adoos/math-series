def fibonacci(num):
    if num==0 or num==1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)   


def lucas(num):
    if num==0:
        return 2
    if num==1:
        return 1
    else :
        return lucas(num-1)+lucas(num-2)




def sum_series(num,a=0,b=1):
    if num==0:
        return a
    if num==1:
        return b
    else:
        return sum_series(num-1,a,b)+sum_series(num-2,a,b)









'''
fibonacci series 0, 1, 1, 2, 3, 5, 8, 13, ... 
lucas series 2, 1, 3, 4, 7, 11, 18, 29, ...
sum_series (num, 0,1) =>fibonacci base
sum_series (num,2,1)  => lucs base
otherwise
differnt series with argumets base 
3 4 7 11 18 29
'''