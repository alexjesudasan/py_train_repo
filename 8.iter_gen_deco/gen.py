def countdown_gen(x):
    count=x
    while count>0:
        yield count
        count -=1

cnt=countdown_gen(5)
g_iter=iter(cnt)
print(next(g_iter))
print(next(g_iter))
print(next(g_iter))
print(next(g_iter))

# Also use for loop to invoke the iterator
# for g in countdown_gen(5):
#     print(g)


