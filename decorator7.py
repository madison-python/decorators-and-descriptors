with open('pi.txt') as f:
    PI = f.read().strip()  # first 100000 digits of pi as string


def make_pi_from_cache(digits):
    for i in range(digits):
        yield PI[i]


def pi_cache(fn):
    def decorator(digits, *args, **kwargs):
        if digits <= 100000:
            return make_pi_from_cache(digits)
        return fn(digits, *args, **kwargs)

    return decorator


@pi_cache
def make_pi(digits):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for _ in range(digits):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


g = make_pi(100000)
pi = ""

for i, n in enumerate(g):
    pi += str(n)

    if i == 0:
        pi += "."

print(pi)
