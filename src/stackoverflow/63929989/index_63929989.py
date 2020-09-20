import pandas


def my_func():
    temp = pandas.ExcelFile('temp.xlsx')
    return temp.parse()
