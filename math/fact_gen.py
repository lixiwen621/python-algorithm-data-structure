# Get the factorial of a number
# 得到一个数的阶乘
def prod(a,b):
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output


def compute_factorial(num):
    if not isinstance(num,int):
        raise ValueError("Please pass the number")
    result = 0
    gen = fact_gen()
    for n in range(num):
        result = next(gen)
    return result


if __name__ == '__main__':
    fact = compute_factorial(5)
    print(fact)