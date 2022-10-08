def fibonacci(num): #fibonacci series function
    if num==0 or num==1:#base case acts as the exit condition of the recursion
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)#use recursion 


def lucas(num): #lucas series function
    if num==0:#base case acts as the exit condition of the recursion
        return 2
    if num==1:#base case acts as the exit condition of the recursion
        return 1 
    else :
        return lucas(num-1)+lucas(num-2) #use recursion 




def sum_series(num,a=0,b=1):#math series function to  calc the series depend on the  base case 
    if num==0:#base case acts as the exit condition of the recursion
        return a
    if num==1:#base case acts as the exit condition of the recursion
        return b
    else:
        return sum_series(num-1,a,b)+sum_series(num-2,a,b)#use recursion 







