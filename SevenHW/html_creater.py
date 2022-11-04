from user_interface import fullname_view
from user_interface import description_view
from user_interface import phone_number_view

def create():
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>fullname: {} c</p>\n'\
        .format(style, fullname_view())
    html += '    <p {}>phone_number: {} </p>\n'\
        .format(style, phone_number_view())
    html += '    <p {}>description: {} </p>\n'\
        .format(style, description_view())
    html += '  </body>\n</html>'
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html



# def new_create(data):
#     t, p, w = data
#     style = 'style="font-size:30px;"'
#     html = '<html>\n  <head></head>\n  <body>\n'
#     html += '    <p {}>Temperature: {} c</p>\n'\
#         .format(style, t)
#     html += '    <p {}>Wind_speed: {} m/s</p>\n'\
#         .format(style, w)
#     html += '    <p {}>Pressure: {} mmHg</p>\n'\
#         .format(style, p)
#     html += '  </body>\n</html>'
    
#     with open('new_index.html', 'w') as page:
#         page.write(html)

#     return data