import math

triangle_record = []

def get_result_c(a, b):
    c = math.sqrt(a**2 + b**2)
    return int(c) if c % 1 == 0 else -1

max_value = 1001
for x in range(1, max_value):
    flag = True
    for y in range(1, x):
        value = get_result_c(x, y)
        if value < max_value:
            if value != -1:
                if len(triangle_record) == 0:
                    triangle_record.append([x, y, value])
                else:
                    for count, c in enumerate(triangle_record):
                        if x % c[0] == 0 and y % c[1] == 0 and value % c[2] == 0:
                            flag = False
                            break
                    if flag:
                        triangle_record.append([x, y, value])

print("list of length(b, a, c):")
print(triangle_record)