import itertools
import time
import string


def brute_force_sequential(alphabet, length, target):
    for combo in itertools.product(alphabet, repeat=length):
        candidate = ''.join(combo)
        if candidate == target:
            m = candidate
    return m


if __name__ == "__main__":
    alphabet = string.ascii_lowercase + string.digits
    length = 4
    secret = "test"

    start = time.time()
    result = brute_force_sequential(alphabet, length, secret)
    end = time.time()

    print(f"Найдено: {result}, время: {end - start:.2f}с")