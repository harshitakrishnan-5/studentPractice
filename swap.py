import sys
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
if __name__=="__main__":
    if len(sys.argv) !=3:
        print("Usage: python swap.py <val1> <val2>")
        sys.exit(1)
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print("Before swapping: a =",a,", b =",b)
    a,b=swap(a,b)
    print("After swapping: a =",a,", b =",b)