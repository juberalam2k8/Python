var = [1, 2, 3, 4, 5]

print(var)

try:
    for v in var[10]:
        if 8 in var:
            print(v)
except Exception as e:
    print(f"exception is: {e}")