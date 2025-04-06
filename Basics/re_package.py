import re
from datetime import datetime

text=""
pattern=""
def identify_pattern_from_text(text,pattern):
    content=re.findall(pattern,text)
    return content

def user_input():
    t=input("Please enter the text\n")
    p=input("enter the keyword you're looking for\n")
    return (t,p)


text, pattern=user_input()
matches = identify_pattern_from_text(text,pattern)
count = len(matches)

if matches:
    print(f"its a match and the match count is {count}")
else:
    print("not matching")


content_file = "test.txt"
search = "warning"
current_date=datetime.now()

with open(content_file,'r') as g:
    content=g.read()

modified_content=re.sub(search,f"{current_date}:{search}\n",content)

with open(content_file,'w') as f:
        f.write(modified_content)

print(modified_content)

content_file="test.txt"
pattern="test"

with open(content_file,'r') as f:
    content=f.read()

count= re.findall(pattern,content)
count=len(count)

print(count)











