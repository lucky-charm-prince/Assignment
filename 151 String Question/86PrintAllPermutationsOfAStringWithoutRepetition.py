s = "ABC"

result = [""]

for ch in s:
    new_result = []
    
    for p in result:
        for i in range(len(p) + 1):
            new_result.append(p[:i] + ch + p[i:])

    result = new_result

for p in result:
    print(p)    