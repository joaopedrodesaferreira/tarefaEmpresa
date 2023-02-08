from sys import settrace


class Funcao():
    __idFuncao: int
    __nomeFuncao: str
    __salario: float

    @property
    def idFuncao(self):
        return self.__idFuncao
    
    @idFuncao.setter
    def idFuncao(self, idFuncao):
        self.__idFuncao = idFuncao
    


    @property
    def nomeFuncao(self):
        return self.__nomeFuncao
    
    @nomeFuncao.setter
    def nomeFuncao(self, nomeFuncao):
        self.__nomeFuncao = nomeFuncao
    


    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario