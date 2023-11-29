nomers = []
a = int(input("Введите количество элементов списка: "))
for i in range(a):
    nomer = float(input("Введите элемент списка: "))
    nomers.append(nomer)
a = 0
b = 0
for nomer in nomers:
    if nomer > 0:
        b += 1
        if b == 2:
            break
    elif b == 1:
        a += nomer
print("Сумма элементов списка между первым и вторым положительными элементами:", a)
zero_count = 0
for i in range(len(nomers)):
    if nomers[i] != 0:
        nomers[zero_count] = nomers[i]
        zero_count += 1
for i in range(zero_count, len(nomers)):
    nomers[i] = 0
print("Получившийся список:", nomers)



