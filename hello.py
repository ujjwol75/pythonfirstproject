#Tower of Hanoi Problem


def TowerOfHanoi(n, source, dest, middle):
    if n<1:
        Print("Not a valid value.")
        return
    if n==1:
        print("Move disk {} from {} to {}".format(n, source, dest))
        return
    TowerOfHanoi(n-1,source,middle,dest)
    print("Move disk {} from {} to {}".format(n,source,dest))
    TowerOfHanoi(n-1, middle, dest, source)

n = int(input("Enter the no. of disks: "))
TowerOfHanoi(n, "a", "b","c")
        