from user_interface import infotake as it
from datetime import datetime as dt
from time import time

# def fullname_logger():
#     time = dt.now().strftime('%H:%M')
#     with open('phonebook.csv', 'a') as file:
#         file.write('{};fullname;{}\n'
#                     .format(time, fv()))

# def phone_number_logger():
#     time = dt.now().strftime('%H:%M')
#     with open('phonebook.csv', 'a') as file:
#         file.write('{};phone_number;{}\n'
#                     .format(time, dv()))


# def description_logger():
#     time = dt.now().strftime('%H:%M')
#     with open('phonebook.csv', 'a') as file:
#         file.write('{};description;{}\n'
#                     .format(time, pnv))

def infotake_logger():
    time = dt.now().strftime('%H:%M')
    with open('phonebook.csv', 'a') as file:
        file.write('{};-->;{}\n'
                    .format(time, it()))
