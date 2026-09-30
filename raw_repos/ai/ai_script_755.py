class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return '{} + {}i'.format(self.real, self.imag)

if __name__ == '__main__':
    c = ComplexNumber(2, 8)
    print(c)