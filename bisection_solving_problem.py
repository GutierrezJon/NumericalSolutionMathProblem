'''
 math olympiad problem
 3^m - 2^m = 65. Solve for m.

 Instead of solving this problem analytically as directed on math olympiad,
 we are going to solve it numerically using the bisection method.
'''
import numpy as np
import time

def func_timer(func):
    '''Decorator Function Timer'''
    def wrapper(*args,**kwargs):
        t = time.process_time()
        func(*args,**kwargs)
        elapsed_time = time.process_time() - t
        print(f"Time elapsed: {elapsed_time}.")
    return wrapper


@func_timer
def bisection(func,a,b,tol,max_iter):
    """Bisection Method for solving roots for continuous function.
        func:       <function>  Function to find roots 
        a:          <double>    Start of interval
        b:          <double>    End of interval
        tol:        <double>    Tolerance for convergence
        max_iter:   <int>       Max number of iterations for method
    """
    for i in range(max_iter):
        mid = (a+b)/2
        #print(mid)
        if func(mid) == 0 or np.abs((b-a)/2) < tol:
            print(f"Root = {mid}. Converged in {i} iterations.")
            return mid
        
        if np.sign(func(mid)) == np.sign(func(a)):
            a = mid
        else:
            b = mid
    print(f"Max iterations Reached. Midpoint value = {mid}") 
    return None


def main():
    #Problem definition
    f = lambda m: 3**m - 2**m - 65

    #Parameters
    a = 0.0
    b = 10.0
    tol = 10**(-10)
    max_iter = 100

    #Run Method
    root = bisection(f,a,b,tol,max_iter)

if __name__ == "__main__":
    main()