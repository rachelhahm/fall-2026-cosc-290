def modularRecursive(x: int, y: int, z: int):
    equation = (x ** y) % z
    if y!=1:
        if y%2 == 0:
            return ((modularRecursive(x,(y//2),z))**2)%z
        else:
            return(x*modularRecursive(x,(y-1),z)**2)%z
    else:
        return equation


def main():
    print(modularRecursive(4,14,23))

main()