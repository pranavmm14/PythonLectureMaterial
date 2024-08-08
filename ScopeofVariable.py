def f1():
    global var
    var= 30
    print("Value in f1", var)

    
def f2():
    global var
    var=10
    print("Value in f2", var)

def f3():
    global var
    print("Value in f3",var)

f1()
f2()
f3()


def sum_all(a,b,*args):
    """
    This function sums all the positional arguments passed to it.
    
    Parameters:
    *args (tuple): Variable length argument list of numbers to be summed.
    
    Returns:
    int/float: The sum of all the arguments.
    """
    return a+b+sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(5,10))   # Output: 30


def mix_args(*args, **kwargs):
    """
    This function prints out positional and keyword arguments passed to it.
    
    Parameters:
    *args (tuple): Variable length argument list of positional arguments.
    **kwargs (dict): Variable length argument dictionary of keyword arguments.
    """
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mix_args(1, 2, 3, name="Alice", age=25)