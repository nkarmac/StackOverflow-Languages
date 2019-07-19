languages = [
'python'
#'java','c','c++','python','.net', 'c#', 'javascript', 'sql','php','assembly',
#'objective-c', 'delphi', 'perl','matlab','ruby','vba','groovy','swift','go','r',
#'sas','abap','fortran', 'dart','scala', 'prolog', 'lisp', 'lua', 'rust', 'ada',
#'f#', 'apex', 'kotlin', 'scheme', 'labview', 'typescript', 'julia', 'awk', 'haskell',
#'clojure', 'erlang', 'bash', 'elixir', 'html', 'vhdl', 'verilog', 'jquery', 'reactjs'
]

import csv
for lang in languages:
    infile = lang + ".csv"
    data = 0
    with open(infile, "r") as csvfile:
        data = list(csv.reader(csvfile, delimiter = ','))
    with open(infile, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        i = 0
        g = 127
        for row in data:
            if i == 0:
                writer.writerow(row)
                i += 1
                continue
            row[2] = str(int(int(row[2]) / g))
            writer.writerow(row)
            g -= 1
            
            
