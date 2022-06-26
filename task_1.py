
# url = "http://github.com/carbonfive/raygun"
# domain_name = "github"

# def domain_name(url):
#   return


# Задание 1
import re
PTRN = r'^(http://github.com/carbonfive/raygun)?(www\.)?([a-z-]*)\..+$'

url = "http://github.com/carbonfive/raygun"
def domain_name(url):
  print(url)
 
  return url.split("www.")[-1].split("//")[-1].split(".")[0]

def domain_name(url)
# regex
m = re.search('https?://([A-Za-z_0-9.-]+).*', 'https://google.co.uk?link=something')
m.group(1)
print(m)

# Задание 2

'''Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:'''


def int32_to_ip(int32):
      
  return


# Задание 3

'''Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:'''

def zeros(n):
    fact=1
    if n==1 or n==0:
        return 1
    elif n<0:
        return 0
    else:
        while n>1:
            fact=n*fact
            n=n-1
        count = 0
        while fact >= 1:
            if fact%10==0:
                count+=1
                fact=fact//10
            else:
                break
    return count


    