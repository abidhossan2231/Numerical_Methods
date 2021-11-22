# Defining Function
def f(x, y):
    return pow(x, 2) - pow(y, 2) - 3
def g(x, y):
    return pow(x, 2) + x*y - 6

if __name__ == '__main__':
    step = 1
    print('\n\n*** FIXED-POINT METHOD FOR A SYSTEM IMPLEMENTATION ***')

# Input Section
    x0 = input('Input First Number,x0: ')
    y0 = input('Input First Number,y0: ')
    e = input('Input tolerable error,e: ')
    n = int(input('Input Iteration number : '))

# Converting input to float
    x0 = float(x0)
    y0 = float(y0)
    e = float(e)

# Implementing Fixed-Point Method For a System
    for n in range(1, n):
        x1 = y0 + (3/(x0+y0))
        y1 = (6 - pow(x0, 2))/x0
        print('Iteration- %d: x%d = %0.6f  and y%d = %0.6f ' % (step, step, x1, step, y1))
        if (x1-x0) < e and (y1-y0) < e:
            print('\nx%d = %0.6f  and y%d = %0.6f ' % (step, x1, step, y1))

        x0 = x1
        y0 = y1

        step = step + 1
