
class Exceptions(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self, message)

class ElementAlreadyExists(Exceptions):
    def __init__(self, message='Elemento já existe'):
        self.message = message
        self.code = 400
        super(ElementAlreadyExists, self).__init__(self.message, self.code)

class ElementDoNotExists(Exceptions):
    def __init__(self, message='Elemento não localizado'):
        self.message = message
        self.code = 404
        super(ElementDoNotExists, self).__init__(self.message, self.code)