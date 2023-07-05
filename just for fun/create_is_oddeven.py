text = "number = input(\"Enter a decimal number> \")"
max_value = 260

with open("odd_even.py", "w+") as f:
    f.write(text)
    for x in range(0, max_value+1):
        if x == 0:
            text2 = "\nif number == \"%s\": \n" % x
        else:
            text2 = "\nelif number == \"%s\": \n" % x
        text2 += "\tprint(\"%s\")" % ("Even" if x % 2 == 0 else "Odd")
        f.write(text2)
    print("done")
