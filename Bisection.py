# Defining Function
def f(x):
    return pow(x, 2) - 4 * x - 10

# Implementing Bisection Method
if __name__ == '__main__':
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    # Input Section
    x1 = input('Input First Number: ')
    x2 = input('Input Second Number: ')
    n = int(input('Input Iteration number : '))

    # Converting input to float
    x1 = float(x1)
    x2 = float(x2)

    for n in range(1, n):
        x0 = (x1 + x2) / 2
        print('Iteration- %d: x0 = %0.6f  and  f(x0) = %0.6f' % (step, x0, f(x0)))

        if f(x0) == 0:
            print('\nRequired Root is : %0.8f' % x0)
            break
        elif f(x0) * f(x1) < 0:
            x2 = x0
        elif f(x0) * f(x2) < 0:
            x1 = x0
        step = step + 1

    print('\nRequired Root is : %0.8f' % x0)


