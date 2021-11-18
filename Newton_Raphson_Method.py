# Defining Function
def f(x):
    return pow(x, 2) - x*3 + 2
def g(x):
    return 2*x - 3

if __name__ == '__main__':
    step = 1
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')

# Input Section
    x1 = input('Input First Number: ')
    n = int(input('Input Iteration number : '))

# Converting input to float
    x1 = float(x1)

# Implementing Newton Raphson Method
    for n in range(1, n):
        if f(x1) == 0.0:
            print("Math error!")
            break
        x2 = x1 - (f(x1)/g(x1))
        print('Iteration- %d: x%d = %0.6f  and  f(x1) = %0.6f' % (step, step+1, x2, f(x2)))
        x1 = x2
        step = step + 1

    print('\nRequired Root is : %0.8f' % x2)


