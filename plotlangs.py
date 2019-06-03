languages = [
'java','c','c++','python','.net', 'c#', 'javascript', 'sql','php','assembly',
'objective-c', 'delphi', 'perl','matlab','ruby','vba','groovy','swift','go','r',
'sas','abap','fortran', 'dart','scala', 'prolog', 'lisp', 'lua', 'rust', 'ada',
'f#', 'apex', 'kotlin', 'scheme', 'labview', 'typescript', 'julia', 'awk', 'haskell',
'clojure', 'erlang', 'bash', 'elixir', 'html', 'vhdl', 'verilog', 'jquery', 'reactjs'
]

import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

for lang in languages:
    filename = './languages/' + lang + '.csv'
    outputfile = './languages/' + lang + '.png'
    df = pd.read_csv(filename)

    x = df['date']
    y = df['count']

    tick_spacing = 3

    fig, ax = plt.subplots(1,1)
    ax.plot(x,y)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.gcf().autofmt_xdate()
    plt.gcf().set_size_inches(25.5, 10.5)
    plt.savefig(outputfile, dpi=100)