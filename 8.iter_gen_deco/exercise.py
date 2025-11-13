# class EvennumIter():
#     def __init__(self,numbers):
#         self.numbers=numbers
#         self.index=0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while (self.index < len(self.numbers)):
#             current = self.numbers[self.index]
#             self.index+=1
#             if (current %2 ==0):
#                 return current
#         raise StopIteration
#
# nums=EvennumIter(range(10))
# for num in nums:
#     print(num)

#Iterator to filter items based on the cost value from a dictionary
# class filter_items:
#     def __init__(self,data):
#         self.data=data
#         self.iterator=iter(self.data.items())
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             item, cost = next(self.iterator)
#             if cost >= 5:
#                 return (item,cost)
#             else:
#                 print(f"{item} is less than 5 rupees")
#         return StopIteration
#
# items = { 'apple': 4, 'banana': 6, 'chocolate': 3, 'milk': 5,'gum': 2}
# objects=filter_items(items)
# for i in objects:
#     print(i)

#generator to print only the even numbers
def prime_num(num):
    i=1
    while i< num:
        if i%2 == 0:
            yield i
        i+=1

g_iter=prime_num(10)
print(next(g_iter))
print(next(g_iter))
