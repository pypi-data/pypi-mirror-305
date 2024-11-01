import sympy


def gen_big_prime() -> int:
    r = sympy.randprime(2**2047, 2**2048)
    return r


def gen_prime_couple() -> tuple:
    print("Generating a couple numbers.")
    return gen_big_prime(), gen_big_prime()
