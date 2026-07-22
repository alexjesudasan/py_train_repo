import os
#To exclusively create a file
name='alex'
f=open("e:/greet.txt", 'x')
f.write(f"Good Morning !! {name}")
f.close()

os.remove('e:/greet.txt')

# To open the file in read and update mode
f=open("hello.txt", 'r+')
f.write('hello world')
print(f"cursor position after write :{f.tell()}")
f.seek(0)
print(f"cursor position after seek :{f.tell()}")
print(f.read(3))
print(f"cursor position after read : {f.tell()}")
print(f.read(3))
print(f"cursor position after read : {f.tell()}")
f.seek(0)
print("truncate :",f.truncate(5))
print(f"file content after truncate : {f.read()}")
f.close()

# To open the file in read mode
f = open("hello.txt", 'r')
print(f.read())
f.close()
