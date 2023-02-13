for i in range(3):
    res_list = []
    try:
        result = 10 /i
        print(result)
        res_list.append(result)
    except ZeroDivisionError:
        print("Not divided by 0")