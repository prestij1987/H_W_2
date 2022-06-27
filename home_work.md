Кратко Секция статьи "Кратко"
Задачи после первой лекций. Требования к задачам:

Должны проходить все тесты;
Написаны без использования сторонних библиотек (можно внутренние, к примеру itertools);
Код соответствует PEP8.
Задача №1. Секция статьи "Задача №1."
Написать метод domain_name, который вернет домен из url адреса:

url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = "cnet"

Скопировать
Основа:

def domain_name(url):
  return

Скопировать
Для проверки:

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

Скопировать
Задача №2. Секция статьи "Задача №2."
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:

2149583361 -> "128.32.10.1"
32         -> "0.0.0.32"
0          -> "0.0.0.0"

Скопировать
Основа:

def int32_to_ip(int32):
  return

Скопировать
Для проверки:

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

Скопировать
Задача №3. Секция статьи "Задача №3."
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

Будьте осторожны 1000! имеет 2568 цифр.

Доп. инфо: http://mathworld.wolfram.com/Factorial.html

zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

Скопировать
Основа:

def zeros(n):
    return 0

Скопировать
Подсказка: вы не должны вычислять факториал.
Найдите другой способ найти количество нулей.

Для проверки:

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

Скопировать
Задача №4. Секция статьи "Задача №4."
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)

Input: bbananana

Output:

b-anana--
b-anan--a
b-ana--na
b-an--ana
b-a--nana
b---anana
-banana--
-banan--a
-bana--na
-ban--ana
-ba--nana
-b--anana

Скопировать
Основа:

def bananas(s) -> set:
    result = set()
    # Your code here!
    return result

Скопировать
Для проверки:

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

Скопировать
Задача №5. Секция статьи "Задача №5."
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

primesL = [2, 5, 7]
limit = 500
List of Numbers Under 500          Prime Factorization
___________________________________________________________
           70                         [2, 5, 7]
          140                         [2, 2, 5, 7]
          280                         [2, 2, 2, 5, 7]
          350                         [2, 5, 5, 7]
          490                         [2, 5, 7, 7]

Скопировать
5 из этих чисел меньше 500, а самое большое из них 490.

primesL = [2, 5, 7]
limit = 500
count_find_num(primesL, val) == [5, 490]

Скопировать
Основа:

def count_find_num(primesL, limit):
    # your code here
    return []

Скопировать
Для проверки:

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
