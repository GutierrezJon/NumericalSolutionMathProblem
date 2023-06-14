'''
 math olympiad problem
 3^m - 2^m = 65. Solve for m.

 Instead of solving this problem analytically as directed on math olympiad,
 we are going to solve it numerically using the bisection method.
'''
import numpy as np
import time
import functools

def func_timer(func):
    '''Decorator Function Timer'''
    #Functools.wraps preserves functions documentation/metadata
    @functools.wraps(func) 
    def func_wrapper(*args,**kwargs):
        t = time.time()
        func_results = func(*args,**kwargs)
        #Get total time of function call. Round to 9 decimal places
        elapsed_time = np.round(time.time() - t, 9) 
        print(f"Time elapsed: {elapsed_time} seconds.")
        return elapsed_time, func_results 
    return func_wrapper


@func_timer
def bisection(func,a,b,tol,max_iter):
    """Bisection Method for solving roots for continuous function.
        func:       <function>  Function to find roots 
        a:          <double>    Start of interval
        b:          <double>    End of interval
        tol:        <double>    Tolerance for convergence
        max_iter:   <int>       Max number of iterations for method
    """
    #time.sleep(2.5)
    for i in range(max_iter):
        mid = (a+b)/2
        #print(mid)
        if func(mid) == 0 or np.abs((b-a)/2) < tol:
            print(f"Root = {mid}. Converged in {i+1} iterations.")
            return mid, i+1
        
        if np.sign(func(mid)) == np.sign(func(a)):
            a = mid
        else:
            b = mid
    print(f"Max iterations reached. Ending script. Current midpoint value = {mid}.") 
    exit()


def main():
    #Problem definition
    f = lambda m: 3**m - 2**m - 65

    #Parameters
    a = 0.0
    b = 10.0
    tol = 10**(-10)
    max_iter = 50

    #Run Method
    elapsed_time, (root, curr_iter)  = bisection(f,a,b,tol,max_iter)

    with open("output.txt", "w") as g:
        g.write(f"Solution: m = {root} for a tolerance of {tol}.\n"
        f"Converged in {curr_iter} iterations.\n"
        f"Time elapsed = {elapsed_time} seconds.")


if __name__ == "__main__":
    main()
