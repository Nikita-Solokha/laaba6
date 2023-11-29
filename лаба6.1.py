s0 = input("Введите строку s0: ")
s = input("Введите строку s: ")
count = 0
i = 0
while i < len(s0):
    if s0[i:i+len(s)] == s:
        count += 1
        i += len(s)
    else:
        i += 1
print(f"Количество вхождений строки {'s0'} в строку {'s'} :" + str(count))

