import functools
import time


def delayed(delay=2):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(f'Sleep {delay} seconds')
            time.sleep(delay)
            result = func(*args, **kwargs)
            return result

        return inner

    return decorator


@delayed(1)
def countdown(number):
    if number < 1:
        print('END')
    else:
        print(number)
        countdown(number - 1)