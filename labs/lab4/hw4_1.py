from typing import Callable
import sys

def func1():
    pass

def author(arg1):
    def wrapped_func():
        func1._author = arg1
    return wrapped_func
 
if __name__ == '__main__':
    func = author(input())
    func()
    print('Автор программы:', func1._author)

