from endpoints.exceptions import ElementAlreadyExists, ElementDoNotExists

class Endpoint:

    def __init__(self):
        pass

    def elementAlreadyExists(self, elemento, lista):
        retorno = elemento in lista
        return retorno

    def addElement(self, elemento, lista):
        elementoAlreadyExists = elemento in lista
        if elementoAlreadyExists == False:
            lista.append(elemento)
        else:
            raise ElementAlreadyExists

    def deleteElement(self, elemento, lista):
        elementoAlreadyExists = elemento in lista
        if elementoAlreadyExists == True:
            lista.pop(lista.index(elemento))
        else:
            raise ElementDoNotExists