def decorator(fun):
    def wrapper():
        print("I am about to print hello")
        fun()
        print("I have printed hello")
    return wrapper

def say_hello():
    print("Hello, World!")
    
#say_hello()
f=decorator(say_hello)
f()