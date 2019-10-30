#we write a str and it is going to find the possibilities of words in the word list.
l=["dog","deer","deal"]
s=input()
result=set()
for i in l:
  if i.startswith(s):
    result.add(i)
print(result)
