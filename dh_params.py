import random, sys

def FLT_test(n: int):
    # base case
    if(n==2 or n==3):
        return True
    else:
        for i in range(20):
            a=random.randint(2,n-2)
            if pow(a,n-1,n)!=1:
                return False
        return True

def make_dh_parameters(digits: int):
    n: int
    g: int

    while(True):    
        q: int = random.randint(10**(digits-1), 10**digits - 1)
        x: bool = FLT_test(q)
        y: bool = FLT_test(2*q+1)
        if(x and y):
            n = 2*q+1
            break
    while (True):
        g = random.randint(2, n-2)
        if pow(g,q,n) !=1:
            break
    return n, g

def main() -> None:
    usage = f"Usage: python3 {sys.argv[0]} <digits>   (digits >= 2)"
    if len(sys.argv) != 2:
        print(usage, file=sys.stderr)
        sys.exit(1)
    try:
        digits = int(sys.argv[1])
    except ValueError:
        print(usage, file=sys.stderr)
        print(f"  {sys.argv[1]!r} is not an integer", file=sys.stderr)
        sys.exit(1)
    if digits < 2:
        print(usage, file=sys.stderr)
        sys.exit(1)

    n, g = make_dh_parameters(digits)
    print(f"n {n}")
    print(f"g {g}")

main()