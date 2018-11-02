# -*- coding: utf-8 -*-
import csv
import pandas as pd


def write_to_csv():
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=' ')   # delimiter为设置列与列之间的分隔符
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(('10001', 'Mike', 20))
        writer.writerow(('10002', 'Bob', 22))
        writer.writerow(['10003', 'Jordan', 21])
    pass


def write_to_csv2():
    with open('data2.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'age'])
        writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])


def write_dict_to_csv():
    with open('data3.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
        writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
    pass


def write_add_to_csv():
    with open('data3.csv', 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'id': '10004', 'name': '宋文济', 'age': 22})
    pass


def read_from_csv():
    with open('data3.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    pass


def use_pandas_read_csv():
    df = pd.read_csv('data3.csv')
    print(df)
    pass


def use_pandas_write_csv():
    f = pd.DataFrame(data=[['10001', 'Mike', 20]], columns=['id', 'name', 'age'])
    f.to_csv('data4.csv')
    pass


if __name__ == '__main__':
    # write_to_csv2()
    # write_dict_to_csv()
    # write_add_to_csv()
    # read_from_csv()
    # use_pandas_read_csv()
    use_pandas_write_csv()
