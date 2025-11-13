#To demonstrate the itereable and itererato
# name="alex" # iterable
# iter1 =iter(name) #iterator
# print(next(iter1)) #just retrieving the first 3 characters
# print(dir(name))

#To demonstrate the iter() & next() method
# l=[1,2,3,4]
# it=iter(l)
# print(next(it)*10)
# print(next(it)*10)
# print(next(it)*10)

#To demonstrate the iter() & next() method
# l=[1,2,3,4]
# it=iter(l)
# j=0
# while(j < 4):
#     p=next(it)
#     if((p %2) == 0):
#         print(p*2)
#     else:
#         print(p)
#     j+=1

#To demonstrate iter & next in dictionary
# dict ={"babu":7, "robin":10, "lydia":7}
# gkey=iter(dict.keys())
# gval=iter(dict.values())
# print(next(gkey))
# print(next(gval))


#To demonstrate the exception StopIteration
# l=[1,2,3,4]
# it=iter(l)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("**Received the Stop Iteration exception**")
#         break

#To demonstrate the own iter and next method
#this code prints the even number and 'chosenit' for all odd number

# class Evenit:
#     def __init__(self, max=0):
#         self.max = max
#     def __iter__(self):
#         self.n = 0
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             self.n += 1
#             if self.n % 2 == 0:
#                 result = self.n
#                 return result
#             else:
#                 return 'chosenit'
#         else:
#             raise StopIteration
#
# numbers = Evenit(10) #created the object
# num_iter = iter(numbers)
# print(next(num_iter))
# print(next(num_iter))
# if "__next__" in dir(numbers):
#     print ("iter method present")
# else:
#     print("iter method not present")
#
# class CountUp:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration
#
# n=CountUp(5)
# n_iter=iter(n)
# print(next(n_iter))
# print(next(n_iter))
# print(next(n_iter))
# print(next(n_iter))
# print(next(n_iter))

# for i in n_iter:
#     print(i)

class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.num = 1   # start before the first prime

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        while self.num <= self.limit:
            if self.is_prime(self.num):
                result = self.num
                self.num += 1
                return result
            self.num += 1
        raise StopIteration

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True



primes = PrimeIterator(10)
it = iter(primes)
try:
    while True:
        print(next(it))
except StopIteration:
    print("End of prime numbers.")
