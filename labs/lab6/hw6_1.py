from collections.abc import MutableMapping
class CustomDict(MutableMapping):
        
    def __init__(self, **kwargs):
        self._data = dict()
        for key, value in kwargs.items():
            self._data[key] = value
            
    def __repr__(self):
        return str(self._data)
        
    def __delitem__(self, key):
        self._data.pop(key)
        
    def __getitem__(self, key):
        pass
        
    def __setitem__(self, key, value):
        if key not in self._data.keys():
            self._data[key] = value
        else:
            print(self._data[key])
            self._data[key] = [self._data[key], value]
        
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
        
    @classmethod
    def from_default(cls, some_dict):
        if type(some_dict) == dict:
            c = CustomDict()
            c._data = some_dict
        else:
            raise ValueError   
        return c
        
        
    def __add__(self, other):
        c = CustomDict()
        if type(other) == dict or type(other) == CustomDict:
            if type(other) == dict:
                other = CustomDict.from_default(other)
                print(other)
            for k, v in other._data.items():
                c[k] = v
            for k, v in self._data.items():
                c[k] = v
        else:
            raise ValueError
        return c
            
    def add(self, other):
        if type(other) == dict or type(other) == CustomDict:
            for k, v in other._data.items():
                self[k] = v
        else:
            raise ValueError
