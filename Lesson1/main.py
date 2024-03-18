
# for i in range(0,30):
#     print("Hello, world! Step %d" % i)

#
# for i in range(0, 10):
#     print("Iteration number ", end="->")
#     print(" ", i, end="\n")
#
#

d = True

a = [1 , d , 3]
print(id(a))
print(id(a * 3))
print(id(a))
print(a)
print(True in a)
print([1] + [2] + [True] * 3 + ["abc"])
sorted(a, reverse=True)
print(a[-1])

#######################################
# Оператор * используеться для упаковки и распаковки итерируемых объектов
# * Оператор args используеться для распаковки кортежей, списков, строк, множеств
# ** Оператор Kwargs используеться для распаковки словарей

# распаковываеться так:

lst = [60, 50, 200]
print(*lst)
# 60, 50, 200

#  упаковываеться с помощью * следующим образом:

lst = [60, 50, 2000, 4000, 8000]
x, y, *numbers = lst
print(x, y, numbers)
# 60 50 [2000, 4000, 8000]







# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
a = "test"
b = "test"
print(id(a), id(b))