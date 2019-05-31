languages = [
'java','c','c++','python','.net', 'c#', 'javascript', 'sql','php','assembly',
'objective-c', 'delphi', 'perl','matlab','ruby','vba','groovy','swift','go','r',
'sas','abap','fortran', 'dart','scala', 'prolog', 'lisp', 'lua', 'rust', 'ada',
'f#', 'apex', 'kotlin', 'scheme', 'labview', 'typescript', 'julia', 'awk', 'haskell',
'clojure', 'erlang', 'bash', 'elixir', 'html', 'vhdl', 'verilog', 'jquery', 'reactjs'
]

def stringmonth(month):
    if month < 10:
        return '0' + str(month)
    else:
        return str(month)

def next(month, year):
    month += 1
    if (month == 13):
        year += 1
        month = 1
    return month, year

import csv

for lang in languages:

    year = 2008
    month = 8

    nextyear = 2008
    nextmonth = 9

    tagcount = {}
    
    while (year <= 2019 and month <= 2) or year < 2019:
        date = str(year) + '-' + stringmonth(month)
        filename = './all-tags/' + date + '.csv'
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if lang == row[0]:
                    tagcount[date] = row[1]
        
        month, year = next(month, year)
        nextmonth, nextyear = next(nextmonth, nextyear)
    
    outputfile = './languages/' + lang + '.csv'

    with open(outputfile, 'w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        csv_out.writerow(['date', 'count'])
        for date in tagcount:
            csv_out.writerow([date, tagcount[date]])
