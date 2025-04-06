import re
from datetime import datetime

content_file = "test.txt"
pattern = "test"

def find_pat(cnt,pat):

    search_pat = re.findall(pat,content)
    count = len(search_pat)

    print(f"Pattern that occured is {pat} and its occurence is {count}")


def include_timestamp(cnt,pat):
    current_date = datetime.now()
    modified_file=re.sub(pat,f"{current_date}:{pat}",cnt)
    with open(content_file,'w') as f:
        f.write(modified_file)


with open(content_file,'r') as f:
    content = f.read()
    
find_pat(content,pattern)
include_timestamp(content,pattern)