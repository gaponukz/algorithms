"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
from hash_table.cm_hash_table import HashTable as CainMethodHashTable # for 6.4
from hash_table.oa_hash_table import HashTable as OpenAddressingHashTable # for 6.3

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global library

    library = OpenAddressingHashTable() # or CainMethodHashTable()


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    if author not in library:
        library[author] = []
    
    library[author].append(title)

def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    try:
        return title in library[author]
    
    except KeyError:
        return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    library[author].remove(title)


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    try:
        return sorted(library[author], key=str.lower)

    except KeyError:
        return []
