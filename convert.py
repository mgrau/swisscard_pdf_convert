import re
import pdfplumber
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print('please specify a PDF filename')
    exit()

with pdfplumber.open(input_file) as pdf:
    text = ''.join([page.extract_text() for page in pdf.pages])

lines = text.split('\n')


parse_str = '^(?P<date>(\d\d\.){2}\d{4}) (?P<transaction>\S*) (?P<credit>-)?(?P<amount>(\'|\d)+\.\d\d)$'
prog = re.compile(parse_str)

transactions = [line for line in lines if prog.match(line) is not None]
data = [next(prog.finditer(transaction)).groupdict()
        for transaction in transactions]

print('!Type:CCard')
for transaction in data:
    print(f'D{transaction["date"]}')
    amount = transaction['amount'].replace('\'','')
    payment = transaction['credit'] is None
    print(f'T{"-" if payment else ""}CHF{amount}')
    print(f'P{transaction["transaction"]}')
    print('^')
