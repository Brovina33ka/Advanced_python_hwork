import os
import json

from typing import Dict


class BaseDatabase:
    def save(self, text: str) -> None:
        raise NotImplementedError()



class JsonDatabase(BaseDatabase):
    def __init__(self, path: str):
        self._path = path

        os.makedirs(
            os.path.dirname(self._path),
            exist_ok=True,
        )

    def save(self, text: str) -> None:
        with open(self._path, 'a') as f:
            f.write(
                json.dumps({'text': text}) + '\n'
            )
            
    def get(self):
        encoding = 'utf-8'
        with open(self._path, 'r') as f:
            text = json.loads(f.readlines()[-1]) 

class SqlDatabase(BaseDatabase):
    pass
