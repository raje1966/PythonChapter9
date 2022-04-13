# #There are two different decorators.  Function decorators and class decorators.  More common are function decorators.  Sometimes, decorator is a function that takes another function as arguments and extends the behavior of that function without explicitly modifying it.  In other words, it allows it to add new functionality to an existing function.
# @mydecorator
# def dosomething():
#     pass

def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('End')
    return wrapper
@start_end_decorator
def print_name():
    print("Alex")

# print_name = start_end_decorator(print_name)
print_name()