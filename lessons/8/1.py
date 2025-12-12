import time
import itertools

def check_password(password, target):
    return password == target

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
        brute_force(target_password, alphabet, length_test)

