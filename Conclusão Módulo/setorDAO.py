from setor import Setor
import mysql.connector

class SetorDAO():
    __setor = Setor()

    @property
    def setor(self):
        return self.__setor
    
    @setor.setter
    def setor(self, setor):
        self.__setor= setor


            
    def conectar(self):
        self.__conexao = mysql.connector.connect(host= '' , database = '', user = '', password = '')
        self.__cursor = self.__conexao.cursor()
    


    def listarSetor(self):
        self.conectar()
        sql = 'select * from setor'
        self.__cursor.execute(sql)    
        return self.__cursor
    


    def pesquisarID(self):
        self.conectar()
        sql = 'select * from setor where idSetor=' + str(self.__setor.idSetor)
        self.__cursor.execute(sql)
        respBD = self.__cursor.fetchone()
        self.__setor.idSetor = respBD[0]
        self.__setor.nomeSetor = respBD[1]
        