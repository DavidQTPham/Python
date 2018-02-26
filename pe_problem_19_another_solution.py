Y = 1901
M = 1
counter = 0
days = 2
while Y < 2001:
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12 :
        days += 31
    elif  M == 4 or M == 6 or M == 9 or M == 11:
        days += 30
    elif M == 2:
        if Y % 100 == 0:
            if Y % 400 == 0:
                days += 29
            else:
                days += 28
        elif Y % 4 == 0:
            days += 29
        else:
            days += 28

    if days % 7 == 0:
        counter += 1

    M += 1
    if M > 12:
        Y += 1
        M = 1

print counter


~

