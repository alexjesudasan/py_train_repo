# def add_sprinkles(func):
#     def wrapper():
#         print("**Add Sprinkles**")
#         func()
#         # print("After function call")
#     return wrapper
#
# @add_sprinkles
# def get_ice_cream():
#     print("Here is your Ice cream")
# get_ice_cream()

#To demonstrate the decorator for logging a function call
def log_call(func):
    def wrapper(*args,**kwargs):
        # print(f"[LOG]: Args:{args}, Kwargs:{kwargs}")
        if args[0] > 5:
            result =func(*args,**kwargs)
            return result
        else:
            error="first parameter is lesser than 5"
            print(error)
            return
    return wrapper

@log_call
def add(a, b):
    print(a + b)

@log_call
def maxi(*nums):
    print(max(nums))

add(3,4)
add(43,20)
maxi(9,4,7,1)
# maxi(9,4,7,1)