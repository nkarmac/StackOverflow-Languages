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

for lang in languages:
    filename = './languages/' + lang + '.csv'
    outputfile = './languages/' + lang + '.png'
    df = pd.read_csv(filename)

    x = df['date']
    y = df['count']

    diff = np.diff(y)
    diff = np.insert(diff, 0, 0)

    tick_spacing = 3

    fig, ax = plt.subplots(1,1)
    ax.plot(x,y)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.gcf().autofmt_xdate()
    plt.gcf().set_size_inches(25.5, 10.5)
    plt.title(lang)
    plt.xlabel('date')
    plt.ylabel('posts')
    plt.savefig(outputfile, dpi=100)

    years = [i for i in range(2008,2020)]
    months = [i for i in range(1,13)]
    dates = []
    for year in years:
        for month in months:
            if (year == 2008 and month < 8) or (year == 2019 and month > 2):
                continue
            dates.append(dt.datetime(year,month,1))

    print(diff)
    x = mdates.date2num(dates)
    z = np.polyfit(x,diff,52)
    f = np.poly1d(z)
    
    outputfile = './languages/' + lang + '_slope' + '.png'
    fig, ax = plt.subplots()
    xx = np.linspace(x.min(), x.max(), 100)
    dd = mdates.num2date(xx)
    ax.plot(dd,f(xx), '-g')
    ax.plot(dates,diff,'x',color='b')
    plt.gcf().autofmt_xdate()
    plt.gcf().set_size_inches(25.5, 10.5)
    plt.title(lang + ' slope')
    plt.ylabel('posts')
    plt.savefig(outputfile, dpi=100)