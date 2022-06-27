

# Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.


def count_find_num(primesL, limit):
    primes = []
    primes_new = []
    Primescount = 1
    Max_primes = 0
    for i in range(0, len(primesL)):
        Primescount *= primesL[i]
    for i in range(0, limit):
        primes.append(i)
    for i in range(0, limit-1):
        if primes[i] != 0 and primes[i] % Primescount == 0:
            primes_new.append(primes[i])
    for i in range(1, (len(primes_new)-1)):
        if primes_new[i] > primes_new[i-1]:
            Max_primes = primes_new[i]
    return [len(primes_new)-1, Max_primes]
 
primesL = list(map(int, input().split()))
limit = int(input())
print(count_find_num(primesL, limit))
