# Defining Function
def f(x):
    return pow(x, 2) + x - 2

if __name__ == '__main__':
    step = 1
    print('\n\n*** FIXED-POINT METHOD IMPLEMENTATION ***')

# Input Section
    x = input('Input First Number: ')
    n = int(input('Input Iteration number : '))

# Converting input to float
    x = float(x)

# Implementing Fixed-Point Method
    for n in range(1, n):

        x1 = 2 - pow(x, 2)
        print('Iteration- %d: x%d = %0.6f  and  f(x1) = %0.6f' % (step, step, x1, f(x1)))
        x = x1
        step = step + 1

    print('\nRequired Root is : %0.8f' % x1)


