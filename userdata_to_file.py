class User:
    """Создал класс User, для ввода пользовательских данных, ввел классметоды для проверки этих данных"""

    def __init__(self, fio, birthdate, phone_number, sex):
        if User.is_correct_fio(fio):
            self.fio = fio
        if User.is_correct_birthdate(birthdate):
            self.birthdate = birthdate
        if User.is_correct_phone(phone_number):
            self.phone_number = phone_number
        if User.is_correct_sex(sex):
            self.sex = sex

    @classmethod
    def is_correct_fio(cls, fio):
        return all(map(str, fio.split())) and len(fio.split()) == 3

    @classmethod
    def is_correct_birthdate(cls, birthdate):
        return all(map(int, birthdate.split(':')))

    @classmethod
    def is_correct_phone(cls, phone_number):
        return isinstance(phone_number, int)

    @classmethod
    def is_correct_sex(cls, sex):
        return sex.lower() == 'f' or sex.lower() == 'm'

    def data_getter(self):
        """геттер строки со всей инфой класса"""
        return f'<{self.fio.split()[0]}><{self.fio.split()[1]}><{self.fio.split()[2]}><{self.birthdate}>' \
               f'<{self.phone_number}><{self.sex}>'


class IncorrectDataQuant(Exception):
    """Пользовательский класс для сигнализации юзера о нехватке переданных данных"""

    pass


# создаю экзмепляр класса с инпутами
user = User(input('Введите ФИО полностью через пробел\n'), input('Введите дату рождения в формате д:м:г\n'),
            int(input('Введите номер телефона через восьмерку\n')), input('Введите пол m или f\n'))
# используя контекстный менеджер записываю результат в файл
with open(r'C:\Users\lepro\Desktop\tasking.txt', 'w', encoding='UTF-8') as file:
    if len(user.__dict__) == 4:
        file.writelines(user.data_getter())
    else:
        raise IncorrectDataQuant('You putted incorrect number of data')

# здесь через контекстный менеджер открываю файл и если его нет то обрабатываю ошибку
try:
    with open(r'C:\Users\lepro\Desktop\tasking.txt', 'r', encoding='UTF-8') as file:
        print(file.readline())
except FileNotFoundError:
    print('Sorry, seems like there is no your file')
