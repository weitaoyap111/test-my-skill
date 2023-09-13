from pprint import pprint

triangle_record = []


def get_result_c(a, b):
    result = (a * a + b * b) ** 0.5
    return int(result) if result % 1 == 0 else -1


max_value = 1000
for x in range(1, max_value + 1):
    for y in range(x, max_value + 1):
        flag = True
        value = get_result_c(x, y)
        if value < max_value and value != -1:
            if len(triangle_record) == 0:
                triangle_record.append([x, y, value, 1])
            else:
                count = 0
                for count, c in enumerate(triangle_record):
                    if x / c[0] == y / c[1]:
                        flag = False
                        break
                if flag:
                    triangle_record.append([x, y, value, count+2])

print("list of length(a, b, c):")
pprint(len(triangle_record))
