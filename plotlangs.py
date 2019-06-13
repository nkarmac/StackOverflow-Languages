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
import numpy as np
import datetime as dt
import matplotlib.dates as mdates

years = [i for i in range(2008,2020)]
months = [i for i in range(1,13)]
dates = []
for year in years:
    for month in months:
        if (year == 2008 and month < 8) or (year == 2019 and month > 2):
            continue
        dates.append(dt.datetime(year,month,1))

for lang in languages:
    filename = './languages/' + lang + '.csv'
    outputfile = './languages/' + lang + '_bestfit.png'
    df = pd.read_csv(filename)

    x = mdates.date2num(dates)
    y = df['count']
    z = np.polyfit(x,y,52)
    f = np.poly1d(z)

    fig, ax = plt.subplots()
    xx = np.linspace(x.min(), x.max(), 100)
    dd = mdates.num2date(xx)
    ax.plot(dd,f(xx), '-g')
    ax.plot(dates,y,'x',color='b')
    plt.gcf().autofmt_xdate()
    plt.gcf().set_size_inches(25.5, 10.5)
    plt.title(lang + ' best fit')
    plt.ylabel('posts')
    plt.savefig(outputfile, dpi=100)