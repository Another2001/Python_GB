import data_provider as prov
import logger as log

def infotake():
    data = prov.data_collection()
    log.infotake_logger()
    return data


# def fullname_view():
#     data = prov.get_fullname()
#     log.fullname_logger()
#     return data


# def phone_number_view():
#     data = prov.get_phone_number()
#     log.phone_number_logger()
#     return data

    
# def description_view():
#     data = prov.get_description()
#     log.description_logger()
#     return data

    