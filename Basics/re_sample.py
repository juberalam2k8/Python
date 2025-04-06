import re

text = "I have many things in my plate, can you please try to take it up to to 3 and 5 and 3 25operate2"
pattern = r"\d+"

match=re.findall(pattern,text)

if match:
    print(f"pattern matched : {match}")
    count = len(match)
    print(f"count of digit is : {count}")

else:
    print("no match")


file= "test.txt"

with open(file,'r') as f:
    content=f.read()
print(content)


modified_file= re.sub(pattern,"",content)
with open(file,'w') as f:
    f.write(modified_file)

print("pattern removed")
  