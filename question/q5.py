import math
number_to_eng_list = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    100: "one hundred",
    1000: "one thousand",
}

def get_all_number(number, lists=number_to_eng_list):
    try:
        return lists[number]
    except:
        return less_10k_number_conv(number)

def less_hundred_number_conv(number, lists=number_to_eng_list):

    if 14 <= number < 20: # 14~19
        return lists[number % 10] + "teen"
    if number < 100:
        get_1st_digits = number % 10
        if number < 14:
            return lists[number]
        elif 14 <= number < 60:
            get_2nd_digits = math.floor(number/10) * 10
            return lists[get_2nd_digits] + ("-" + lists[get_1st_digits] if get_1st_digits != 0 else "")
        else:
            get_2nd_digits = (number - (number % 10)) / 10
            return lists[get_2nd_digits] + ("t" if get_2nd_digits != 8 else "") + "y" + ("-" + lists[get_1st_digits] if get_1st_digits != 0 else "")

def less_thousand_number_conv(number, lists=number_to_eng_list):
    if number < 100:
        return less_hundred_number_conv(number)
    else:
        get_3rd_digits = math.floor((number - (number % 100)) / 100)
        get_last_2_digits = number - get_3rd_digits * 100
        return lists[get_3rd_digits] + " hundred" + (" and " + less_hundred_number_conv(get_last_2_digits) if get_last_2_digits != 0 else "")

def less_10k_number_conv(number, lists=number_to_eng_list):
    if number < 1000:
        return less_thousand_number_conv(number)
    else:
        get_4th_digits = math.floor((number - (number % 1000)) / 1000)
        get_last_3_digits = number - get_4th_digits * 1000
        return lists[get_4th_digits] + " thousand" + (" " + less_thousand_number_conv(get_last_3_digits) if get_last_3_digits != 0 else "")

for x in range(0, 10000):
    print(str(x) + ": " + get_all_number(x))