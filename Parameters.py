class parameters:
    def __init__(self):
        self.__class = ''
        self.__id = ''
        self.__name = ''
        self.__size = ''

    def set_class(self, c):
        self.__class = c

    def set_id(self, i):
        self.__id = i

    def set_name(self, n):
        self.__name = n

    def set_size(self, s):
        self.__size = s

    def get_class(self):
        return self.__class

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size
