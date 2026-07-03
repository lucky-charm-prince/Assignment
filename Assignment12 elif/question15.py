marks=38
attendance=80
internal=26
if marks>=40:
    if attendance>=75:
        if internal>=20:
            print("result")
        else:
            print("grace pass")
    else:
        print("result is detained")
else:
    if marks>=35:
        if internal>=25:
            print("result is Reappear ")
        else:
            print("fail")
