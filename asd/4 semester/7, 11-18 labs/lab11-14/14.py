# функция для считывания строки из файла
def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

# функция для вычисления хеш-функции
def hash_func(s):
    p, h = 31, 0
    for i in range(len(s)):
        h = h * p + ord(s[i])
    return h


# функция для реализации алгоритма Рабина-Карпа
def rabin_karp_search(text, pattern):
    # определяем длину строки и образца
    n, m = len(text), len(pattern)
    # вычисляем хеш-функцию для образца и первой подстроки в исходной строке
    p_hash, t_hash = hash_func(pattern), hash_func(text[:m])
    # проходим по каждой возможной подстроке в исходной строке, начиная с позиции m
    for i in range(n - m + 1):
        # если хеш-функции образца и текущей подстроки совпадают
        if p_hash == t_hash:
            # выполняем проверку на полное совпадение
            if text[i:i+m] == pattern:
                return i
        # пересчитываем хеш-функцию для следующей подстроки
        if i < n - m:
            t_hash = (t_hash - ord(text[i]) *
                      pow(31, m-1)) * 31 + ord(text[i+m])
    return -1


input_file = "input.txt"

text = read_file(input_file)
print(f'\nИсходная строка: {text}')
pattern = input("\nВведите образец для поиска: ")
# ищем образец в строке
index = rabin_karp_search(text, pattern)
if index == -1:
    print("\nОбразец не найден!\n")
else:
    print(f"\nОбразец найден в позиции {index}.\n")