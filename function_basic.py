def count_to_x(x):
    for i in range(1,x+1):
        print(i)


def do_something(x):
    for i in range(len(x)):
        x[i] = i


def quadrat_wurzel(x:int) -> float:
    """ returns square root of x """
    return x**(1/2)

def is_Even(x:int) -> bool:
    if x % 2 == 0:
        return True
    return False

def is_even(x:int) -> bool:
    return x % 2 == 0 

def is_Odd(x:int) -> bool:
    return not is_Even(x)


if __name__ == "__main__":
    print("Hallo Welt")
    print(__name__)
    print(__file__)
