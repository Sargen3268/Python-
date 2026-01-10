def fib(n):
    #base case of recurssion 
    if(n==0 or n==1):
        return n
    else:
        return fib(n-2) + fib(n-1)
print(fib(4))


# n=0
# m = int(input("Enter a number: "))

# while(fib(n)<=m):
#     print(fib(n))
#     n=n+1

'''
i tried using while loop to print fibonacci series till a desired number 
it was a sucess
'''

