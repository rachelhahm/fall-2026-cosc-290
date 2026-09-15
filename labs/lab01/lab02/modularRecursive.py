def modularRecursive(x: float, y: float, z: float):
    num equation = (x^y)%z
    while(y>1):
        if(y%2 == 0):
            y = y/2
            equation = (x^y)^2%z
        else:
            y = (y-1)/2
            (x*(x^y%z)^2)%23
    print(equation)

def main():
    modularRecursive(4.0,14.0,23.0)

main()