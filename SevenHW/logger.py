from datetime import datetime as dt
from time import time
from data_provider import data_collection

def data_collection_logger():
    time = dt.now().strftime('%H:%M')
    with open('phonebook.csv', 'a', encoding ='utf-8') as file:
        file.write('{} --> {}\n'
                    .format(time, data_collection()))

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