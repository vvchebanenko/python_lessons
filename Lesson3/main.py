a = 15
b = 10

print(f"A+B = {a+b: 15}, b={b}")

print("a is b")
print(a is b)

print("a is not b")
print(a is not b)

print("test in betatesting")
print("test" in "betatesting") # поиск чего-то в чём-то, работает для строк, списков и словарей (ищет в списке ключей)

# Тернарные операторы
x = 0
if x == 0: print("Ноль")

print("Ноль") if x == 0 else print("Не ноль")

val = 30
a = 1 if val > 50 else 0
print(a)


# Что будет ?
l = 51
s = ("Не любит", "Любит")[l > 50] # Работает потому что в [ x > y ] превращаеться в логическое врыжение, которые будет 1 или 0, дальше слайсинг
print(s)


test_string = "three"
match test_string:
    case "one":
        print("Введено one")
    case "two":
        print("Введено two")
    case "three" | "four":
        print("Введено three or four")
    case _:
        print("Введено что-то ещё")

# Цикл While
x = 0
while x < 100:
    print("x = %d" % x )
    x = x + 1
else:
    print("Конец цикла")

# Тоже самое но короче
while x < 100 : x = x + 1; print("x = %d" % x) # Так тоже можно он понимает ; в одну строку




print(list(range(0, 20))) # range возвращает итерируемый объект

# итератор ( генератор ) отрабатывает только 1 РАЗ!!!! и после нужно пересоздавать
gen = (x*x*x for x in range(0,10))
print("type(gen)")
print(type(gen))

for _ in gen:
    print(_)
# этот уже не отработает
for _ in gen:
    print(_)


# функция генератор yield !!!!

def fib(n):
    a, b = 1, 1

    step = 0
    while step < n:
        yield a
        b, a = a + b, b
        step += 1

def fibr(n):...
...

for i in fib(50):
    print(i)