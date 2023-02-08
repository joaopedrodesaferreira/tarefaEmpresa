class Setor():
    __idSetor: int
    __nomeSetor: str

    @property
    def idSetor(self):
        return self.__idSetor
    
    @idSetor.setter
    def idSetor(self, idSetor):
        self.__idSetor = idSetor
    

    
    @property
    def nomeSetor(self):
        return self.__nomeSetor
    
    @nomeSetor.setter
    def nomeSetor(self, nomeSetor):
        self.__nomeSetor = nomeSetor