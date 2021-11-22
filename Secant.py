# Defining Function
def f(x):
    return pow(x, 2) - 4*x - 10

if __name__ == '__main__':
    step = 1
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***\n')

    # Input Section
    x1 = input('Input First Number: ')
    x2 = input('Input Second Number: ')
    n = int(input('Input Iteration number : '))

    # Converting input to float
    x1 = float(x1)
    x2 = float(x2)

# Implementing Secant Method
    for n in range(1, n):
        x3 = x2 - ((f(x2) * (x2-x1) / (f(x2)-f(x1))))
        print('Iteration- %d: x%d = %0.6f  and  f(x%d) = %0.6f also f(x%d) = %0.6f' % (step, 2+step, x3, step, f(x1), step+1, f(x2)))
        x1 = x2
        x2 = x3
        step = step + 1

    print('\nRequired Root is : %0.8f' % x3)


