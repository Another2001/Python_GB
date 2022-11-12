def createhtml():
    lis = open("NineHW/task1/db.json","r").read()
    style = 'style="font-size:24px;margin:0"'
    html = '<html>\n  <head></head>\n  <body>\n'
    for elem in lis:
        html += '    <p {}>{}</p>'\
            .format(style, elem)
    with open('NineHW/task1/db.html', 'w') as page:
        page.write(html)
    return html