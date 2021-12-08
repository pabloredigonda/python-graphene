def divisors(num):
    divisors = []
    for i in range (1, num+1):
        if(num % i == 0):
            divisors.append(i)
    return divisors


def run():
    try:
        num = input("Ingresa un número:")
        assert num.isnumeric(), "Ingresa un número válido"
        num = int(num)
        assert num >= 0, "Ingresa un número positivo"
        print(divisors(num))

    except AssertionError as e:
        print(e)

if __name__ == '__main__':
    run()