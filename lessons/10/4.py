def mod_pow(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


m = 2 # Буква 'B'
e, n = 7, 33
d = 3

# Шифрование
c = mod_pow(m, e, n)
print(f"Шифруем {m}: c = {m}^{e} mod {n} = {c}")

# Дешифровка
m_decrypted = mod_pow(c, d, n)
print(f"Расшифровываем шифр c={c}: m = {c}^{d} mod {n} = {m_decrypted}")