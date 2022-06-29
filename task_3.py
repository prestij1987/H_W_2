
#  '''задание № 3Написать метод zeros, который принимает на вход целое число (integer) и
# возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
#
# Будьте осторожны 1000! имеет 2568 цифр.'''

# '''Доп. инфо: http://mathworld.wolfram.com/Factorial.html'''

# zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

def zeros(n):
    res = 0
    i = 5
    
    while n / i >= 1:
        res += n // i
        i *= 5
    
    return res






















# def zeros(n):
#  fact = 1
#  if n == 1 or n == 0:
#   return 1
#  elif n < 0:
#   return 0
#  else:
#   while n > 1:
#    fact = n * fact
#    n = n - 1
#   count = 0
#   while fact >= 1:
#    if fact % 10 == 0:
#     count += 1
#     fact = fact // 10
#    else:
#     break
#   return count
