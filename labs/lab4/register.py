from typing import Callable
import argparse
import json
import sys

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--surname', required=True)
    parser.add_argument('--middle_name', default=None)
    parser.add_argument('--age', required=True)
    parser.add_argument('--sex', choices=['M', 'F'], required=True)
    parser.add_argument ('--married', action='store_true', default=False)
    parser.add_argument ('--hobbies', default=None)
    args = parser.parse_args()
    args_dict = vars(args)

    return args_dict

if __name__ == '__main__':
    args_dict = createParser()
    with open("journal.txt", 'w') as file:
        json.dump(args_dict, file)


#--name: имя (строка; обязательный).
#--surname: фамилия (строка; обязательный).
#--middle_name: отчество (строка; необязательный, по умолчанию None).
#--age: возраст (целое число; обязательный).
#--sex: пол (строка, всего два возможных значения: "M" и "F"; обязательный).
#--married: состоит ли в браке (булевское значение; необязательный, по умолчанию False). Если этот параметр есть, то значение married должно становиться True. То есть писать надо не напрямую <params> --married True <other params>, а просто <params> --married <other params>.
#--hobbies: хобби (список строк; необязательный, по умолчанию None).

        
    
