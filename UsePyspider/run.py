# -*- coding: utf-8 -*-
from requests import Response,Request

def my_callback(a):
    print(a + 1)


def get(i, callback):
    callback(i)


if __name__ == '__main__':
    get(1, callback=my_callback)
