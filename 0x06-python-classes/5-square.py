
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the calculated the area of Square instance"""
        return self.size ** 2

    def my_print(self):
        """Prints to stdout the square with # or an empty line if size is 0"""
        if self.size == 0:
            print("")
        for i in range(self.size):
            print("#" * self.size)
~

