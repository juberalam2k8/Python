
list1=[1, 2, 4, 5, 8, 8, 9, 2, 1, 1]
print(f"Original list is : {list1}")

occurence={}

for num in list1:
    if num in occurence:
        occurence[num] +=1
    else:
        occurence[num]=1

print(f"count of each element is : {occurence}")
