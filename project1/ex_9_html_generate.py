import csv
from ex_8_csv import generate_fruits_csv

report = ['<!DOCTYPE html>\n']

# generate list data
generate_fruits_csv()
list_data = []
with open ('test.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        list_data.append(row)

html_indent = 0

def indent()->str:
    global html_indent
    if html_indent > 0:
        return '  ' * html_indent
    return ''

def tag_attributes(attributes)->str:
    if attributes and len(attributes) > 0:
        string = ''
        for attr, value in attributes.items():
            string = string + ' ' + attr + '="' + value + '"'
        return string
    return ''

def tag_open(tag, text = None, close = False, attributes = None):
    global html_indent
    report.append(f'{indent()}<{tag}{tag_attributes(attributes)}>\n')
    html_indent += 1
    if text:
        tag_text(text)
    if close:
        tag_close(tag)

def tag_close(tag):
    global html_indent
    if html_indent > 0:
        html_indent -= 1
    report.append(f'{indent()}</{tag}>\n')

def tag_text(text):
    global html_indent
    html_indent += 1
    report.append(f'{indent()}{text}\n')
    html_indent -= 1

def head(title):
    tag_open('html', None, False, {'lang': 'pl', 'class': 'title'})
    tag_open('head')
    tag_open('title', title, True)
    tag_close('head')

def body():
    tag_open('body')
    tag_open('h1', 'Report title', True)
    tag_open('div', 'Report body', False, {'class': 'report-body'})
    tag_open('h2', 'Report paragraph', True)
    tag_close('div')
    tag_open('div')
    tag_open('h3', 'Report list', True)
    tag_list(list_data)
    tag_close('div')

def tag_list(data):
    tag_open('ul')
    for data_row in data:
        tag_open('li')
        tag_open('strong', data_row[0] + ':', True)
        tag_text(data_row[1])
        tag_close('li')
    tag_close('ul')

def footer(footer_text = None):
    if footer_text:
        tag_open('footer')
        tag_open('h3', 'Report footer', True)
        tag_close('footer')
    tag_close('body')
    tag_close('html')

report_name = input('Report file name: ')
file = report_name + '.html'

head('Python report')
body()
footer('&copy; Copy by Python')

# print(report)

f = open(file, 'w')
f.writelines(report)
f.close()