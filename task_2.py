import ipaddress


# """Задача № 2 Написать метод int32_to_ip, который принимает на вход 32-битное целое число
# (integer) и возвращает строковое представление его в виде IPv4-адреса:"""

# 2149583361 ==> "128.32.10.1"
# 32         ==> "0.0.0.32"
# 0          ==> "0.0.0.0"


def int32_to_ip(int32):
    bin_str = f'{int32:b}'.rjust(32, '0')
    return '.'.join([str(int(bin_str[idx:idx + 8], 2)) for idx in range(0, len(bin_str), 8)])

