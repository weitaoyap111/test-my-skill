"""
Next week's winning lottery numbers are 8 different numbers all in the range 11 to 99 inclusive
Three, and only three of them are prime numbers and the sum of these three is 265
Of the other 5, just two of them are even, and when these 2 are multiplied together they make 1332
The mean of the remaining 3 is 23
What are the eight winning lottery numbers?
"""


def get_list_prime(number, start=2):
    prime_list = []
    for x in range(start, number):
        if is_prime(x):
            prime_list.append(x)
    return prime_list
        

def is_prime(number):
    for i in range(2, number):
        if(number % i) == 0:
            return False
    return True


def increase_list(lists, max_value=21, start=0):
    max_length = len(lists)
    lists[max_length-1] += 1

    # check increment
    for x in range(max_length):
        if (lists[max_length-x-1] == max_value):
            lists[max_length-x-1] = start
            if(max_length-x-2) >= 0:
                lists[max_length-x-2] += 1
            else:
                lists.insert(0, 1)
    return lists

def multi_lists(lists):
    """
    all_even_odd
    e - all must be even
    o - all must be odd
    i - ignore
    """
    multi_result = 1
    for x in lists:
        multi_result *= x
    return multi_result

def get_list(start, end, all_even_odd="e", ignore_list=[]):
    temp_list = []
    for x in range(start, end+1):
        skip = False
        if ignore_list:
            for y in ignore_list:
                if x == y:
                    skip = True
        if not skip:
            if all_even_odd == "e":
                if x % 2 == 0:
                    temp_list.append(x)
            elif all_even_odd == "o":
                if x % 2 == 1:
                    temp_list.append(x)
            else:
                temp_list.append(x)
    return temp_list

def check_not_same(lists):
    max_length = len(lists)
    for x in range(max_length-1):
        if(lists[x] == lists[x+1]):
            return True
    return False


def check_sum(lists, total=265, total_number=3, different_number=True, sort=True):
    temp_list = []
    if sort:
        lists.sort(reverse=True)
    max_length = len(lists)
    max_value = [max_length] * total_number
    count = 0
    new_number = []
    for x in range(total_number):
        new_number.append(count)
        if different_number:
            count += 1
    for x in range(total_number):
        temp_list.append(lists[x])
    while (total != sum(temp_list) and max_value != new_number or check_not_same(temp_list)):
        temp_list = []
        new_number = increase_list(new_number)
        for x in new_number:
            temp_list.append(lists[int(x)])
    return temp_list

def check_multi(lists, total=1332, total_number=2, different_number=True, sort=False):
    temp_list = []
    if sort:
        lists.sort(reverse=True)
    max_length = len(lists)
    max_value = [max_length] * total_number
    count = 0
    new_number = []
    for x in range(total_number):
        new_number.append(count)
        if different_number:
            count += 1
    for x in range(total_number):
        temp_list.append(lists[x])
    while (total != multi_lists(temp_list) and max_value != new_number or check_not_same(temp_list)):
        temp_list = []
        new_number = increase_list(new_number, len(lists))
        for x in new_number:
            temp_list.append(lists[int(x)])
    return temp_list

def check_mean(lists, total_number=3, total=23, different_number=True, sort=False):
    temp_list = []
    if sort:
        lists.sort(reverse=True)
    max_length = len(lists)
    max_value = [max_length] * total_number
    count = 0
    new_number = []
    for x in range(total_number):
        new_number.append(count)
        if different_number:
            count += 1
    for x in range(total_number):
        temp_list.append(lists[x])
    while (total*total_number != sum(temp_list) and max_value != new_number or check_not_same(temp_list)):
        temp_list = []
        new_number = increase_list(new_number, len(lists))
        for x in new_number:
            temp_list.append(lists[int(x)])

    return temp_list

final_list = []
prime_lists = get_list_prime(99, 11)
final_list.extend(check_sum(prime_lists))
final_list.extend(check_multi(get_list(11, 99, "e", prime_lists)))
final_list.extend(check_mean(get_list(11, 99, "o", prime_lists)))
print(final_list)
