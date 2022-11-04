from random import randint
def get_fullname():
    # return input('Введите свои ФИО: ')
    return str(randint(5, 2000))

def get_phone_number():
        # return input('Укажите свой номер телефона: ') 
      return  str(randint(5, 2000))
def get_description():
        # return input('Описание(необязательно): ')
      return  str(randint(5, 2000))
def data_collection():
    return (get_fullname(), get_phone_number(), get_description())