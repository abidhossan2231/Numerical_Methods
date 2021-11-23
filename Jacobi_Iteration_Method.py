# Defining Function
def f(x2, x3):
    return (5 - x2 - x3) / 2
def g(x1, x3):
    return (15 - 3*x1 - 2*x3) / 5
def h(x1, x2):
    return (8 - 2*x1 - x2) / 4

if __name__ == '__main__':
    step = 1
    print('\n\n*** GAUSS-SEIDEL METHOD IMPLEMENTATION ***\n')

    # Input Section
    x1 = input('Input First Number,x1: ')
    x2 = input('Input Second Number,x2: ')
    x3 = input('Input Second Number,x3: ')
    n = int(input('Input Iteration number : '))

    # Converting input to float
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)

    # Implementing Gauss-Seidel Method
    for n in range(1, n):
        xx1 = f(x2, x3)
        xx2 = g(x1, x3)
        xx3 = h(x1, x2)
        print('Iteration- %d: \nx1 = %0.6f  , x2 = %0.6f  , x3 = %0.6f  ' % (step, xx1, xx2, xx3))
        x1 = xx1
        x2 = xx2
        x3 = xx3
        step = step + 1



