import time
import itertools
import multiprocessing

def check_password(password, target):
    return password == target


def worker(start_letter, end_letter, target, alphabet, length, result_queue):
    print(f"This worker is worling with the letters {start_letter, end_letter}")

    process_alphabet = alphabet[start_letter:end_letter]
    attempts = 0
    for password in itertools.product(alphabet, repeat=length):
        password_str = ''.join(password)
        attempts += 1

        if password_str[0] in process_alphabet:
            if check_password(password_str, target):
                result_queue.put((password_str, attempts))
                return

    result_queue.put(None)

def brute_force_multi(target, alphabet, length, num_processes = 4):
    print("Start brute force multi")
    start_time = time.time()

    result_queue = multiprocessing.Queue()

    letters_per_process = len(alphabet) // num_processes

    processes = []

    for i in range(num_processes):
        start_index = i * letters_per_process
        if i == num_processes - 1:
            end_index = len(alphabet)
        else:
            end_index = (i + 1) * letters_per_process

        process = multiprocessing.Process(
            target=worker,
            args=(start_index, end_index, target, alphabet, length, result_queue)
        )
        processes.append(process)
        process.start()

    found_password = None
    total_attempts = 0

    for _ in range(num_processes):
        result = result_queue.get()
        if result is not None:
            found_password, attempts = result
            total_attempts += attempts

    for process in processes:
        process.terminate()
        process.join()

    end_time = time.time()

    if found_password:
        print(f"Password is {found_password}. It took {total_attempts} attempts. And time is {end_time - start_time:.2f}")
    else:
        print("No password")
    return found_password


def brute_force(target, alphabet, length):
    print("Start brute force")
    start_time = time.time()
    attempts = 0
    for password in itertools.product(alphabet, repeat=length):
        password_str = ''.join(password)
        attempts += 1
        if check_password(password_str, target):
            end_time = time.time()
            print(f"Password is {password_str}. It took {attempts} attempts. And time is {end_time - start_time:.2f}")
            return password_str

    print(f"No password with length {length}")
    return None

if __name__ == "__main__":
        target_password = "testte"
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        length_test = 6
        # brute_force(target_password, alphabet, length_test)

        brute_force_multi(target_password, alphabet, length_test, num_processes=12)

