#decorator with argument

def repeat(n):
        def decorator(fun):
                def wrapper(a):
                        for i in range(n):
                                fun(a)
                return wrapper
        return decorator

@repeat(5)

def say_hello(a):
        print("Hello ",a)
say_hello("Chinmay")