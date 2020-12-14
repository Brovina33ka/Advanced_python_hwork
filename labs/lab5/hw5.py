class Library:
    def __init__(self, name):
        self._name = name
        self._bookList = dict()

    def add_book(self, book):
        self._bookList[book._ISNB] = book

    def search_author(self, author):####
        arr_author = []
        for i in self._bookList.values():
            if i._author == author:
                arr_author.append(i._name)
        return arr_author if arr_author != [] else f"В данной библиотеке нет книг автора {author}"
                    

    def present_book(self, book):
        if book._ISNB not in self._bookList.keys():
            raise AssertionError
        else:
            print(book.__dict__)#работает!!!
                
                
    def delete_book(self, book):
        if book._ISNB not in self._bookList.keys():
            raise AssertionError
        else:
            del self._bookList[book._ISNB]
                
                

    

class Book(object):
    def __init__(self, name, author, publisher, pubdate, ISNB: int):
        self._name = name
        self._author = author
        self._publisher = publisher
        self._pubdate = pubdate
        self._ISNB = ISNB
    


def test_library():
    L1 = Library('L1')
    Anna_Karenina = Book('Anna Karenina', 'Лев Толстой', 'Publ1', '1 okt', 1)
    Childhood = Book('Childhood', 'Лев Толстой', 'Publ2', '6 okt', 2)
    War_and_Peace = Book('War and Peace', 'Лев Толстой', 'Publ4', '13 okt', 3)
    L1.add_book(Anna_Karenina)
    L1.add_book(Childhood)
    L1.add_book(War_and_Peace)
    L1.present_book(Anna_Karenina)
    L1.present_book(Childhood)
    L1.present_book(War_and_Peace)
    L1.delete_book(Anna_Karenina)
    L1.delete_book(Childhood)
    L1.delete_book(War_and_Peace)
    print(L1.search_author('Лев Толстой'))
    


if __name__ == '__main__':
    test_library()
    
    
