from exporting import  take_text
from importing import importing

def createhtml():
    lis = take_text()
    style = 'style="font-size:24px;margin:0"'
    html = '<html>\n  <head></head>\n  <body>\n'
    for elem in lis:
        html += '    <p {}>{}</p>'\
            .format(style, elem)
    with open('index.html', 'w') as page:
        page.write(html)
    return html
createhtml()