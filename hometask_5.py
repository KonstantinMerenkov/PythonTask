# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
def get_file_path(folder: str) -> tuple:
    path, name, ext = '\\'.join(folder.split('\\')[:-1]), folder.split('\\')[-1].split('.')[0], \
                      folder.split('\\')[-1].split('.')[1]
    return path, name, ext


path_file = r'''C:\Users\lepro\PycharmProjects\Django_project\alpha_tempest\stormrage\static\
stormrage_static\images\main.ico'''
print(get_file_path(path_file))  # ('C:\\Users\\lepro\\PycharmProjects\\Django_project\\alpha_tempest\\stormrage\\


# static\\stormrage_static\\images', 'main', 'ico')

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
def get_deposit(customer: list, rate: list, stonks: list) -> dict:
    return {cust: rat / 100 * float(stn) for cust, rat, stn in zip(customer, rate, map(lambda x: x.replace('%', ''),
                                                                                       stonks))}


print(get_deposit(customer=['Timur', 'Max', 'Den'], rate=[10000, 29000, 18000], stonks=['10.25', '9.25', '8.25']))


# вернется: {'Timur': 1025.0, 'Max': 2682.5, 'Den': 1485.0}

# Создайте функцию генератор чисел Фибоначчи
def get_fibonacci(num: int):
    f1, f2 = 0, 1
    for _ in range(num):
        yield f2
        f1, f2 = f2, f1 + f2


for i in get_fibonacci(5):
    print(i, end=' ')  # вернет: 1 1 2 3 5
