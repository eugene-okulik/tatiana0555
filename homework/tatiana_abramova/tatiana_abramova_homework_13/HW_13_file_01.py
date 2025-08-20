import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

dates = []


def read_file():
    with open(okulik_file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    split_text = data_line.split(' - ')
    data_only = split_text[0].split('. ')[1]
    dates.append(data_only)

fmt = '%Y-%m-%d %H:%M:%S.%f'
date1 = datetime.datetime.strptime(dates[0], fmt)
date2 = datetime.datetime.strptime(dates[1], fmt)
date3 = datetime.datetime.strptime(dates[2], fmt)
now = datetime.datetime.now()

print(date1 + datetime.timedelta(weeks=1))
print(date2.strftime('%A'))
print((now - date3).days)
