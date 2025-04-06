import re
from datetime import datetime

temp_file="file.tmp"
replace="warning|error"
replace_with="DEBUG"

def add_timestamp(file):
    current_time=datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    
    with open(file,'r') as read_file, open(temp_file,'w') as write_file:
        for line in read_file:
            modified_contnent=re.sub(f"{replace}",f"{replace_with}",line)
            write_file.write(f"{current_time}:{modified_contnent}")

add_timestamp("test.txt")