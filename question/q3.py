text = "danfaytnidrh42 gd2bt 99."
# "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
# "0123456789":

index = 0
message = ""
while True:
    next_flag = False
    temp = text[index]
    if temp in "0123456789" and not next_flag:
        index -= int(temp)
        next_flag = True

    elif temp == "." and not next_flag:
        break

    if not next_flag:
        message += temp

    if not next_flag:
        if temp == " ":
            index -= 13
        else:
            index += ord(temp) % 16

print(message)
