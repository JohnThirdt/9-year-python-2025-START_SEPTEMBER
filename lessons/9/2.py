import itertools
import time
import string
from multiprocessing import Pool, cpu_count


def check_range(params):
    start_idx, end_idx, alphabet, length, target = params
    my_letters = alphabet[start_idx:end_idx]

    for first in my_letters:
        for tail in itertools.product(alphabet, repeat=length - 1):
            candidate = first + ''.join(tail)
            if candidate == target:
                return candidate
    return None


def brute_force_parallel(alphabet, length, target, processes=None):
    if processes is None:
        processes = cpu_count()

    chunk = len(alphabet) // processes
    tasks = []

    for i in range(processes):
        start = i * chunk
        end = len(alphabet) if i == processes - 1 else (i + 1) * chunk
        tasks.append((start, end, alphabet, length, target))

    with Pool(processes=processes) as pool:
        results = pool.map(check_range, tasks)

    for res in results:
        if res is not None:
            return res
    return None


if __name__ == "__main__":
    alphabet = string.ascii_lowercase + string.digits
    length = 4
    secret = "test"

    start = time.time()
    result = brute_force_parallel(alphabet, length, secret, processes=4)
    end = time.time()

    print(f"Найдено: {result}, время: {end - start:.2f}с")