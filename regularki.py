import re
"""https://regex101.com - тут можно чекать как работают регулярки"""
def main():
    string = '4h54m8s'
    # if matcher := re.match(R"\d", string): #моржовый оператор
    #     print(matcher.group(0))
    # else:
    #     print("No match")


def main2():
    string = '4h54m18s'
    if matcher := re.search(R"\d{2}", string):  #поиск по всей строке
        print(matcher.group(0))
    else:
        print("No match")

def smena():
    string = '4h54m8s'
    result = re.sub(R"\d{2}", "TTT", string) #замена
    print(result)

def razdel():
    string = '4h54m8s'
    result = re.split(R"\D", string) #разделение между цифрами
    print(result)

def optimization():
    string = '4h54m8s'
    double_digit = re.compile(R"\d{2}")  #уже скомпилированное выражение
    result = re.split(double_digit, string) #разделение между цифрами
    print(result)

main()
main2()
smena()
razdel()