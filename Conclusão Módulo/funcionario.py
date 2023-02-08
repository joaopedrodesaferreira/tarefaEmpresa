from datetime import datetime

class Funcionario():
    __idFuncionario: int
    __nomeFuncionario: str
    __cpfFuncionario: str
    __enderecoFuncionario: str
    __dataNascimento: datetime
    __emailFuncionario: str
    __idSetor: int
    __idFuncao: int
    __dataContratacao: datetime
    __nomeSetor: str
    __nomeFuncao: str
    __salarioFuncao: float

    @property
    def idFuncionario(self):
        return self.__idFuncionario
    
    @idFuncionario.setter
    def idFuncionario(self, idFuncionario):
        self.__idFuncionario = idFuncionario
    

    @property
    def nomeFuncionario(self):
        return self.__nomeFuncionario
    
    @nomeFuncionario.setter
    def nomeFuncionario(self, nomeFuncionario):
        self.__nomeFuncionario = nomeFuncionario
    
    
    @property
    def cpfFuncionario(self):
        return self.__cpfFuncionario
    
    @cpfFuncionario.setter
    def cpfFuncionario(self, cpfFuncionario):
        self.__cpfFuncionario = cpfFuncionario
    

    @property
    def enderecoFuncionario(self):
        return self.__enderecoFuncionario
    
    @enderecoFuncionario.setter
    def enderecoFuncionario(self, enderecoFuncionario):
        self.__enderecoFuncionario = enderecoFuncionario
    

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
    

    @property
    def emailFuncionario(self):
        return self.__emailFuncionario
    
    @emailFuncionario.setter
    def emailFuncionario(self, emailFuncionario):
        self.__emailFuncionario = emailFuncionario
    

    @property
    def idSetor(self):
        return self.__idSetor
    
    @idSetor.setter
    def idSetor(self, idSetor):
        self.__idSetor = idSetor
    

    @property
    def idFuncao(self):
        return self.__idFuncao
    
    @idFuncao.setter 
    def idFuncao(self, idFuncao):
        self.__idFuncao = idFuncao

    
    @property
    def dataContratacao(self):
        return self.__dataContratacao
    
    @dataContratacao.setter 
    def dataContratacao(self, dataContratacao):
        self.__dataContratacao = dataContratacao


    @property
    def nomeSetor(self):
        return self.__nomeSetor
    
    @nomeSetor.setter 
    def nomeSetor(self, nomeSetor):
        self.__nomeSetor = nomeSetor


    @property
    def nomeFuncao(self):
        return self.__nomeFuncao
    
    @nomeFuncao.setter 
    def nomeFuncao(self, nomeFuncao):
        self.__nomeFuncao = nomeFuncao
    

    @property
    def salarioFuncao(self):
        return self.__salarioFuncao
    
    @salarioFuncao.setter 
    def salarioFuncao(self, salarioFuncao):
        self.__salarioFuncao =salarioFuncao
    