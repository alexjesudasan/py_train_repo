# from collections import Counter
# #question #1
word_counts={}
f=open("chosen.txt",'r+')
content=f.read()
words=content.split()
f.close()
for w in words:
    word_counts[w]=word_counts.get(w,0)+1
print(word_counts)

# word_counts=Counter(words)
# print(word_counts)
# for word, count in word_counts.items():
#         print("{word}: {count}")