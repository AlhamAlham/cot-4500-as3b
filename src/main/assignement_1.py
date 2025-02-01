def approximation_algorithm(f, x0, tol=1e-5, max_iter=1000):
    """
    Approximation method to find the root of a function f(x).
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        x = x - fx / 2  # Placeholder for approximation step
    return x

def bisection_method(f, a, b, tol=1e-5):
    """
    Bisection method to find the root of f(x) in the interval [a, b].
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have opposite signs at the endpoints.")
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

def fixed_point_iteration(g, x0, tol=1e-5, max_iter=1000):
    """
    Fixed-Point Iteration method to solve x = g(x).
    """
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def newton_raphson_method(f, df, x0, tol=1e-5, max_iter=1000):
    """
    Newton-Raphson method to find roots of f(x).
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero. Cannot continue.")
        x = x - fx / dfx
    return x

if __name__ == "__main__":
    # Example usage
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    g = lambda x: (4 + x) / 2  # g(x) for fixed-point iteration

    print("Approximation Algorithm:", approximation_algorithm(f, 2.0))
    print("Bisection Method:", bisection_method(f, 0, 3))
    print("Fixed-Point Iteration:", fixed_point_iteration(g, 1.0))
    print("Newton-Raphson Method:", newton_raphson_method(f, df, 3.0))
