def helper(_24, mini):
    if _24 == 0:
        return "12", mini, "AM"
    elif _24 < 12:
        return str(_24), mini, "AM"
    elif _24 == 12:
        return "12", mini, "PM"
    else:
        return str(_24 - 12), mini, "PM"


for _ in range(int(input())):
 
    time_24 = input().strip().split(':')
    _24 = int(time_24[0])
    mini = time_24[1]


    hour_12, mini, period = helper(_24, mini)


    print(f"{hour_12.zfill(2)}:{mini} {period}")
