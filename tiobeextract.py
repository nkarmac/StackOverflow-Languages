import requests
import re
import csv

languages = [
    'java', 'python', 'c', 'cplusplus', 'csharp', 'visual-basic-dotnet', 'javascript', 'php', 'sql',
    'objective-c', 'ruby', 'assembly-language', 'swift', 'matlab', 'groovy', 'go',
    'visual-basic', 'delphi-object-pascal', 'perl', 'r', 'sas', 'dart', 'scala'
]

languages_filename = [
    'c', 'c++', 'c#', '.net', 'javascript', 'php', 'sql',
    'objective-c', 'ruby', 'assembly', 'swift', 'matlab', 'groovy', 'go',
    'vba', 'delphi', 'perl', 'r', 'sas', 'dart', 'scala'
]
for (lang, filelang) in zip(languages, languages_filename):

    url = 'https://www.tiobe.com/tiobe-index/' + lang + '/'
    data = requests.get(url)

    graph = re.findall('\[Date.UTC\((.*?), (.*?), .*?, (.*?)\]', data.text)

    def stringmonth(month):
        if month < 10:
            return '0' + str(month)
        else:
            return str(month)

    infile = './languagesv2/' + filelang + '.csv'

    with open(infile, "r") as csvfile:
        data = list(csv.reader(csvfile, delimiter = ','))
    with open(infile, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        i = 0
        oldrating = None
        for row in data:
            if i == 0:
                row.append('tiobe rating')
                writer.writerow(row)
                i += 1
                continue
            ratingfound = False
            for node in graph:
                date = str(node[0]) + '-' + stringmonth(int(node[1])+1)
                if row[0] == date:
                    ratingfound = True
                    rating = str(node[2])
                    oldrating = rating
                    print('YES')
                    row.append(rating)
                    writer.writerow(row)
                    break
            if ratingfound == False:
                if oldrating is None:
                    rating = '0'
                else:
                    rating = oldrating
                print('NO')
                row.append(rating)
                writer.writerow(row)