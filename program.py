cache = {'count': 0, 'result': None}

def cache3(func):
    def wrapper(*args, **kwargs):
        if cache['count'] > 3:
            cache['count'] = 0
            cache['result'] = None
         
        elif cache['count'] in range(1, 3):
            cache['count'] += 1
            return cache['result']
        else:
            result = func(*args, **kwargs)
            cache['count'] += 1
            return cache['count']
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1